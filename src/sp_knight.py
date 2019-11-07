from piece import Piece
from queen import Queen

class SpKnight(Queen):

        def __init__(self, colour):
                self.colour = colour
                self.name = "Knight"
                if self.colour == "Black":
                        self.symbol = '♞'
                        self.value = -30
                elif self.colour == "White":
                        self.symbol = "♘"
                        self.value = 30
        
        
