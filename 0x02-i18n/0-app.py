#!/usr/bin/env python3
from flask import Flask, render_template

# initialze the Flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
