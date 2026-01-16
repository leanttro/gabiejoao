# Imagem leve do Python
FROM python:3.9-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 80
EXPOSE 80

# Comando para rodar com Gunicorn (Servidor de produção)
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]