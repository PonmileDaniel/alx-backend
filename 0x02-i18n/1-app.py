#!/usr/bin/env
"""Get locale from request"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.routes("/")
def index():
    """Default routes"""
    return render_template("1-index.html")


if __name___ == "__main__":
    app.run()
