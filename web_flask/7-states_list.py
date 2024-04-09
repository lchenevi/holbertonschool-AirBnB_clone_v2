#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

# Create a Flask application instance
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns the list of all States in the database."""
    states = {}
    for state in sorted(storage.all("State").values(), key=lambda s: s.name):
        states[state.id] = state.name
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close(self):
    """Closes the database session."""
    storage.close()


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
