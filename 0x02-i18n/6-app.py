#!/usr/bin/env python3
"""
A Flask app with Babel setup for internationalization, locale detection,
template parametrization, forced locale via URL parameter, and mock login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


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
    Determine the best match with our supported languages based on the
    following priority: URL parameter, user settings, request header,
    and default locale.

    Returns:
        str: Best match language code.
    """
    # Locale from URL parameter
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    # Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
