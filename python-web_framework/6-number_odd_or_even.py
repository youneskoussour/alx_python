
"""
Flask Application

This script defines a Flask web application with various routes.

Routes:
- /: display "Hello HBNB!"
- /hbnb: display "HBNB"
- /c/<text>: display "C ", followed by the value of the text variable (replace underscore _ symbols with a space)
- /python/<text>: display "Python ", followed by the value of the text variable (replace underscore _ symbols with a space)
- /number/<n>: display "n is a number" only if n is an integer
- /number_template/<n>: display a HTML page only if n is an integer with H1 tag: "Number: n" inside the tag BODY
- /number_odd_or_even/<n>: display a HTML page only if n is an integer with H1 tag: "Number: n is even|odd" inside the tag BODY

The application listens on 0.0.0.0, port 5000.

Usage:
    Run the script, and the Flask application will start.

"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
