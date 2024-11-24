from tensorflow import keras
import logging

# Configura el nivel de registro para mostrar mensajes de depuración
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def load_model(current_dir):
    """
    Carga un modelo de aprendizaje profundo desde un directorio especificado.

    Esta función construye la ruta al modelo almacenado en un subdirectorio llamado 'models'
    y carga el modelo utilizando Keras. Si el modelo se carga correctamente, se registra un mensaje
    de éxito. Si ocurre un error durante la carga, se registra el error y se devuelve None.

    Parámetros:
    -----------
    current_dir : Path
        El directorio actual desde el cual se construye la ruta al modelo.

    Retorna:
    --------
    keras.Model o None
        El modelo cargado si se carga correctamente, o None si ocurre un error.
    """
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

   