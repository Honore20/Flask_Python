from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    pyramide = '<pre>'
    for i in range(1, valeur + 1):
        espaces = ' ' * (valeur - i)
        chiffres = ''.join(str(j) for j in range(1, i + 1)) + ''.join(str(j) for j in range(i - 1, 0, -1))
        pyramide += espaces + chiffres + '\n'
    pyramide += '</pre>'
    return pyramide

if __name__ == "__main__":
    app.run(debug=True)


