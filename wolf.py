import random


class Island:
    def __init__(self, size):
        self.size = size
        self.grid = [['🌿' for _ in range(size)] for _ in range(size)]
        self.population = {'rabbits': [], 'wolves': [], 'she-wolves': []}

    def add_rabbit(self, x, y):
        rabbit = Rabbit(x, y)
        self.population['rabbits'].append(rabbit)
        self.grid[y][x] = rabbit.symbol

    def add_wolf(self, x, y):
        wolf = Wolf(x, y)
        self.population['wolves'].append(wolf)
        self.grid[y][x] = wolf.symbol

    def add_she_wolf(self, x, y):
        she_wolf = SheWolf(x, y)
        self.population['she-wolves'].append(she_wolf)
        self.grid[y][x] = she_wolf.symbol

    def move(self):
        for wolf in self.population['wolves']:
            wolf.move(self)
        for she_wolf in self.population['she-wolves']:
            she_wolf.move(self)
        for rabbit in self.population['rabbits']:
            rabbit.move(self)
        self.update_grid()

    def update_grid(self):
        self.grid = [['🌿' for _ in range(self.size)] for _ in range(self.size)]
        for rabbit in self.population['rabbits']:
            self.grid[rabbit.y][rabbit.x] = rabbit.symbol
        for wolf in self.population['wolves']:
            self.grid[wolf.y][wolf.x] = wolf.symbol
        for she_wolf in self.population['she-wolves']:
            self.grid[she_wolf.y][she_wolf.x] = she_wolf.symbol

    def remove_dead_animals(self):
        self.population['wolves'] = [wolf for wolf in self.population['wolves'] if wolf.score > 0]
        self.population['she-wolves'] = [she_wolf for she_wolf in self.population['she-wolves'] if she_wolf.score > 0]

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()
        return self.grid


class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 1
        self.symbol = ''

    def move(self, island):
        possible_moves = [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)]
        valid_moves = [(x, y) for (x, y) in possible_moves if 0 <= x < island.size and 0 <= y < island.size]
        new_x, new_y = random.choice(valid_moves)

        if not isinstance(island.grid[new_y][new_x], Animal):
            self.x = new_x
            self.y = new_y


class Rabbit(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = '🐇'

    def move(self, island):
        super().move(island)
        if random.random() < 0.2:
            for _ in range(2):
                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < island.size and 0 <= new_y < island.size and not isinstance(island.grid[new_y][new_x], Animal):
                    island.add_rabbit(new_x, new_y)


class Wolf(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = '🐺'

    def move(self, island):
        super().move(island)
        if random.random() < 0.2:
            for _ in range(2):
                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < island.size and 0 <= new_y < island.size:
                    if isinstance(island.grid[new_y][new_x], Rabbit):
                        island.population['rabbits'] = [rabbit for rabbit in island.population['rabbits'] if
                                                       not (rabbit.x == new_x and rabbit.y == new_y)]
                        island.grid[new_y][new_x] = self.symbol
                    elif isinstance(island.grid[new_y][new_x], SheWolf):
                        she_wolf = [she_wolf for she_wolf in island.population['she-wolves'] if
                                    she_wolf.x == new_x and she_wolf.y == new_y]
                        if she_wolf:
                            she_wolf[0].breed(island)


class SheWolf(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = '🐶'

    def move(self, island):
        super().move(island)
        if random.random() < 0.2:
            for _ in range(2):
                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < island.size and 0 <= new_y < island.size:
                    if isinstance(island.grid[new_y][new_x], Rabbit):
                        island.population['rabbits'] = [rabbit for rabbit in island.population['rabbits'] if
                                                       not (rabbit.x == new_x and rabbit.y == new_y)]
                        island.grid[new_y][new_x] = self.symbol
                    elif isinstance(island.grid[new_y][new_x], Wolf):
                        wolf = [wolf for wolf in island.population['wolves'] if wolf.x == new_x and wolf.y == new_y]
                        if wolf:
                            wolf[0].breed(island)

    def breed(self, island):
        for _ in range(2):
            dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < island.size and 0 <= new_y < island.size and not isinstance(island.grid[new_y][new_x], Animal):
                island.add_she_wolf(new_x, new_y)


def simulate_game():
    island = Island(20)
    for _ in range(10):
        x, y = random.randint(0, 19), random.randint(0, 19)
        island.add_rabbit(x, y)
    for _ in range(5):
        x, y = random.randint(0, 19), random.randint(0, 19)
        island.add_wolf(x, y)
    for _ in range(5):
        x, y = random.randint(0, 19), random.randint(0, 19)
        island.add_she_wolf(x, y)

    island.print_grid()

    for _ in range(20):
        island.move()
        island.remove_dead_animals()
        island.print_grid()
        print()
    return island
