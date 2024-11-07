#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Default routes"""
    return render_template("1-index.html")


if __name___ == "__main__":
    app.run()
