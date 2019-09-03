#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Fucn index"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Func hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Func c"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """Func python"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number(n):
    """Func integer """
    return '{} is a number'.format(n)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
