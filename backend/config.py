from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Cambia esto por el puerto que usa tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)