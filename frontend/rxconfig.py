import reflex as rx

config = rx.Config(
    app_name="frontend",
    api_url="http://localhost:51001",  # Backend URL con el puerto especificado en el docker-compose
    backend_port=51001,
    frontend_port=3000,  # no confundir este puerto con el 50001 que es el usado por el forntend en el navegador. De eso se encarga docker-compose de mapear 50001 -> 3000
    dev_mode=True,
)
