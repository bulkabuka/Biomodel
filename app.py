import os.path

from bottle import route, run, template, request, response, static_file, post, get, abort
import numpy as np
import json
from lichen import simulate_lishai
from life import *
from wolf import *

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


@route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            if message == "start":
                sim = Simulation()  # Initialize your simulation here
                sim.setup()
                for i in range(sim.iterations):
                    sim.run()
                    wsock.send(json.dumps(sim.matrix.tolist()))  # Send the matrix to the front-end
        except WebSocketError:
            break


# инициализация поля случано выбранными живыми/неживыми клетками
@route('/start', method='POST')
def start():
    global game_state
    rows = int(request.forms.get('rows'))
    cols = int(request.forms.get('cols'))
    game_state = np.random.choice([0, 1], size=(rows, cols))
    return {'status': 'Game started', 'grid': game_state.tolist()}


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


# интерпретация данных в JSON для анализа на сервере
@route('/next')
def next_gen():
    global game_state
    game_state = next_generation(game_state)
    response.content_type = 'application/json'
    return json.dumps({'grid': game_state.tolist()})


# сохранение следующей итерации в файл JSON
@post('/save-life')
def save_life():
    global game_state
    game_state = next_generation(game_state)
    response.content_type = 'application/json'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('output.json', 'w') as file:
        json.dump({'grid': game_state.tolist()}, file)


run(host='localhost', port=8080)
