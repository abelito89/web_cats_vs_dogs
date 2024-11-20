import reflex as rx
import aiohttp
import logging
import base64

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

class AppState(rx.State):
    img: str = ""
    prediction: str = ""
    sound_url: str = ""


    async def handle_upload(self, files: list[rx.UploadFile]):
        """Envía la imagen a la API FastAPI y muestra la imagen cargada."""
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
                
                async with session.post("http://127.0.0.1:8000/predict/", data=form) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        _logger.info(data)  # Esto imprimirá todo el diccionario devuelto por FastAPI
                        # Verifica si "prediction" es None
                        if data.get("prediction") is None:
                            self.prediction = data.get("error", "Error desconocido")

                        else:
                            self.prediction = data["prediction"]
                            self.sound_url = data.get("sound_url","")
                            """self.img = data["image_url"]"""
                            """_logger.info(f"Image URL: {self.img}")"""   # Comprueba que la URL es la correcta
                    else:
                        self.prediction = "Error al subir la imagen"
                        self.sound_url = ""
