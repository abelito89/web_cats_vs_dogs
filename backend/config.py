from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    """
    Configura el middleware CORS para la aplicación FastAPI.

    Esta función añade el middleware CORS (Cross-Origin Resource Sharing) a la aplicación FastAPI,
    permitiendo solicitudes desde el origen especificado. Esto es útil para permitir que el frontend
    se comunique con el backend sin problemas de CORS.

    Parámetros:
    -----------
    app : FastAPI
        La instancia de la aplicación FastAPI a la que se añadirá el middleware CORS.

    Configuración:
    --------------
    allow_origins : list
        Lista de orígenes permitidos para las solicitudes CORS.
    allow_credentials : bool
        Permitir el uso de credenciales en las solicitudes CORS.
    allow_methods : list
        Lista de métodos HTTP permitidos en las solicitudes CORS.
    allow_headers : list
        Lista de encabezados permitidos en las solicitudes CORS.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # Cambia esto por el puerto que usa tu frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
