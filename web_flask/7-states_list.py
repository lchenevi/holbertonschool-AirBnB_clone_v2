#!/usr/bin/python3
"""Module for the different pages with Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """Close storage"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """List all states"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
