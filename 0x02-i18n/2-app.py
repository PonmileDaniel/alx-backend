#!/usr/bin/env python3
"""Get locale form request"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str: 
    """Get the best match"""
    return request.accept_language.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """Default route"""
    return render_template("2-index.html")

if __name__ == "__main__":
    app.run()
