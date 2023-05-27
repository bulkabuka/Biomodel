import json
import numpy as np
from bottle import request, response

game_state = None


def next_generation(state):
    new_state = state.copy()
    rows, cols = state.shape
    for i in range(rows):
        for j in range(cols):
            total = np.sum(state[max(0, i - 1):min(rows, i + 2), max(0, j - 1):min(cols, j + 2)]) - state[i, j]
            if state[i, j]:
                if total < 2 or total > 3:
                    new_state[i, j] = 0
            elif total == 3:
                new_state[i, j] = 1
    response.content_type = 'application/json'
    return json.dumps({'grid': new_state.tolist()})


def start():
    global game_state
    rows = int(request.forms.get('rows'))
    cols = int(request.forms.get('cols'))
    game_state = np.random.choice([0, 1], size=(rows, cols))
    return {'status': 'Game started', 'grid': game_state.tolist()}
