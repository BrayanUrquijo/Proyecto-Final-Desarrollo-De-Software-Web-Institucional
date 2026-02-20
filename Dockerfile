# Usar Python 3.12 como base
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY requirements_web.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements_web.txt

# Copiar todos los archivos del proyecto
COPY . .

# Exponer puerto 5000 para Flask
EXPOSE 5000

# Comando para ejecutar la aplicacion
CMD ["python", "app.py"]
