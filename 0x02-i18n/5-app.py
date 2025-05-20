#!/usr/bin/env python3
"""
Flask app with Babel, user mock login, and personalized greetings for ALX
i18n project.
This app allows user selection via URL and displays personalized or default
greetings.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict


class Config:
    """
    Configuration for Babel with supported languages, default locale, and
    timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Optional[Dict]:
    """Retrieve a user dictionary based on the login_as URL parameter."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Set g.user to the current user if logged in, else None."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Select the best match language from the request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the index page with translated messages and user greeting."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
