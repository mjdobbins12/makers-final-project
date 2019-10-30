class Bishop:
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "Black":
            self.name = '♝'
        elif self.colour == "White":
            self.name = "♗"

    def illegal_directions(self, start_row, start_col, end_row, end_col):
        return (
            abs(start_row - end_row) != abs(start_col - end_col) # must move the same absolute number of squares in x and y directions
            )
