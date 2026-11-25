class Board:
    def __init__(self):
        self.board = [[0,0,0] for x in range(0, 3)]


    def place(self, position, player_symbol):
        flattened_board = [item for row in self.board for item in row]
        if flattened_board[position] == 0:
            flattened_board[position] = player_symbol
        else:
            return "not valid"

    