import random


class Game:
    def __init__(self):
        self.map = []
        self.initialize_map()

    def initialize_map(self):
        for i in range(0, 11):
            self.map.append([0,0,0,0,0,0,0,0,0,0])

    def place(self, ship, x, y):
        if ship.orientation=="h":
            for i in range(0, ship.size):
                self.map[y][x+i] = 1
                print(i)

        else:
            for i in range(0, ship.size):
                self.map[y+i-1][x] = 1
                print(i)

    def hit(self, x, y):
        if self.map[x][y] == 1:
            print("HIT SHIP")
            self.map[x][y] == "H"
        else:
            self.map[x][y] == "x"



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
board.place(launcher, 0, 3)
board.hit(0, 3)
print(board.map)

