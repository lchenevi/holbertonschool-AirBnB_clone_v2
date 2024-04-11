#!/usr/bin/python3
""" Return html page """
from flask import Flask, render_template

app = Flask(__name__)


# Définit une route '/' pour l'URL racine
@app.route("/", strict_slashes=False)
def hello_world():
    """ Retourne Hello HBNB"""
    return "Hello HBNB!"


# Définit une route pour l'URL '/hbnb'
@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Retourne HBNB"""
    return "HBNB"


# Définit une route pour l'URL '/c/<text>'
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Retourne texte 'C' suivi de la variable <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


# Définit une route pour l'URL '/python/<text>'
@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text='is cool'):
    """ Retourne texte 'Python' suivi de la
    variable <text> ou 'is cool' par défaut"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Retourne "is a number" suivi du nombre n"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Retourne page HTML /templates/5-number.html en remplaçant
    la variable 'number' par la valeur de la variable 'n'"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Retourne page HTML /templates/6-number_odd_or_even.html en remplaçant
    la variable 'number' par la valeur de la variable 'n'
    précisant si le nombre est pair ou impair"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    '''Lance l'application Flask'''
    app.run(host='0.0.0.0', port=5000)
