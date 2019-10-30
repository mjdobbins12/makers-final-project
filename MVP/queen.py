from piece import Piece

class Queen(Piece):
        def __init__(self, colour):
                self.colour = colour
                self.name = "Queen"
                if self.colour == "Black":
                        self.symbol = '♛'
                elif self.colour == "White":
                        self.symbol = '♕'

        def invalid_move_types(self, start_row, start_col, end_row, end_col):
