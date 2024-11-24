from fastapi import FastAPI, File, UploadFile
import uvicorn
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from preprocessing_module import preprocess_image_manually
import logging
from model import load_model
from preprocess import jpg_verify
from config import configure_cors

# Configura el nivel de registro para mostrar mensajes de depuración
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

app = FastAPI()
configure_cors(app)

# Configura FastAPI para servir archivos estáticos desde la carpeta '/assets/audio'
app.mount("/assets/audio", StaticFiles(directory="assets/audio"), name="audio")

# Obtén la ruta del directorio donde está este script
current_dir = Path(__file__).parent
IMG_SIZE = (180, 180)

modelo = load_model(current_dir)

# Ruta para cargar y clasificar una imagen
@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    if not modelo:
        return {"error": "El modelo no se ha cargado correctamente."}
    if not jpg_verify(file):
        return {"prediction":None, "error": "El archivo no es una imagen JPEG válida."}
    file.file.seek(0)
    try:
        file_content = await file.read()  # Lee el archivo en memoria
        if not file_content:  # Verifica si el archivo está vacío
            return {"prediction": None, "error": "El archivo está vacío."}
        
        # Guardar la imagen temporalmente
        temp_image_path = current_dir / "temp_image.jpg"  # Ruta temporal
        with open(temp_image_path, "wb") as buffer:
            buffer.write(file_content)  # Guarda el contenido previamente leído

        # Llamar a preprocess_image_manually con la ruta temporal
        image_ready = preprocess_image_manually(str(temp_image_path), image_size=(180, 180), color_mode="rgb")

        # Realizar la predicción con el modelo
        prediction = modelo.predict(image_ready)
        _logger.info(f"predicción hecha{prediction}")

        # Asumiendo que el modelo devuelve un valor cercano a 0 para 'cat' y cercano a 1 para 'dog'
        predicted_class = "dog" if prediction[0][0] > 0.5 else "cat"
        sound_url = f"http://127.0.0.1:8000/assets/audio/ladrido1.mp3" if prediction[0][0] > 0.5 else f"http://127.0.0.1:8000/assets/audio/maullido1.mp3"

        # Opcional: Eliminar el archivo temporal después de su uso
        temp_image_path.unlink(missing_ok=True)  # Elimina el archivo si existe

        return {"prediction": predicted_class, "sound_url": sound_url}
    except Exception as e:
        return {"prediction": None, "error": f"Error procesando la imagen: {e}"}

if __name__ == "__main__":
    # Esto inicia el servidor cuando ejecutas el script de Python
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)