#!/usr/bin/env python3
"""
Get locale form request
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Config Class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate the app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

# wrap the app with babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get the locale for the web page.

    Returns:
        str: The best matc """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """ Default route for the html page """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
