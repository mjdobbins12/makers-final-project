class Knight:
        def __init__(self, colour):
                self.colour = colour
                if self.colour == "Black":
                        self.name = 'Knight'
                elif self.colour == "White":
                        self.name = "Knight"
        
        def illegal_directions(self, start_row, start_col, end_row, end_col):
               return any([
                        (not abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2) or # vertical L shape
                        not abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1 # horizontal L shape 
                        ])
                        
