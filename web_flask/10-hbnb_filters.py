#!/usr/bin/python3
"""define route module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardow(self):
    """"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    return render_template('10-hbnb_filters.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
