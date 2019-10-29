class ChessBoard:
    board = [
        ["R","N","B","K","Q","B","N","R"],
        ['p','p','p','p','p','p','p','p'],
        ["-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ['p','p','p','p','p','p','p','p'],
        ["R","N","B","Q","K","B","N","R"]
        ]

    def show_board(self):
        return self.board

    def move(self, start_row, start_col, end_row, end_col):
        self.board[start_row][start_col] = "-"
        self.board[end_row][end_col] = "-"