#!/usr/bin/env python3
"""
A Flask app with Babel setup for internationalization and locale detection.
"""


from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.

    Returns:
        str: Best match language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
