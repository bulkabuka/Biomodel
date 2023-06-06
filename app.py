from bottle import route, run, template, request, response, static_file, post, get
import numpy as np
import json
import life
from lichen import simulate_lishai
from life import *
from datetime import *

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


# инициализация поля случано выбранными живыми/неживыми клетками
@route('/start', method='POST')
def start():
    global game_state
    rows = int(request.forms.get('rows'))
    cols = int(request.forms.get('cols'))
    game_state = np.random.choice([0, 1], size=(rows, cols))
    return {'status': 'Game started', 'grid': game_state.tolist()}


from datetime import datetime
import json
from bottle import request, response, route


#запуск симуляции


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
    print(intervals)

    result = simulate_lishai(rows, cols, intervals)

    with open('last_matrix.json', 'a') as file:
        file.write(json.dumps(result))
        now = datetime.now()
        file.write(str(now) + '\n')

    response.content_type = 'application/json'
    return result



# интерпретация данных в JSON для анализа на сервере
@route('/next')
def next_gen():
    global game_state
    game_state = next_generation(game_state)
    response.content_type = 'application/json'
    return json.dumps({'grid': game_state.tolist()})




run(host='localhost', port=8080)
