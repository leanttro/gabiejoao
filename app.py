from flask import Flask, render_template

# Configura para buscar o template na pasta raiz
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)