# Usar una imagen base de Python oficial
FROM python:3.11-slim-bookworm

# Evitar que Python genere archivos .pyc y habilitar modo sin buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 y PostGIS (opcional)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn daphne

# Copiar el proyecto
COPY . /app/

# Crear carpeta para archivos estáticos y media
RUN mkdir -p /app/staticfiles /app/media

# Exponer el puerto
EXPOSE 8000

# Comando para iniciar la aplicación usando Daphne (mejor para WebSockets/Channels)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]
