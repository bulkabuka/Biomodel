import unittest
from io import StringIO
from contextlib import redirect_stdout
from wolf import Rabbit, Wolf, SheWolf, Island

class TestIsland(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.rabbit_x = 2
        self.rabbit_y = 3
        self.wolf_x = 1
        self.wolf_y = 4
        self.she_wolf_x = 2
        self.she_wolf_y = 2

    def test_add_rabbit(self):
        island = Island(self.size)
        island.add_rabbit(self.rabbit_x, self.rabbit_y)
        expected_population = 1
        expected_grid_value = '🐇'

        self.assertEqual(len(island.population['rabbits']), expected_population,
                         f"Ожидаемое количество кроликов: {expected_population}, получено: {len(island.population['rabbits'])}")
        self.assertEqual(island.grid[self.rabbit_y][self.rabbit_x], expected_grid_value,
                         f"Ожидаемое значение ячейки на острове: {expected_grid_value}, получено: {island.grid[self.rabbit_y][self.rabbit_x]}")

    def test_add_wolf(self):
        island = Island(self.size)
        island.add_wolf(self.wolf_x, self.wolf_y)
        expected_population = 1
        expected_grid_value = '🐺'

        self.assertEqual(len(island.population['wolves']), expected_population,
                         f"Ожидаемое количество волков: {expected_population}, получено: {len(island.population['wolves'])}")
        self.assertEqual(island.grid[self.wolf_y][self.wolf_x], expected_grid_value,
                         f"Ожидаемое значение ячейки на острове: {expected_grid_value}, получено: {island.grid[self.wolf_y][self.wolf_x]}")

    def test_add_she_wolf(self):
        island = Island(self.size)
        island.add_she_wolf(self.she_wolf_x, self.she_wolf_y)
        expected_population = 1
        expected_grid_value = '🐶'

        self.assertEqual(len(island.population['she-wolves']), expected_population,
                         f"Ожидаемое количество волчиц: {expected_population}, получено: {len(island.population['she-wolves'])}")
        self.assertEqual(island.grid[self.she_wolf_y][self.she_wolf_x], expected_grid_value,
                         f"Ожидаемое значение ячейки на острове: {expected_grid_value}, получено: {island.grid[self.she_wolf_y][self.she_wolf_x]}")

    def test_rabbit_move(self):
        island = Island(self.size)
        rabbit = Rabbit(self.rabbit_x, self.rabbit_y)
        island.grid[self.rabbit_y][self.rabbit_x] = rabbit
        rabbit.move(island)
        expected_grid_values = ['🌿', '🐇']

        self.assertIn(island.grid[rabbit.y][rabbit.x], expected_grid_values,
                      f"Непредвиденное значение ячейки после перемещения кролика: {island.grid[rabbit.y][rabbit.x]}")

    def test_wolf_move(self):
        island = Island(self.size)
        wolf = Wolf(self.wolf_x, self.wolf_y)
        island.grid[self.wolf_y][self.wolf_x] = wolf
        wolf.move(island)
        expected_grid_values = ['🌿', '🐺']

        self.assertIn(island.grid[wolf.y][wolf.x], expected_grid_values,
                      f"Непредвиденное значение ячейки после перемещения волка: {island.grid[wolf.y][wolf.x]}")

    def test_she_wolf_move(self):
        island = Island(self.size)
        she_wolf = SheWolf(self.she_wolf_x, self.she_wolf_y)
        island.grid[self.she_wolf_y][self.she_wolf_x] = she_wolf
        she_wolf.move(island)
        expected_grid_values = ['🌿', '🐶']

        self.assertIn(island.grid[she_wolf.y][she_wolf.x], expected_grid_values,
                      f"Непредвиденное значение ячейки после перемещения волчицы: {island.grid[she_wolf.y][she_wolf.x]}")

    def test_breed_she_wolf(self):
        island = Island(self.size)
        she_wolf = SheWolf(self.she_wolf_x, self.she_wolf_y)
        island.grid[self.she_wolf_y][self.she_wolf_x] = she_wolf
        she_wolf.breed(island)
        expected_population = 2

        self.assertEqual(len(island.population['she-wolves']), expected_population,
                         f"Ожидаемое количество волчиц после размножения: {expected_population}, получено: {len(island.population['she-wolves'])}")

    def test_print_grid(self):
        island = Island(5)
        island.add_rabbit(1, 1)
        island.add_wolf(3, 3)
        island.add_she_wolf(2, 2)
        expected_output = '🌿 🌿 🌿 🌿 🌿\n🌿 🐇 🌿 🌿 🌿\n🌿 🌿 🐶 🌿 🌿\n🌿 🌿 🌿 🐺 🌿\n🌿 🌿 🌿 🌿 🌿'

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            island.print_grid()
        output = captured_output.getvalue().strip()

        self.assertEqual(output, expected_output, "Некорректный вывод сетки на острове.")

    if __name__ == '__main__':
        unittest.main()