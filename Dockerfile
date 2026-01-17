# Dockerfile
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copiar código
COPY ./app /app
WORKDIR /app

# Instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.wsgi:app", "--workers", "4", "--log-level", "info"]



