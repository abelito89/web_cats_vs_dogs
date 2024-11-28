# Usa una imagen base de Python 3.11.4
FROM python:3.11-slim

# Instalar herramientas esenciales
RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Instala pip y actualiza a la última versión
RUN pip install --no-cache-dir --upgrade pip

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .

# Inicializa Reflex y prepara el entorno
RUN reflex init

# Expone el puerto en el que Reflex sirve la app (predeterminado: 3000)
EXPOSE 3000

# Comando para iniciar Reflex en modo producción
CMD ["reflex", "run", "--env", "prod"]