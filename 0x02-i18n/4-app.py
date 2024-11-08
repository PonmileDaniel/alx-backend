#!/usr/bin/env python3
"""
Get locale form request
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


# Instantiate the app
app = Flask(__name__)


# wrap the app with babel
babel = Babel(app)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']



@babel.localeselector
def get_locale() -> str:
    """ Check locale parameter """
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    """ Get the best match """
    return request.accept_languages.best_match(app.config["BABEL_SUPPORTED_LOCALES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """ Default route """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
