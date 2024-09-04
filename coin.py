from flask import Flask
import random

app = Flask(__name__)

@app.route('/lanzar_moneda')
def lanzar_moneda():
    resultado = random.choice(['Cara', 'Cruz'])
    return f'El resultado es: {resultado}'

if __name__ == '__main__':
    app.run(debug=True)
