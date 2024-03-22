"""
Import flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """created my first route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """added a new route that display something else"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_way(text):
    """
    display C then followed by any value appeneded to it
    """
    return 'C ' + text.replace('_', ' ')
