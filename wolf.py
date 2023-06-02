import numpy as np
import random


class Animal:
    def __init__(self, point=1, simulation=None):
        self.point = point
        self.simulation = simulation

    def move(self, matrix, current_position):
        raise NotImplementedError()


class Rabbit(Animal):
    def move(self, matrix, current_position):
        neighbors = Simulation.get_neighboring_cells(simulation, current_position)
        direction = random.choice(neighbors + [current_position] * 2)  # 1/9 chance to stay in place

        if matrix[direction].get('type') == 0:  # Only move to free spaces
            matrix[direction], matrix[current_position] = matrix[current_position], matrix[direction]

        if random.random() < 0.2:  # 1/5 chance to multiply
            free_neighbors = [position for position in neighbors if matrix[position].get('type') == 0]
            if free_neighbors:
                new_position = random.choice(free_neighbors)
                matrix[new_position] = {'type': 1, 'object': Rabbit()}


class SheWolf(Animal):
    def move(self, matrix, current_position):
        neighbors = Simulation.get_neighboring_cells(simulation, current_position)
        rabbit_neighbors = [position for position in neighbors if matrix[position].get('type') == 1]

        if rabbit_neighbors:  # If there are rabbits, eat one
            eat_position = random.choice(rabbit_neighbors)
            matrix[eat_position], matrix[current_position] = matrix[current_position], matrix[eat_position]
            self.point += 1
        else:  # If no rabbits, move randomly
            free_neighbors = [position for position in neighbors if matrix[position].get('type') == 0]
            if free_neighbors:
                new_position = random.choice(free_neighbors)
                matrix[new_position], matrix[current_position] = matrix[current_position], matrix[new_position]
                self.point -= 0.1

        if self.point <= 0:
            matrix[current_position] = {'type': 0, 'object': None}  # Dead


class HeWolf(Animal):
    def move(self, matrix, current_position):
        neighbors = Simulation.get_neighboring_cells(simulation, current_position)
        rabbit_neighbors = [position for position in neighbors if matrix[position].get('type') == 1]
        she_wolf_neighbors = [position for position in neighbors if matrix[position].get('type') == 3]

        if rabbit_neighbors:  # If there are rabbits, eat one
            eat_position = random.choice(rabbit_neighbors)
            matrix[eat_position], matrix[current_position] = matrix[current_position], matrix[eat_position]
            self.point += 1
        elif she_wolf_neighbors:  # If no rabbits but she-wolves, procreate
            procreate_position = random.choice(she_wolf_neighbors)
            free_neighbors = [position for position in neighbors if matrix[position].get('type') == 0]
            if free_neighbors:
                new_position = random.choice(free_neighbors)
                new_animal_type = random.choice([2, 3])  # Randomly choose he-wolf or she-wolf
                matrix[new_position] = {'type': new_animal_type,
                                        'object': HeWolf() if new_animal_type == 2 else SheWolf()}
        else:  # If no rabbits or she-wolves, move randomly
            free_neighbors = [position for position in neighbors if matrix[position].get('type') == 0]
            if free_neighbors:
                new_position = random.choice(free_neighbors)
                matrix[new_position], matrix[current_position] = matrix[current_position], matrix[new_position]
                self.point -= 0.1

        if self.point <= 0:
            matrix[current_position] = {'type': 0, 'object': None}  # Dead


class Simulation:
    def __init__(self, size=20, iterations=10):
        self.size = size
        self.iterations = iterations
        self.matrix = np.full((self.size, self.size), {'type': 0, 'object': None}, dtype=object)

    def get_neighboring_cells(self, position):
        x, y = position
        neighbors = [(nx, ny) for nx in range(max(0, x-1), min(self.size, x+2)) for ny in range(max(0, y-1), min(self.size, y+2)) if nx != x or ny != y]
        return neighbors

    def setup(self):
        for _ in range(100):  # Randomly place 100 of each type of animal
            for animal_type, animal_class in [(1, Rabbit), (2, HeWolf), (3, SheWolf)]:
                while True:
                    position = (random.randrange(self.size), random.randrange(self.size))
                    if self.matrix[position]['type'] == 0:
                        self.matrix[position] = {'type': animal_type, 'object': animal_class(1, self)}
                        break

    def run(self):
        self.setup()
        for _ in range(self.iterations):
            for (x, y), cell in np.ndenumerate(self.matrix):
                if cell['type'] != 0:
                    cell['object'].move(self.matrix, (x, y))


simulation = Simulation()
simulation.run()
