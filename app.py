from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

# Serve imagens (hero1.png, flor1.png) e arquivos estáticos
@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)