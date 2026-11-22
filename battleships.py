import random


class Game:

    ships_hit = 0

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
            self.map[x][y] = "H"
            self.ships_hit +=1
        else:
            self.map[x][y] = "X"

    def show(self, setup=False):
        if setup == False:
            for row in self.map:
                Crow = ""  
                for item in row:   
                    if item == 0 or item == 1:
                        Crow += "❓"
                    elif item == "X":
                        Crow += "🌊"
                    else:
                        Crow += "💥"
                print(Crow)
        else:
            for row in self.map:
                Crow = ""
                for item in row:
                    if item == 0:
                        Crow += "🌊"
                    if item == 1:
                        Crow += "🚢"
                print(Crow)
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

for ship in ships:

    player1.show(True)
    print(f"ship type: {ship}")

    coords = input("where would you like to place the ships?(top left is 0,0): ")
    x, y = coords.split(" ")
    x = int(x)
    y = int(y)

    orientation = input("what orientation would u like ur ship to be?(h, v): ")

    player1.place(len(ship), orientation, x, y)

player1.show()

print('\033[H\033[J', end='')
print("Player two choose ship positions")

for ship in ships:

    player2.show(True)
    print(f"ship type: {ship}")

    coords = input("where would you like to place the ships?(top left is 0,0): ")
    x, y = coords.split(" ")
    x = int(x)
    y = int(y)

    orientation = input("what orientation would u like ur ship to be?(h, v): ")

    player2.place(len(ship), orientation, x, y)

player2.show()

