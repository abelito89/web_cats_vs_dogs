import reflex as rx

config = rx.Config(
    app_name="frontend",
    frontend_port=3000,
    backend_port=8000,
    asset_dir="frontend/assets",  # Cambia según tu estructura
)
print(f"Serving static files from: {config.asset_dir}")