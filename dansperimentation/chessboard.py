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
        if end_row > 7 or end_col > 7:
            raise ValueError("Invalid Move")
        
        piece_to_move = self.board[start_row][start_col]
        self.board[start_row][start_col] = "-"
        self.board[end_row][end_col] = piece_to_move

        if piece_to_move.colour == "Black" and end_row > start_row:
            raise ValueError("Invalid Move")
        if piece_to_move.colour == "White" and end_row < start_row:
            raise ValueError("Invalid Move")
        
        if isinstance(piece_to_move, pawn.Pawn) and abs(start_row - end_row) > 2:
            raise ValueError("Invalid Move")
        
        if (start_row != 6 and start_row != 1) and abs(start_row - end_row) >= 2:
             raise ValueError("Invalid Move")
        
