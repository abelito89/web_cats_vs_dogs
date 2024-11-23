import reflex as rx
from frontend.state.state import AppState

def image_display() -> rx.Component:
    box = rx.box(
        rx.cond(
            AppState.img != "",  # Mostrar la imagen apenas esté disponible
            rx.image(
                src=AppState.img,
                width="300px",  # Define un ancho fijo para todas las imágenes
                height="auto",  # Ajusta la altura automáticamente para mantener la proporción
                margin_top="1em"
            )
        )
    )
    return box