import unittest
import numpy as np
from life import *


class TestGameOfLife(unittest.TestCase):
    def test_start(self):
        game_state = start(5, 5)
        self.assertEqual(game_state.shape, (5, 5))
        self.assertTrue(np.all(np.logical_or(game_state == 0, game_state == 1)))

    def test_next_generation(self):
        # Паттерн осциллятор
        initial_state = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        next_state = next_generation(initial_state)
        expected_state = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.assertTrue(np.array_equal(next_state, expected_state))

        # Другая итерация
        next_state = next_generation(next_state)
        self.assertTrue(np.array_equal(next_state, initial_state))

    # Тест на невалидные и краевые значения для инициализации
    def test_invalid_start(self):
        with self.assertRaises(ValueError):
            start(-1, 5)
        with self.assertRaises(ValueError):
            start(5, 0)

    # Тест на стабильное состояние
    def test_run_still_life(self):
        initial_state = np.array([
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ])
        next_state = next_generation(initial_state)
        self.assertTrue(np.array_equal(next_state, initial_state))

    # Тест на паттерн Глайдер
    def test_run_glider(self):
        initial_state = np.zeros((5, 5))
        initial_state[0, 1] = initial_state[1, 2] = initial_state[2, 0] = initial_state[2, 1] = initial_state[2, 2] = 1
        next_state = next_generation(initial_state)

        expected_state = np.zeros((5, 5))
        expected_state[1, 0] = expected_state[1, 2] = expected_state[2, 2] = expected_state[2, 1] = expected_state[
            3, 1] = 1
        self.assertTrue(np.array_equal(next_state, expected_state))


if __name__ == "__main__":
    unittest.main()
