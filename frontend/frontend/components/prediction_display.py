import reflex as rx
from frontend.state.state import AppState

def prediction_display() -> rx.Component:
    box = rx.box(
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
    )
    )
    return box