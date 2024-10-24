import reflex as rx
from frontend.state.state import AppState

def upload_button():
    """Crea un botón de subida de imagen."""
    return rx.upload(
        rx.vstack(
            rx.button("Seleccionar imagen"),
            rx.text("Arrastra y suelta aquí o haz clic para seleccionar"),
        ),
        id="upload_image",
        on_drop=AppState.handle_upload(rx.upload_files(upload_id="upload_image")),
        border="1px dotted #707070",
        padding="2em",
        accept={"image/jpeg": [".jpg", ".jpeg"], "image/png": [".png"]},
        max_files=1,
    )
