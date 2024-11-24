import reflex as rx
from frontend.state.state import AppState

def prediction_display() -> rx.Component:
    """
    Muestra la predicción de la imagen y reproduce un audio correspondiente.

    Esta función crea un componente de Reflex que muestra el resultado de la predicción
    (gato o perro) y reproduce un audio correspondiente si hay una predicción disponible.
    Si no hay predicción, muestra un mensaje solicitando al usuario que suba una imagen.

    Retorna:
    --------
    rx.Component
        Un componente de Reflex que representa la visualización de la predicción y el audio.
    """
    box = rx.box(
        rx.cond(
            AppState.prediction != "",  # Mostrar predicción y reproducir audio si está disponible
            rx.vstack(
                rx.cond(
                    AppState.prediction == "cat",
                    rx.text(
                        "Esto es un gato", 
                        margin="0 auto",
                        font_size="1.2em",
                        text_align="center",
                    ),
                    rx.text(
                        "Esto es un perro", 
                        margin="0 auto",
                        font_size="1.2em",
                        text_align="center",
                    )
                ),
                rx.audio(
                    url=AppState.sound_url,
                    autoplay=True,
                    controls=True,  # Oculta los controles
                ),
                spacing="0.2em",
                align_items="center",
                justify_content="center",
            ),
            rx.text(    
                "Por favor, sube una imagen para obtener un resultado.",
                text_align="center",  # Centrar texto inicial
                margin_top="1em",
            ),
        ),
        style={
            "margin": "0",
            "padding": "0",
            "height": "auto",
            "min-height": "auto",
        },
    )
    return box
