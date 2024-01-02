#!/usr/bin/python3
"""
    Starts  a Flask web application
                                    """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

# Creating the Flask instance
app = Flask(__name__)


@app.teardown_appcontext
def hbnb_close(self):
    """
        Closes current session with the database
                                                """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
        Renders 6-index template from AirBnB_clone project
                                                            """
    states = storage.all(State)
    place_amenity = storage.all(Amenity)

    return render_template('10-hbnb_filters.html',
                           states=states.values(),
                           place_amenity=place_amenity.values())


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
