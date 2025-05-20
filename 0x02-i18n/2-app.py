#!/usr/bin/env python3
"""Flask app with Babel and locale selection for ALX i18n project.
This app configures Babel and selects locale from request headers.
"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """Select the best match language from the request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the index page with a welcome message."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
