# 1. Base Image: Usa una imagen oficial de Python como base para el backend de Django.
# (Se recomienda usar una versión específica y ligera, como 3.11-slim)
FROM python:3.11-slim

# 2. Environment: Establece variables de entorno que Docker puede usar.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Working Directory: Define el directorio de trabajo dentro del contenedor.
# Aquí es donde se copiará y ejecutará la aplicación.
WORKDIR /app

# 4. Dependencies: Copia el archivo de dependencias (requirements.txt) y las instala.
# Esto es más eficiente, ya que solo reinstala las dependencias si este archivo cambia.
# Esto asegura que las "Dependencias explícitas y aisladas" [cite: 94, 95] se cumplan.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Application Code: Copia el resto del código del backend al contenedor.
# Esta es la etapa de 'Build' de su ciclo.
COPY . /app/

# 6. Port: Especifica el puerto en el que correrá la aplicación.
# En este caso, el puerto por defecto de Django.
EXPOSE 8000