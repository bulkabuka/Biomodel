import numpy as np


# инициализация поля случано выбранными живыми/неживыми клетками
def start(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))


# метод для генерации следующего поколения, возвращает новую матрицу
def next_generation(game_state):
    # инициализация и заполнение новой матрицы нулями
    rows, cols = game_state.shape
    new_state = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            state = game_state[i, j]
            # вычисление суммы всех соседей для подсчета их количества
            neighbours = np.sum(game_state[max(0, i - 1):min(rows, i + 2), max(0, j - 1):min(cols, j + 2)]) - state

            # проверка если клетка уже живая
            if state:
                # смерть от перенаселения или недостатка соседей
                if neighbours < 2 or neighbours > 3:
                    new_state[i, j] = 0
                else:
                    # иначе остается в живых
                    new_state[i, j] = 1
            # три живых соседа - жизнь для мертвой клетки
            elif neighbours == 3:
                new_state[i, j] = 1

    return new_state
