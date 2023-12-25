#!/usr/bin/python3
"""define route module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardow(self):
    """"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
