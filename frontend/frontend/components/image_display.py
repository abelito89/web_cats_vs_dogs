import reflex as rx
from frontend.state.state import AppState

def image_display() -> rx.Component:
    """
    Muestra la imagen subida por el usuario.

    Esta función crea un componente de Reflex que muestra la imagen subida por el usuario
    tan pronto como esté disponible. La imagen se ajusta automáticamente para mantener
    la proporción y se muestra con un margen superior.

    Retorna:
    --------
    rx.Component
        Un componente de Reflex que representa la visualización de la imagen subida.
    """
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