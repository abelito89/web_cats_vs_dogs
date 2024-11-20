import reflex as rx
from frontend.components.navbar import navbar
from frontend.components.image_upload_button import upload_button
from frontend.state.state import AppState
import logging

from rxconfig import config


logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

api_url = "http://127.0.0.1:8000/predict/"

def audio_reproductor(audio):
    _logger.debug(f"Reproduciendo audio: {audio}")  # Registro de prueba
    print(f"Reproduciendo audio: {audio}")  # Agrega esta línea para ver si se llama en el navegador
    return rx.audio(
        src=f"/assets/audio/{audio}",
        autoplay=True
    )

def index():
    """Vista principal de la aplicación."""
    _logger.debug(f"Valor de AppState.prediction: {AppState.prediction}")
    return rx.vstack(
        upload_button(),  # Botón para subir imágenes
        rx.cond(
            AppState.img != "",  # Mostrar la imagen apenas esté disponible
            rx.image(src=AppState.img),
        ),
        rx.cond(
            AppState.prediction != "",
            rx.cond(
                AppState.prediction == "cat",
                rx.fragment(
                    rx.text("Esto es un gato"),
                    rx.audio(
                        url=AppState.sound_url,
                        autoplay=True,
                        controls=False,
                    )
                ),
                rx.fragment(
                    rx.text("Esto es un perro"),
                    rx.audio(
                        url=AppState.sound_url,
                        autoplay=True,
                        controls=False,
                    )
                )
            ),
            rx.text("Por favor, sube una imagen para obtener un resultado.")
        ),
        padding="5em",
    )



app = rx.App(State=AppState, config=config)
app.add_page(index)