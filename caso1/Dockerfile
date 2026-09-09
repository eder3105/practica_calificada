# Imagen base - Python oficial
FROM python:3.11-slim

# Metadata
LABEL maintainer="tu-email@ejemplo.com"
LABEL description="Descargador de videos de redes sociales con yt-dlp"

# Establecer directorio de trabajo
WORKDIR /app

# Instalar ffmpeg (necesario para que yt-dlp una audio/video en algunas plataformas)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py .

# Exponer el puerto
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]