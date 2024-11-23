import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Neural network",
            font_size="1em",  # Tamaño de fuente ajustado para destacar el título
            font_weight="bold",  # Hace el texto más prominente
            color="white",  # Contraste adecuado con el fondo azul
        ),
        background_color="blue",  # Fondo azul claro para toda la barra
        padding="1em",  # Espaciado interno de la barra
        box_shadow="0px 2px 5px rgba(0, 0, 0, 0.1)",  # Añade una sombra para dar profundidad
        justify="center"
    )