class Rook:
        
        def __init__(self, colour):
                self.colour = colour
                self.name = "Rook"
                if self.colour == "Black":
                        self.symbol = '♜'
                elif self.colour == "White":
                        self.symbol = '♖'

        def illegal_directions(self, start_row, start_col, end_row, end_col):
                return any([(start_row != end_row and start_col != end_col), # cant move diagonally

                ]
                )
