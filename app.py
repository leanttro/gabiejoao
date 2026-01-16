from flask import Flask, render_template, send_from_directory
import os

# Configura o Flask
app = Flask(__name__, template_folder='.')

# Rota principal (o site)
@app.route('/')
def home():
    return render_template('index.html')

# Rota genérica para servir qualquer arquivo estático (imagens, css, js)
# que esteja na raiz da pasta junto com o app.py
@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # Roda o servidor acessível na rede (host 0.0.0.0) na porta 80
    app.run(host='0.0.0.0', port=80)