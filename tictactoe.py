class Board:
    def __init__(self):
        self.board = [[0,0,0] for x in range(0, 3)]


    def place(self, position, player_symbol):
        flattened_board = [item for row in self.board for item in row]
        if flattened_board[position] == 0:
            flattened_board[position] = player_symbol
        else:
            return "not valid"

    def check_for_winner(self):
        for row in self.board:
            if row[0] == len(row(row[0])): #only works for horizontal
                print(f"{row[0]} has won!")
            