#!/usr/bin/env python3
"""A basic flask app that serves a welcome message """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    '''Default'''
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
