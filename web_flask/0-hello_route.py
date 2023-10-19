#!/usr/bin/python3
"""
Created by damassoh Japhet
"""

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', methods=['GET'], strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
