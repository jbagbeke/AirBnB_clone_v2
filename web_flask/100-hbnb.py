#!/usr/bin/python3
"""
    Starts a Flask web application
                                    """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity

# Creating the Flask instance
app = Flask(__name__)


@app.teardown_appcontext
def hbnb_close(self):
    """
        Closes current session with the app/database
                                            """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_app():
    """
        Displays custom information bases on object info
                                                        """
    states = storage.all(State)
    hbnb_places = storage.all(Place)
    place_amenity = storage.all(Amenity)

    return render_template('100-hbnb.html',
                           states=states.values(),
                           hbnb_places=hbnb_places.values(),
                           place_amenity=place_amenity.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
