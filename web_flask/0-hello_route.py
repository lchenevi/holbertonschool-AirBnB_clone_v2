#!/usr/bin/python3
"""
Retourn html page


"""

from flask import Flask

'''Créer une instance de l'application Flask'''
app = Flask(__name__)

# Définit une route '/' pour l'URL racine

@app.route("/", strict_slashes=False)
def hello_world():
    '''Fonction de vue qui renvoie "Hello HBNB!"'''
    return "Hello HBNB!"

# si ce script est exécuté en tant que programme principal
if __name__ == '__main__':
    '''Lance l'application Flask'''
    # host='0.0.0.0' permet à l'application d'écouter sur toutes
    # les interfaces réseau
    # port=5000 spécifie le port sur lequel l'application va écouter'''
    app.run(host='0.0.0.0', port=5000)
