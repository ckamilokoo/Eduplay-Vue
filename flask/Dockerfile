# Derivar la imagen base
FROM python:3.10-slim-bullseye

# Crear un entorno virtual
RUN python -m venv /opt/env

# Activar el entorno virtual
ENV PATH="/opt/env/bin:$PATH"

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/app/src

# Copiar los archivos necesarios al contenedor
COPY requirements.txt ./
COPY app ./app  
COPY main.py ./  

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "-m", "main"]

