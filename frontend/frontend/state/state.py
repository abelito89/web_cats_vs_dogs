import reflex as rx
import aiohttp

class AppState(rx.State):
    img: str = ""
    prediction: str = ""

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Envía la imagen a la API FastAPI."""
        file = files[0]  # Solo manejar el primer archivo
        if files:
            async with aiohttp.ClientSession() as session:
            
                form = aiohttp.FormData()
                form.add_field("file", await file.read(), filename=file.filename, content_type="image/jpeg")
                
                async with session.post("http://127.0.0.1:8000/predict/", data=form) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        print(data)  # Esto imprimirá todo el diccionario devuelto por FastAPI
                        self.prediction = data["prediction"]
                        self.img = data["image_url"]
                        print(f"Image URL: {self.img}")   # Comprueba que la URL es la correcta
                    
                    else:
                        self.prediction = "Error al subir la imagen"
