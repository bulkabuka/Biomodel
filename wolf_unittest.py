import unittest
from io import StringIO
from contextlib import redirect_stdout
from wolf import Rabbit, Wolf, SheWolf, Island, simulate_game


class TestIsland(unittest.TestCase):
    def test_add_rabbit(self):
        island = Island(5)
        island.add_rabbit(2, 3)
        self.assertEqual(len(island.population['rabbits']), 1)
        self.assertEqual(island.grid[3][2], '🐇')

    def test_add_wolf(self):
        island = Island(5)
        island.add_wolf(1, 4)
        self.assertEqual(len(island.population['wolves']), 1)
        self.assertEqual(island.grid[4][1], '🐺')

    def test_add_she_wolf(self):
        island = Island(5)
        island.add_she_wolf(4, 2)
        self.assertEqual(len(island.population['she-wolves']), 1)
        self.assertEqual(island.grid[2][4], '🐶')

    def test_rabbit_move(self):
        island = Island(5)
        rabbit = Rabbit(2, 3)
        island.grid[3][2] = rabbit
        rabbit.move(island)
        self.assertIn(island.grid[rabbit.y][rabbit.x], ['🌿', '🐇'])

    def test_wolf_move(self):
        island = Island(5)
        wolf = Wolf(1, 4)
        island.grid[4][1] = wolf
        wolf.move(island)
        self.assertIn(island.grid[wolf.y][wolf.x], ['🌿', '🐺'])

    def test_she_wolf_move(self):
        island = Island(5)
        she_wolf = SheWolf(4, 2)
        island.grid[2][4] = she_wolf
        she_wolf.move(island)
        self.assertIn(island.grid[she_wolf.y][she_wolf.x], ['🌿', '🐶'])

    def test_breed_she_wolf(self):
        island = Island(5)
        she_wolf = SheWolf(1, 1)
        island.grid[1][1] = she_wolf
        she_wolf.breed(island)
        self.assertEqual(len(island.population['she-wolves']), 2)

    def test_print_grid(self):
        island = Island(5)
        island.add_rabbit(1, 1)
        island.add_wolf(3, 3)
        island.add_she_wolf(2, 2)
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            island.print_grid()
        output = captured_output.getvalue().strip()
        expected_output = '🌿 🌿 🌿 🌿 🌿\n🌿 🐇 🌿 🌿 🌿\n🌿 🌿 🐶 🌿 🌿\n🌿 🌿 🌿 🐺 🌿\n🌿 🌿 🌿 🌿 🌿'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
