#!/usr/bin/python3
"""
    Starts a Flask web application
                                    """
from flask import Flask


# Creating the Flask instance
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_display():
    """
        Displays “Hello HBNB!”
                                """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb_root():
    """
        Displays "HBNB"
                        """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
        Displays C followed by input
                                    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'})
def display_Python(text):
    """
        Displays Python followed by input
                                        """
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
