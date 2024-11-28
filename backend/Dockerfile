# Usa la imagen oficial de TensorFlow para GPU con Python 3.9
FROM tensorflow/tensorflow:2.10.0-gpu

# Instala pip y actualiza a la última versión
RUN pip install --no-cache-dir --upgrade pip

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Permite el crecimiento dinámico de memoria de la GPU
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

# Selecciona la GPU (0 en este caso)
ENV CUDA_VISIBLE_DEVICES=0

# Copia el código fuente al contenedor
COPY . .

# Expone el puerto 8000 para FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
