from flask import Flask

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(nombre) for nombre in liste_nombres]
    valeur_max = liste_nombres[0]
    for nombre in liste_nombres:
        if nombre > valeur_max:
            valeur_max=nombre
    return str(valeur_max)

if __name__ == '__main__':
    app.run(host='0.0.0.0')





