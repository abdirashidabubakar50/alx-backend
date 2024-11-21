#!/usr/bin/env python3
""" A basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configuration for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = ["en"]
    BABEL_DEFAULT_TIMEZONE = "UTC"


# initialze the Flask app
app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """ Index route """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
