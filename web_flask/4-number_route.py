#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return "C {}". format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    return "Python {}".format(text.replace('_',' '))

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n=None):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
