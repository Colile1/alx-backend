#!/usr/bin/env python3
"""
Flask application for Task 3: Parametrize templates.
This module sets up a Flask app with Babel integration,
configures available languages, determines locale from request,
and uses gettext for template parametrization.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask application.
    This class holds configuration variables for the application,
    such as available languages, default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on request.
    Uses the 'Accept-Language' header from the incoming request.
    Returns:
        str: The best matched language code (e.g., 'en', 'fr').
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index page using parametrized templates.
    The title and header are translated using message IDs.
    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
