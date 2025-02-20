#!/usr/bin/python3
"""
    Starts a Flask web application
                                    """
from models import storage
from models.state import State
from flask import Flask, render_template


# Creating the Flask instance
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def hbnb_state():
    """
        Displays all states
                            """
    states = storage.all(State)

    return render_template('9-states.html', states=states.values())


@app.teardown_appcontext
def close(self):
    """
        Method to close the current session with the database
                                    """
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
def hbnb_state_id(id):
    """
        Displays the state with the specified id
                                                """
    states = storage.all(State)

    return render_template('9-states.html', states=states.values(), id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
