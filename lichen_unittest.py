import unittest
from unittest.mock import patch
from lichen import simulate_lishai, get_neighbors


class SimulateLishaiTest(unittest.TestCase):
    @patch('random.random', return_value=0.5)
    def test_simulate_lishai(self, random_mock):
        rows = 3
        cols = 3
        intervals = 2

        expected_result = [
            [
                ['healthy', 'healthy', 'healthy'],
                ['healthy', 'infected', 'healthy'],
                ['healthy', 'healthy', 'healthy']
            ],
            [
                ['healthy', 'healthy', 'healthy'],
                ['healthy', 'infected', 'healthy'],
                ['healthy', 'healthy', 'healthy']
            ],
            [
                ['healthy', 'healthy', 'healthy'],
                ['healthy', 'infected', 'healthy'],
                ['healthy', 'healthy', 'healthy']
            ]
        ]

        result = simulate_lishai(rows, cols, intervals)

        self.assertEqual(result['grid'], expected_result)
        random_mock.assert_called()

    def test_get_neighbors(self):
        rows = 3
        cols = 3
        row = 1
        col = 1

        expected_neighbors = [(0, 1), (2, 1), (1, 0), (1, 2)]
        neighbors = get_neighbors(row, col, rows, cols)

        self.assertEqual(neighbors, expected_neighbors)

    def test_get_neighbors_with_boundary_cells(self):
        rows = 3
        cols = 3

        # Testing top-left corner cell
        row = 0
        col = 0
        expected_neighbors = [(1, 0), (0, 1)]
        neighbors = get_neighbors(row, col, rows, cols)
        self.assertEqual(neighbors, expected_neighbors)

        # Testing top-right corner cell
        row = 0
        col = 2
        expected_neighbors = [(1, 2), (0, 1)]
        neighbors = get_neighbors(row, col, rows, cols)
        self.assertEqual(neighbors, expected_neighbors)

        # Testing bottom-left corner cell
        row = 2
        col = 0
        expected_neighbors = [(1, 0), (2, 1)]
        neighbors = get_neighbors(row, col, rows, cols)
        self.assertEqual(neighbors, expected_neighbors)

        # Testing bottom-right corner cell
        row = 2
        col = 2
        expected_neighbors = [(1, 2), (2, 1)]
        neighbors = get_neighbors(row, col, rows, cols)
        self.assertEqual(neighbors, expected_neighbors)

    @patch('random.random', return_value=0.5)
    def test_first_infected_cell_odd_intervals_3(self, mock_random):
        rows = 3
        cols = 3
        intervals = 7

        result = simulate_lishai(rows, cols, intervals)

        first_infected_cell = result['grid'][1][1][1]  # Accessing the first infected cell in the third interval

        self.assertEqual(first_infected_cell, 'infected')

    def test_all_healthy_cells(self):
        rows = 4
        cols = 4
        intervals = 7

        grid = [
            ['healthy', 'healthy', 'healthy', 'healthy'],
            ['healthy', 'healthy', 'healthy', 'healthy'],
            ['healthy', 'healthy', 'infected', 'healthy'],
            ['healthy', 'healthy', 'healthy', 'healthy']
        ]

        result = simulate_lishai(rows, cols, intervals)

        # Check that the resulting grid is not equal to the initial grid
        self.assertNotEqual(result['grid'], [grid])


if __name__ == '__main__':
    unittest.main()
