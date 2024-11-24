import reflex as rx
from frontend.state.state import AppState

def upload_button():
    """
    Crea un botón de subida de imagen.

    Esta función crea un componente de Reflex que permite al usuario subir una imagen.
    El botón permite seleccionar una imagen desde el dispositivo o arrastrar y soltar
    la imagen en el área designada. Se aceptan archivos JPEG y PNG.

    Retorna:
    --------
    rx.Component
        Un componente de Reflex que representa el botón de subida de imagen.
    """
    return rx.upload(
        rx.vstack(
            rx.button("Seleccionar imagen"),
            rx.text("Arrastra y suelta aquí o haz clic para seleccionar"),
            align="center"
        ),
        id="upload_image",
        on_drop=AppState.handle_upload(rx.upload_files(upload_id="upload_image")),
        border="1px dotted #707070",
        padding="2em",
        margin="2em",
        accept={"image/jpeg": [".jpg", ".jpeg"], "image/png": [".png"]},
        max_files=1,
    )
