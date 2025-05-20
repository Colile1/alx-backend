#!/usr/bin/env python3
"""Basic Flask app for ALX i18n project.
This app serves a single route with a welcome message.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Render the index page with a welcome message."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
