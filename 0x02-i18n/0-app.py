#!/usr/bin/env python3
"""
A basic Flask app to demonstrate a simple web page with a welcome message.
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
