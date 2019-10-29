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
                if self.invalid_move(start_row, start_col, end_row, end_col):
                        raise ValueError("Invalid Move")
                self.board[start_row][start_col] = "-"
                self.board[end_row][end_col] = piece_to_move

        def invalid_move(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                return any(
                        [end_row > 7 or end_col > 7,
                        end_row < 0 or end_col < 0,
                        piece_to_move.colour == "Black" and end_row > start_row,
                        piece_to_move.colour == "White" and end_row < start_row,
                        start_row == end_row,
                        isinstance(piece_to_move, pawn.Pawn) and abs(start_row - end_row) > 2,
                        (start_row != 6 and start_row != 1) and abs(start_row - end_row) >= 2]
                        )

        
