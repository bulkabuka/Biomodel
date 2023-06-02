from bottle import route, run, template, request, response, static_file, post, get
import numpy as np
import json
import life
from lichen import simulate_lishai

game_state = None


@route('/life')
def life():
    return template('life', title='Игра в жизнь')


@route('/')
def index():
    return template('index', title="Главная страница")


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')


@route('/the_spread_of_lichen')
def the_spread_of_lichen():
    return template('the_spread_of_lichen', title="Распространение лишая")


@route('/wolf_island')
def the_spread_of_lichen():
    return template('wolf_island', title="Волчий остров")


@route('/start', method='POST')
def start():
    global game_state
    rows = int(request.forms.get('rows'))
    cols = int(request.forms.get('cols'))
    game_state = np.random.choice([0, 1], size=(rows, cols))
    return {'status': 'Game started', 'grid': game_state.tolist()}


@route('/next')
def next_gen():
    global game_state
    game_state = next_generation(game_state)
    response.content_type = 'application/json'
    return json.dumps({'grid': game_state.tolist()})


def next_generation(state):
    new_state = state.copy()
    rows, cols = state.shape
    for i in range(rows):
        for j in range(cols):
            total = np.sum(state[max(0,i-1):min(rows,i+2), max(0,j-1):min(cols,j+2)]) - state[i,j]
            if state[i,j]:
                if total < 2 or total > 3:
                    new_state[i,j] = 0
            elif total == 3:
                new_state[i,j] = 1
    return new_state


@route("/simulate", method="post")
def simulate():
    data = request.forms
    print(data)
    if data is None or 'rows' not in data or 'cols' not in data or 'intervals' not in data:
        response.content_type = 'application/json'
        return json.dumps({'error': 'Invalid request data'})

    rows = int(data['rows'])
    cols = int(data['cols'])
    intervals = int(data['intervals'])

    result = simulate_lishai(rows, cols, intervals)

    response.content_type = 'application/json'
    return result


run(host='localhost', port=8080)
