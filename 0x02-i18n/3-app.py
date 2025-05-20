#!/usr/bin/env python3
"""
Flask app with Babel and template parametrization for ALX i18n project.
This app configures Babel and uses gettext for translations in templates.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


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
    """Select the best match language from the URL, user settings, or request
    headers.
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # 2. Locale from user settings (mocked user)
    user = getattr(g, 'user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Select the best match timezone from the URL, user settings, or default
    to UTC.
    """
    # 1. Timezone from URL parameters
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            pytz.timezone(tz_param)
            return tz_param
        except UnknownTimeZoneError:
            pass
    # 2. Timezone from user settings (mocked user)
    user = getattr(g, 'user', None)
    if user:
        user_tz = user.get('timezone')
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass
    # 3. Default to UTC
    return 'UTC'


@app.route('/')
def index() -> str:
    """Render the index page with translated messages and current time.
    """
    current_time = format_datetime(datetime.now(pytz.timezone(get_timezone())))
    return render_template('3-index.html', current_time=current_time, get_locale=get_locale)


if __name__ == '__main__':
    app.run()
