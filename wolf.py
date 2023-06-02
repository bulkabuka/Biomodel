import random


class Island:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.population = {'rabbits': [], 'wolves': [], 'she-wolves': []}
        self.score = 0

    def add_rabbit(self, x, y):
        rabbit = Rabbit(x, y)
        self.population['rabbits'].append(rabbit)
        self.grid[y][x] = rabbit

    def add_wolf(self, x, y):
        wolf = Wolf(x, y)
        self.population['wolves'].append(wolf)
        self.grid[y][x] = wolf

    def add_she_wolf(self, x, y):
        she_wolf = SheWolf(x, y)
        self.population['she-wolves'].append(she_wolf)
        self.grid[y][x] = she_wolf

    def move(self):
        for wolf in self.population['wolves']:
            wolf.move(self)
        for she_wolf in self.population['she-wolves']:
            she_wolf.move(self)
        for rabbit in self.population['rabbits']:
            rabbit.move(self)

    def remove_dead_animals(self):
        self.population['wolves'] = [wolf for wolf in self.population['wolves'] if wolf.score > 0]
        self.population['she-wolves'] = [she_wolf for she_wolf in self.population['she-wolves'] if she_wolf.score > 0]

    def print_grid(self):
        for row in self.grid:
            print(' '.join([str(cell) if cell else '-' for cell in row]))


class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, island):
        possible_moves = [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)]
        valid_moves = [(x, y) for (x, y) in possible_moves if 0 <= x < island.size and 0 <= y < island.size]
        new_x, new_y = random.choice(valid_moves)
        if not island.grid[new_y][new_x]:
            island.grid[self.y][self.x] = None
            self.x = new_x
            self.y = new_y
            island.grid[self.y][self.x] = self

    def __repr__(self):
        return self.symbol


class Rabbit(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = 'R'

    def move(self, island):
        super().move(island)
        if random.random() < 1 / 9:
            new_x, new_y = random.choice(
                [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)])
            if 0 <= new_x < island.size and 0 <= new_y < island.size and not island.grid[new_y][new_x]:
                island.add_rabbit(new_x, new_y)

        if random.random() < 0.2:
            new_x, new_y = random.choice(
                [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)])
            if 0 <= new_x < island.size and 0 <= new_y < island.size and not island.grid[new_y][new_x]:
                island.add_rabbit(new_x, new_y)


class Wolf(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = 'W'
        self.score = 0

    def move(self, island):
        super().move(island)
        if not island.population['rabbits']:
            return

        nearby_rabbits = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < island.size and 0 <= new_y < island.size and isinstance(island.grid[new_y][new_x], Rabbit):
                    nearby_rabbits.append((new_x, new_y))

        if nearby_rabbits:
            target_x, target_y = random.choice(nearby_rabbits)
            self.score += 1
            island.score += 1
            rabbit = island.grid[target_y][target_x]
            island.population['rabbits'].remove(rabbit)
            island.grid[target_y][target_x] = None
            return

        self.score -= 0.1

        she_wolf = None
        if island.population['she-wolves']:
            she_wolf = island.population['she-wolves'][0]
            for sw in island.population['she-wolves']:
                if abs(sw.x - self.x) + abs(sw.y - self.y) < abs(she_wolf.x - self.x) + abs(she_wolf.y - self.y):
                    she_wolf = sw

        if she_wolf and abs(she_wolf.x - self.x) <= 1 and abs(she_wolf.y - self.y) <= 1:
            if island.grid[she_wolf.y][she_wolf.x] == she_wolf:
                self.score += 1
                island.score += 1
                offspring_gender = random.choice(['M', 'F'])
                offspring_x, offspring_y = random.choice(
                    [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)])
                if 0 <= offspring_x < island.size and 0 <= offspring_y < island.size and not island.grid[offspring_y][
                    offspring_x]:
                    if offspring_gender == 'M':
                        island.add_wolf(offspring_x, offspring_y)
                    else:
                        island.add_she_wolf(offspring_x, offspring_y)


class SheWolf(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = 'S'
        self.score = 0

    def move(self, island):
        super().move(island)
        if not island.population['rabbits']:
            return

        nearby_rabbits = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < island.size and 0 <= new_y < island.size and isinstance(island.grid[new_y][new_x], Rabbit):
                    nearby_rabbits.append((new_x, new_y))

        if nearby_rabbits:
            target_x, target_y = random.choice(nearby_rabbits)
            self.score += 1
            island.score += 1
            rabbit = island.grid[target_y][target_x]
            island.population['rabbits'].remove(rabbit)
            island.grid[target_y][target_x] = None
            return

        self.score -= 0.1

        wolf = None
        if island.population['wolves']:
            wolf = island.population['wolves'][0]
            for w in island.population['wolves']:
                if abs(w.x - self.x) + abs(w.y - self.y) < abs(wolf.x - self.x) + abs(wolf.y - self.y):
                    wolf = w

        if wolf and abs(wolf.x - self.x) <= 1 and abs(wolf.y - self.y) <= 1:
            if island.grid[wolf.y][wolf.x] == wolf:
                self.score += 1
                island.score += 1
                offspring_gender = random.choice(['M', 'F'])
                offspring_x, offspring_y = random.choice(
                    [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)])
                if 0 <= offspring_x < island.size and 0 <= offspring_y < island.size and not island.grid[offspring_y][
                    offspring_x]:
                    if offspring_gender == 'M':
                        island.add_wolf(offspring_x, offspring_y)
                    else:
                        island.add_she_wolf(offspring_x, offspring_y)


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
    print()

    for _ in range(10):
        island.move()
        island.remove_dead_animals()
        island.print_grid()
        print()


simulate_game()
