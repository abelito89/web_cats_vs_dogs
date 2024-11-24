from pydantic import BaseModel
from typing import Optional

class PredictionResponse(BaseModel):
    """
    Modelo de respuesta para la predicción de imágenes.

    Esta clase define la estructura de la respuesta que se envía al cliente después de realizar
    una predicción de imagen. Incluye la predicción, la URL del sonido correspondiente y cualquier
    mensaje de error que pueda haber ocurrido durante el proceso.

    Atributos:
    ----------
    prediction : Optional[str]
        La predicción realizada por el modelo ('cat' o 'dog'). Puede ser None si ocurre un error.
    sound_url : Optional[str]
        La URL del sonido correspondiente a la predicción. Puede ser None si ocurre un error.
    error : Optional[str]
        Un mensaje de error si ocurre algún problema durante el proceso de predicción.
    """
    prediction: Optional[str] = None
    sound_url: Optional[str] = None
    error: Optional[str] = None
