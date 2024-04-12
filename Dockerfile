# Use a imagem base do Python 3.9 Slim
FROM python:3.9-slim

# Instale as dependências do seu aplicativo
RUN pip install Flask

# Copie o código do seu aplicativo para o contêiner
COPY . /app
WORKDIR /app

# Exponha a porta que seu aplicativo estará ouvindo
EXPOSE 8000

# Comando para iniciar o seu aplicativo quando o contêiner for iniciado
CMD ["python", "main.py"]
