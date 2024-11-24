import logging
from fastapi import UploadFile
from PIL import Image
from typing import Optional

# Configura el nivel de registro para mostrar mensajes de depuración
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def jpg_verify(file: UploadFile) -> Optional[bool]:
    """
    Verifica si un archivo subido es una imagen JPEG válida.

    Parámetros:
    -----------
    file : UploadFile
        El archivo de imagen subido por el usuario.

    Retorna:
    --------
    Optional[bool]
        True si el archivo es una imagen JPEG válida, None si no lo es o si ocurre un error.

    Manejo de Excepciones:
    ----------------------
    AttributeError
        Si el archivo no tiene los atributos correctos para ser procesado.
    OSError, IOError
        Si hay errores relacionados con el sistema de archivos, como archivos corruptos o inválidos.
    Exception
        Para capturar cualquier otra excepción general no prevista.
    """
    try:
        # Intentar abrir la imagen usando Pillow
        with Image.open(file.file) as img:
            # Verificar si el formato de la imagen es JPEG
            return img.format == "JPEG"
    except AttributeError:
        # Manejar errores si el archivo no tiene los atributos correctos
        _logger.error("Error: El archivo no tiene los atributos correctos para ser procesado.")
        return None
    except (OSError, IOError) as e:
        # Captura errores relacionados con el sistema de archivos, como archivos corruptos o inválidos
        _logger.error(f"Error de sistema de archivos: {e}")
        return None
    except Exception as e:
        # Captura cualquier otra excepción general no prevista
        _logger.error(f"Error inesperado: {e}")
        return None