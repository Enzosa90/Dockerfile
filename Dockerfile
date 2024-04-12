FROM python:3.9-slim

# Instalando Flask
RUN pip install Flask

# Copiando o código para o contêiner
COPY . /app
WORKDIR /app

# Expondo a porta 8000
EXPOSE 8000

# Comando para executar o servidor Flask
CMD ["python", "main.py"]
