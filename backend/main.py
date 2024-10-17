from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import uvicorn
from io import BytesIO
from pathlib import Path
from tensorflow import keras

app = FastAPI()

# Obtén la ruta del directorio donde está este script
current_dir = Path(__file__).parent

# Construir una ruta para un archivo llamado 'file.txt' en un subdirectorio llamado 'data'
model_path = current_dir / "models" / "modelo_xception_cats_vs_dogs"

# Cargar el modelo (suponiendo que ya está entrenado y guardado como 'model.h5')
modelo = keras.models.load_model(model_path)

# Definir el tamaño de entrada de la imagen (según fue entrenado el modelo)
IMG_SIZE = (224, 224)

# Función para cargar y preprocesar la imagen
def read_imagefile(file):
    pass

def preprocess_image(image):
    pass

# Ruta para cargar y clasificar una imagen
@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # Leer el archivo y procesar la imagen
    pass


if __name__ == "__main__":
    # Esto inicia el servidor cuando ejecutas el script de Python
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)