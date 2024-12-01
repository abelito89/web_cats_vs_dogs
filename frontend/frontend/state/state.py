import reflex as rx
import aiohttp
import logging
import base64
import os

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

class AppState(rx.State):
    """
    Estado de la aplicación para manejar la carga de imágenes y las predicciones.

    Atributos:
    ----------
    img : str
        La URL de la imagen cargada en formato Base64.
    prediction : str
        La predicción realizada por el modelo ('cat' o 'dog').
    sound_url : str
        La URL del sonido correspondiente a la predicción.
    """
    img: str = ""
    prediction: str = ""
    sound_url: str = ""

    async def handle_upload(self, files: list[rx.UploadFile]):
        """
        Maneja la carga de imágenes y envía la imagen a la API FastAPI para obtener una predicción.

        Esta función lee el archivo de imagen subido, lo convierte a Base64 para mostrarlo en la interfaz,
        y lo envía al backend para obtener una predicción. Actualiza el estado de la aplicación con la
        imagen cargada, la predicción y la URL del sonido correspondiente.

        Parámetros:
        -----------
        files : list[rx.UploadFile]
            Lista de archivos subidos por el usuario. Solo se maneja el primer archivo de la lista.

        Retorna:
        --------
        None
        """
        file = files[0]  # Solo manejar el primer archivo

        if file:
            # Leer los datos del archivo
            file_data = await file.read()

            # Obtener el tipo de contenido
            content_type = file.content_type

            # Convertir los datos a Base64 usando el módulo base64
            base64_data = base64.b64encode(file_data).decode('utf-8')

            # Generar el Data URL para mostrar la imagen
            self.img = f"data:{content_type};base64,{base64_data}"
            
            # Enviar la imagen al backend
            async with aiohttp.ClientSession() as session:
                form = aiohttp.FormData()
                form.add_field("file", file_data, filename=file.filename, content_type="image/jpeg")
                backend_ip_address = os.getenv("BACKEND_IP_ADDRESS", "localhost")
                async with session.post(f"http://{backend_ip_address}:8000/predict/", data=form) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        _logger.info(data)  # Esto imprimirá todo el diccionario devuelto por FastAPI
                        # Verifica si "prediction" es None
                        if data.get("prediction") is None:
                            self.prediction = data.get("error", "Error desconocido")
                        else:
                            self.prediction = data["prediction"]
                            self.sound_url = data.get("sound_url", "")
                            """self.img = data["image_url"]"""
                            """_logger.info(f"Image URL: {self.img}")"""   # Comprueba que la URL es la correcta
                    else:
                        self.prediction = "Error al subir la imagen"
                        self.sound_url = ""

