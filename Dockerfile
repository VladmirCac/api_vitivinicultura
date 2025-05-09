FROM python:3.13-slim

# Instalar dependências de sistema (ex: build-essential, lxml etc.)
RUN apt-get update && apt-get install -y build-essential libxml2-dev libxslt1-dev && apt-get clean

# Diretório da aplicação
WORKDIR /app

# Copiar os arquivos para dentro do container
COPY . .

# Instalar o poetry
RUN pip install poetry

# Instalar dependências com poetry
RUN poetry install --no-root

# Expor a porta padrão
EXPOSE 8000

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Comando para iniciar a aplicação
CMD ["bash", "-c", "poetry run alembic upgrade head && poetry run uvicorn api_vitivinicultura.main:app --host=0.0.0.0 --port=8000"]