#!/usr/bin/env python3
"""Flask app with user locale support."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict, Any

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict[str, Any]]:
    """Retrieve a user dictionary based on the login_as parameter."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Set the user in the global context before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages.
    Priority: URL param > user setting > request header > default
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return (request.accept_languages.best_match(app.config['LANGUAGES'])
            or app.config['BABEL_DEFAULT_LOCALE'])


@app.route('/')
def index() -> str:
    """Render the index page."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
