class ChessBoard:
    def __init__(self):
        self.board = [
        ["R","N","B","K","Q","B","N","R"],
        ['p','p','p','p','p','p','p','p'],
        ["-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ['p','p','p','p','p','p','p','p'],
        ["R","N","B","Q","K","B","N","R"]
        ]

    def show_board(self, p1_name, p2_name):
        print('')
        print(p2_name)
        print("_" * 33)
        for row in self.board:
            x = " | "
            print(f"| {x.join(row)} |")
            print("-" * 33)
        print(p1_name)
        print('')


    def move(self, start_row, start_col, end_row, end_col):
        piece_to_move = self.board[start_row][start_col]
        self.board[start_row][start_col] = "-"
        self.board[end_row][end_col] = piece_to_move
        if piece_to_move == 'p' and abs(start_row - end_row) > 2:
            raise ValueError("Invalid Move")
