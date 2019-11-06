from piece import Piece
from rook import Rook

class UnRook(Rook):

        def __init__(self, colour):
                self.colour = colour
                self.name = "Rook"
                if self.colour == "Black":
                        self.symbol = '♜'
                        self.value = -50
                elif self.colour == "White":
                        self.symbol = '♖'
                        self.value = 50

        def invalid_move_types(self, start_row, start_col, end_row, end_col):
                return True
        

