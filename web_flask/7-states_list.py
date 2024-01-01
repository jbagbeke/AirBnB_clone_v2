#!/usr/bin/python3
"""
    Starts a Flask web application
                                    """
from models import storage
from flask import Flask, render_template
from models.state import State


# Creating the Flask instance
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hbnb_states():
    """
        Display a HTML page: (inside the tag BODY)
                                                    """
    states = storage.all(State)
    states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def hbnb_teardown(self):
    """
        Closes current session with the database
                                                """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
