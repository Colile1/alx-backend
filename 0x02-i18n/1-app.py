#!/usr/bin/env python3
"""
Flask app with Babel setup for ALX i18n project.
This app configures Babel for English and French support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration for Babel with supported languages, default locale, and
    timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Render the index page with a welcome message."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
