# 0x02-i18n

This directory contains tasks related to internationalization (i18n) in Flask applications. The tasks demonstrate how to set up and use Flask with Babel for localization, including locale selection, user-based localization, time zone handling, and displaying the current time in the user's locale.

## Tasks

### 0. Basic Flask app
- Implements a simple Flask app with a single route (`/`).
- Renders a template with the title "Welcome to ALX" and header "Hello world".

### 1. Basic Babel setup
- Sets up Babel for the Flask app.
- Configures available languages (`en`, `fr`) and default locale/timezone.

### 2. Get locale from request
- Implements a `get_locale` function to determine the best match for supported languages based on the request.

### 3. Parametrize templates
- Uses `_` or `gettext` to parametrize templates for translations.
- Sets up translation files and compiles them for use.

### 4. Force locale with URL parameter
- Allows forcing a specific locale using a `locale` URL parameter.

### 5. Mock logging in
- Simulates user login with a `login_as` URL parameter.
- Displays user-specific messages based on login status.

### 6. Use user locale
- Updates `get_locale` to prioritize user settings for locale selection (URL param > user setting > request header > default).

### 7. Infer appropriate time zone
- Implements a `get_timezone` function to determine the appropriate time zone based on URL parameters, user settings, or defaults.
- Validates time zones using `pytz`.

### 8. Display the current time (Advanced)
- Displays the current time on the home page in a locale-aware format using Babel.
- Uses the translation key `current_time_is` for both English and French.

## Usage
1. Install Flask, Flask-Babel, and pytz:
   ```bash
   pip install Flask flask-babel pytz
   ```
2. Extract and compile translations:
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   pybabel init -i messages.pot -d translations -l en
   pybabel init -i messages.pot -d translations -l fr
   # Edit translations/en/LC_MESSAGES/messages.po and translations/fr/LC_MESSAGES/messages.po as needed
   pybabel compile -d translations
   ```
3. Run the desired app file (e.g., `python3 app.py`).
4. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Files
- `0-app.py` to `7-app.py`, `app.py`: Flask app files for each task.
- `templates/`: Contains HTML templates for each task.
- `babel.cfg`: Configuration file for Babel.
- `translations/`: Directory for compiled translation files.

---

*This directory is part of the ALX Backend specialization.*