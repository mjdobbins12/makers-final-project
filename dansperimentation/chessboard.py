import pawn
    
class ChessBoard:
    def __init__(self):
        self.board = [
            ["R","N","B","K","Q","B","N","R"],
            [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
            pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-"],
            [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
            pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
            ["R","N","B","Q","K","B","N","R"]
            ]

    def show_board(self):
        return self.board

    def move(self, start_row, start_col, end_row, end_col):
        piece_to_move = self.board[start_row][start_col]
        self.board[start_row][start_col] = "-"
        self.board[end_row][end_col] = piece_to_move

        if piece_to_move == 'p' and abs(start_row - end_row) > 2:
            raise ValueError("Invalid Move")