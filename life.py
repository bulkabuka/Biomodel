import numpy as np


def start(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))


def next_generation(game_state):
    rows, cols = game_state.shape
    new_state = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            state = game_state[i, j]
            neighbours = np.sum(game_state[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - state

            if state:
                if neighbours < 2 or neighbours > 3:
                    new_state[i, j] = 0
                else:
                    new_state[i, j] = 1
            elif neighbours == 3:
                new_state[i, j] = 1

    return new_state
