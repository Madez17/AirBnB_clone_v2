#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    dict_states = {}
    states_dic = storage.all(State)
    for key, value in states_dic.items():
        dict_states[value.id] = value.name
    return render_template('7-states_list.html', state=dict_states)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
