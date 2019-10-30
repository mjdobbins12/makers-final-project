from piece import Piece

class Knight(Piece):
        def __init__(self, colour):
                self.colour = colour
                self.name = "Knight"
                if self.colour == "Black":
                        self.symbol = '♞'
                elif self.colour == "White":
                        self.symbol = "♘"
        
        def illegal_directions(self, board, start_row, start_col, end_row, end_col):
                return any([
                        not (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2 or # vertical L shape
                        abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1), # horizontal L shape
                        (self.__knight_specific_board_constraints(board, start_row, start_col, end_row, end_col))  
                        ])

        def __knight_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
                piece_to_move = board[start_row][start_col]
                return any([
                        hasattr(board[end_row][end_col], 'colour') and
                        # knight cannot take any piece of same colour
                        piece_to_move.colour == board[end_row][end_col].colour
                        ]
                        )
                        
