from tensorflow import keras
import logging

# Configura el nivel de registro para mostrar mensajes de depuración
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def load_model(current_dir):
    # Construir una ruta para un archivo llamado 'file.txt' en un subdirectorio llamado 'data'
    model_path = current_dir / "models" / "modelo_xception_cats_vs_dogs"

    # Cargar el modelo (suponiendo que ya está entrenado y guardado como 'model.h5')
    try:
        modelo = keras.models.load_model(model_path)
        _logger.info("Modelo cargado exitosamente")
    except Exception as e:
        _logger.error(f"Error al cargar el modelo: {e}")
        modelo = None
    return modelo

   