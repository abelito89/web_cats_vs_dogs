import reflex as rx
from frontend.components.navbar import navbar
from frontend.components.image_upload_button import upload_button
from frontend.components.image_display import image_display
from frontend.components.prediction_display import prediction_display
from frontend.state.state import AppState
import logging

from rxconfig import config


logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


def index():
    """Vista principal de la aplicación."""
    box = rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    upload_button(),  # Botón para subir imágenes
                    image_display(),                 
                    width="300px",
                    align = "center"
                ),
                prediction_display(),
            spacing="1em",  # Espaciado uniforme entre elementos                   
            ),
        width="100%",  # Usar todo el ancho disponible
        padding="2em",
        #background_color="#1c1c1c",  # Fondo oscuro para contraste
        align="right"
        )    
    )
    return box



app = rx.App(State=AppState, config=config)
app.add_page(index)