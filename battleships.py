import random


class Game:
    def __init__(self):
        self.map = []
        self.initialize_map()

    def initialize_map(self):
        for i in range(0, 10):
            self.map.append([0,0,0,0,0,0,0,0,0,0])
    def place(self, size, orientation, x, y):
        if orientation == "h":
            for i in range(0, size):
                if x+(size) <= 10:
                    self.map[y][x+i] = 1
                else:
                    print("Invalid Ship Position")
                    break
                    

        else:
            for i in range(0, size):
                if y+(size) <= 10:
                    self.map[y+i][x] = 1
                #print(i)
                else:
                    print("Invalid Ship Position")
                    break

    def hit(self, x, y):
        if self.map[x][y] == 1:
            print("HIT SHIP")
            self.map[x][y] == "H"
        else:
            self.map[x][y] == "x"

    def __str__(self):
        return self.map

ships = [
    [1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

#TESTING: 

# board = Game()
# launcher=Ship(1)
# board.place(launcher,"v", 7, 2)
# board.hit(0, 1)
# print(board.map)


#Game loop
player1 = Game()
player2 = Game()
print(player1.map)

for ship in ships:

    print(f"ship type: {ship}")

    coords = input("where would you like to place the ships?(top left is 0,0): ")
    x, y = coords.split(" ")
    int(x)
    int(y)

    orientation = input("what orientation would u like ur ship to be?(h, v): ")

    player1.place(len(ship), orientation, x, y)
    print(player1.map)