from piece import Piece

class Bishop:
    def __init__(self, colour):
        self.colour = colour
        self.name = "Bishop"
        if self.colour == "Black":
            self.symbol = '♝'
        elif self.colour == "White":
            self.symbol = "♗"

    def illegal_directions(self, start_row, start_col, end_row, end_col):
        return (
            abs(start_row - end_row) != abs(start_col - end_col) # must move the same absolute number of squares in x and y directions
            )
