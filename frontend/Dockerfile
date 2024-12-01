# Usa una imagen base de Python 3.11.4
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instalar herramientas esenciales
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de dependencias
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .

# Expone el puerto en el que Reflex sirve la app (predeterminado: 3000, modificado por 50001) y el puerto usando para la comunicacion con el backend de reflex (no confundir con el backend de fastapi)
EXPOSE 50001 51001

# Comando para iniciar Reflex en modo producción.
# Importante especificar --backend-host como 0.0.0.0 para que Reflex pueda comunicarse con el backend de FastAPI (o su propio backend, la verdad no estoy seguro)
CMD ["reflex", "run", "--env", "prod", "--backend-host", "0.0.0.0"]