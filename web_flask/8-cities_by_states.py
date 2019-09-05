#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models import State
from models import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    dict_states = {}
    dict_cities = {}

    states_dic = storage.all(State)
    for key, value in states_dic.items():
        dict_states[value.id] = value.name

    for iter in states_dic:
        dict_cities[states_dic[iter].id] = states_dic[iter].cities


    return render_template('8-cities_by_states.html', state=dict_states, city=dict_cities)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
