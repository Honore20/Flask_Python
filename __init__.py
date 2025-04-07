from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    sequence = [a, b]
    for _ in range(2, valeur):
        a, b = b, a + b
        sequence.append(b)
    
    fibonacci = '<pre>' + ', '.join(map(str, sequence)) + '</pre>'
    return fibonacci

if __name__ == "__main__":
    app.run(debug=True)



