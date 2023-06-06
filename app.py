import logging
import traceback
from datetime import *
import os.path

from bottle import route, run, template, request, response, static_file, post, get, abort
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


# сохранение следующей итерации в файл JSON
@post('/save-life')
def save_life():
    global game_state
    game_state = next_generation(game_state)
    response.content_type = 'application/json'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('output.txt', 'a') as file:
        json.dump({'grid': game_state.tolist()}, file)
        file.write(" " + str(datetime.now()))


@route('/simulation',method="post")
def simulation():
    simulate_game()

    return simulate_game()


@get('/print_wolf')
def print_wolf():
    try:
        matrices = []
        for _ in range(1):
            result = simulate_game()
            matrices.append(result.grid)

        result_string = ""
        for matrix in matrices:
            for row in matrix:
                result_string += ' '.join(map(str, row))
                result_string += '\n'
            result_string += '\n'

        print(result_string)  # Print the result_string to the console

        response.content_type = 'application/json'
        return json.dumps({'success': result_string})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.error(traceback.format_exc())
        return json.dumps({'error': str(e)})


run(host='localhost', port=8080)
