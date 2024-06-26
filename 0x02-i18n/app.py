#!/usr/bin/env python3
"""
A Flask app with Babel setup for internationalization, locale detection,
template parametrization, forced locale via URL parameter, and mock login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
from datetime import datetime
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> dict:
    """
    Retrieves a user dictionary based on the login_as parameter.

    Returns:
        dict: User dictionary or None if user ID is not found or not provided.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Function to be executed before all other functions.
    Sets the user in the global context if logged in.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages or use the locale
    from the URL parameters if provided and valid.

    Returns:
        str: Best match language code or the forced locale.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best match for the user's timezone or use the timezone from
    the URL parameters if provided and valid.

    Returns:
        str: Best match timezone or the forced timezone.
    """
    timezone = request.args.get('timezone')
    if timezone:
        return timezone
    if g.user and g.user['timezone']:
        return g.user['timezone']
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    current_time = format_datetime(datetime.now(pytz.timezone(get_timezone())))
    return render_template('5-index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
