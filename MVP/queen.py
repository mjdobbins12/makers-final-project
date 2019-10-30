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
                return any([self.__can_only_move_like_rook_or_bishop(start_row, start_col, end_row, end_col),
                ])

        def __can_only_move_like_rook_or_bishop(self, start_row, start_col, end_row, end_col):
                if abs(start_row - end_row) > 1 and abs(start_col - end_col) != 0 and abs(start_col - end_col) != abs(start_row - end_row):
                        return True
                elif abs(start_col - end_col) > 1 and abs(start_row - end_row) != 0 and abs(start_row - end_row) != abs(start_col - end_col):
                        return True
                else:
                        return False
                
