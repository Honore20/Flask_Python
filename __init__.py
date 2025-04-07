from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    if valeur < 2:
        return '<pre>La valeur doit être supérieure ou égale à 2.</pre>'
    
    sequence = [0, 1]
    for _ in range(2, valeur):
        sequence.append(sequence[-1] + sequence[-2])
    
    fibonacci = '<pre>' + ', '.join(map(str, sequence)) + '</pre>'
    return fibonacci

if __name__ == "__main__":
    app.run(debug=True)



