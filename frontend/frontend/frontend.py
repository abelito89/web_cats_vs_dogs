import reflex as rx
from frontend.components.navbar import navbar
from frontend.components.image_upload_button import upload_button
from frontend.state.state import AppState
import logging

from rxconfig import config


logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


def index():
    """Vista principal de la aplicación."""
    return rx.vstack(
        upload_button(),  # Botón para subir imágenes
        rx.cond(
            AppState.img != "",  # Mostrar la imagen apenas esté disponible
             rx.image(
                src=AppState.img,
                width="300px",  # Define un ancho fijo para todas las imágenes
                height="auto",  # Ajusta la altura automáticamente para mantener la proporción
            ),
        ),
        rx.cond(
            AppState.prediction != "",  # Mostrar predicción y reproducir audio si está disponible
            rx.fragment(
                rx.cond(
                    AppState.prediction == "cat",
                    rx.text("Esto es un gato"),
                    rx.text("Esto es un perro")
                ),
                rx.audio(
                    url=AppState.sound_url,
                    autoplay=True,
                    controls=True,  # Oculta los controles
                ),
            ),
            rx.text("Por favor, sube una imagen para obtener un resultado."),
        ),
        padding="5em",
    )



app = rx.App(State=AppState, config=config)
app.add_page(index)