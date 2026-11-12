class Game:
    def __init__(self):
        self.map = []
        self.initialize_map()

    def initialize_map(self):
        self.map.append([0 for x in range(0, 11) for x in range(0, 11)])
        print("map initialzed")

ships = [

    [1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

class Ship:
    def __init__(self, type, orientation, position):
        self.type = type
        self.orientation = orientation
        self.position = position
        self.size = len(self.type)

        # if self.orientation == "v":
        #     for i in range(0, self.size):
        #         self.type.append(1 for x in range(0,1) for y in range(0, self.size))

    def __str__(self):
        return f"{self.type}"

match1 = Game()
print(match1.map)
ship1 = Ship([1, 1], "h", 0)
print(ship1)
