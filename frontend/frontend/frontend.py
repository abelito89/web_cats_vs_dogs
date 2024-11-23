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
    box = rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.box(
                        upload_button(),  # Botón para subir imágenes
                        rx.cond(
                            AppState.img != "",  # Mostrar la imagen apenas esté disponible
                            rx.image(
                                src=AppState.img,
                                width="300px",  # Define un ancho fijo para todas las imágenes
                                height="auto",  # Ajusta la altura automáticamente para mantener la proporción
                                margin_top="1em"
                            )
                        ),
                        width="300px"
                    ),
                    rx.cond(
                        AppState.prediction != "",  # Mostrar predicción y reproducir audio si está disponible
                        rx.vstack(
                            rx.cond(
                                AppState.prediction == "cat",
                                rx.text(
                                    "Esto es un gato", 
                                    margin="0.5em auto",
                                    font_size="1.2em",
                                    text_align="center",
                                    ),
                                rx.text(
                                    "Esto es un perro", 
                                    margin="0.5em auto",
                                    font_size="1.2em",
                                    text_align="center",
                                    )
                            ),
                            rx.audio(
                                url=AppState.sound_url,
                                autoplay=True,
                                controls=True,  # Oculta los controles
                                margin_top = "auto"
                            ),
                            spacing="1em",
                            align_items="center",
                        ),
                        rx.text(    
                            "Por favor, sube una imagen para obtener un resultado.",
                            text_align="center",  # Centrar texto inicial
                            margin_top="1em",
                                ),
                    ),
                spacing="1em",  # Espaciado uniforme entre elementos                
                )
            ),
        width="100%",  # Usar todo el ancho disponible
        padding="2em",
        #background_color="#1c1c1c",  # Fondo oscuro para contraste
        align="center"
        )    
    )
    return box



app = rx.App(State=AppState, config=config)
app.add_page(index)