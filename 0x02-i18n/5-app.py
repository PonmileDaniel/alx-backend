#!/usr/bin/env python3
"""
Get locale form request
"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Config Class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieve user based on the user id
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Stores this data in g.user
    """

    users = get_user()
    g.user = users


@babel.localeselector
def get_locale() -> str:
    """Get the locale for the web page.

    Returns:
        str: The best match
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """Get the locale for the web page.

    Returns:
        html: homepage
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
