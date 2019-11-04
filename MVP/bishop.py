from piece import Piece

class Bishop(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.name = "Bishop"
        if self.colour == "Black":
            self.symbol = '♝'
            self.value = -3
        elif self.colour == "White":
            self.symbol = "♗"
            self.value = 3

    def illegal_directions(self, board, start_row, start_col, end_row, end_col):
        return any([
            abs(start_row - end_row) != abs(start_col - end_col), # must move the same absolute number of squares in x and y directions
            self.__bishop_specific_board_constraints(board, start_row, start_col, end_row, end_col)
            ])

    def __bishop_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
            piece_to_move = board[start_row][start_col]
            return any([
                (self.check_if_diagonal_blocked(board, start_row, start_col, end_row, end_col)),
                (isinstance(board[end_row][end_col], Piece) and board[end_row][end_col].colour == piece_to_move.colour),
            ])
