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


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            state_id = state
    return render_template('9-states.html', id=id, state=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
