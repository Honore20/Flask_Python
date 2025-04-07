from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    somme = 0
    for i in range(1, valeur + 1):
        if i % 11 == 0:
            continue
        if i % 5 == 0 or i % 7 == 0:
            somme += i
        if somme > 5000:
            break
    
    return f'<pre>Somme finale: {somme}</pre>'

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)




