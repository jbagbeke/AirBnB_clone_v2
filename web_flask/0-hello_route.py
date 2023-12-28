#!/usr/bin/python3
"""
    Starts a Flask web application
                                    """
from flask import Flask


# Creating the Flask instance
app = Flask(__name__)


@app.route('/')
def hbnb_display():
    """
        Displays “Hello HBNB!”
                                """
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
