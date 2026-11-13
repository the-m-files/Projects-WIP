import random


class Game:
    def __init__(self):
        self.map = []
        self.initialize_map()

    def initialize_map(self):
        self.map.append([0 for x in range(0, 10) for y in range(0, 10)])

    def place(self, ship, x, y):
        for i in range(0, ship.size):
            self.map[x][y] = 1
            print(i)



ships = [

    [1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

class Ship:
    def __init__(self, type, orientation):
        self.type = ships[type]
        self.orientation = orientation
        self.size = len(self.type)

        # if self.orientation == "v":
        #     for i in range(0, self.size):
        #         self.type.append(1 for x in range(0,1) for y in range(0, self.size))

    def __str__(self):
        return f"{self.type}"

board = Game()
launcher=Ship(1, "h")
board.place(launcher, 0, 0)
print(board.map)