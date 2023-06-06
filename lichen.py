import random
import json


def simulate_lishai(rows, cols, intervals):
    # Создаем сетку размером rows x cols и заполняем ее здоровыми клетками
    grid = [['healthy' for _ in range(cols)] for _ in range(rows)]

    # Создаем двумерный массив счетчиков времени
    time_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Находим центральную клетку
    center_row = rows // 2
    center_col = cols // 2

    # Заражаем центральную клетку
    grid[center_row][center_col] = 'infected'

    result = []

    # Добавляем начальное состояние сетки в результат
    result.append(grid.copy())

    # Проходим по заданному количеству интервалов времени
    for _ in range(intervals):
        # Создаем новую копию сетки на текущем интервале времени
        current_grid = [row.copy() for row in grid]

        # Проходим по каждой клетке в сетке
        for row in range(rows):
            for col in range(cols):
                # Если клетка заражена
                if grid[row][col] == 'infected':
                    # Заражаем любую здоровую соседнюю клетку
                    neighbors = get_neighbors(row, col, rows, cols)
                    for neighbor_row, neighbor_col in neighbors:
                        if current_grid[neighbor_row][neighbor_col] == 'healthy' and random.random() < 0.5:
                            current_grid[neighbor_row][neighbor_col] = 'infected'
                            time_grid[neighbor_row][neighbor_col] = 1
                            break
                    # Увеличиваем счетчик времени для данной клетки
                    time_grid[row][col] += 1

                    # Если счетчик времени достиг 6, клетка становится иммунной
                    if time_grid[row][col] == 6:
                        current_grid[row][col] = 'immune'
                # Если клетка имеет иммунитет
                elif grid[row][col] == 'immune':
                    # Уменьшаем счетчик времени для данной клетки
                    time_grid[row][col] += 1

                    # Если счетчик времени достиг 8, клетка становится здоровой
                    if time_grid[row][col] == 8:
                        current_grid[row][col] = 'healthy'
                        time_grid[row][col] = 0

        # Добавляем текущую копию сетки в результат
        result.append(current_grid)

        # Обновляем сетку для следующего интервала времени
        grid = current_grid

    return {'grid': result}


def get_neighbors(row, col, rows, cols):
    # Возвращает список соседних клеток для заданной клетки
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < cols - 1:
        neighbors.append((row, col + 1))
    return neighbors


