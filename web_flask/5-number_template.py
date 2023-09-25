#!/usr/bin/python3
"""
Created by damassoh Japhet
"""

from flask import Flask
from flask import render_template
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

@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
