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
    """display C then followed by any value appeneded to it"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    declare two route that has a default string
    but can change when needed
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def int_validator(n):
    """
    detects if the entered argument is a number.
    if not return a error page
    """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)