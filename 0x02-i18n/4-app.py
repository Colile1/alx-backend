#!/usr/bin/env python3
"""Flask app with Babel and URL locale override for ALX i18n project.
This app allows forcing the locale via a URL parameter.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    """Select the best match language from the URL, then request headers."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the index page with translated messages."""
    return render_template('4-index.html', get_locale=get_locale)


if __name__ == '__main__':
    app.run()
