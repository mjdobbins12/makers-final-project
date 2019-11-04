from piece import Piece

class Queen(Piece):
        def __init__(self, colour):
                self.colour = colour
                self.name = "Queen"
                if self.colour == "Black":
                        self.symbol = '♛'
                        self.value = -9
                elif self.colour == "White":
                        self.symbol = '♕'
                        self.value = 9

        def illegal_directions(self, board, start_row, start_col, end_row, end_col):
                return any([self.invalid_move_types(start_row, start_col, end_row, end_col),
                        self.__queen_specific_board_constraints(board, start_row, start_col, end_row, end_col)
                        ])


        def invalid_move_types(self, start_row, start_col, end_row, end_col):
                return any([self.__can_only_move_like_rook_or_bishop(start_row, start_col, end_row, end_col)
                ])

        # private methods

        def __can_only_move_like_rook_or_bishop(self, start_row, start_col, end_row, end_col):
                if abs(start_row - end_row) > 1 and abs(start_col - end_col) != 0 and abs(start_col - end_col) != abs(start_row - end_row):
                        return True
                elif abs(start_col - end_col) > 1 and abs(start_row - end_row) != 0 and abs(start_row - end_row) != abs(start_col - end_col):
                        return True
                else:
                        return False

        def __queen_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
                piece_to_move = board[start_row][start_col]
                end_square_taken = (isinstance(board[end_row][end_col], Piece) and board[end_row][end_col].colour == piece_to_move.colour)
                if (start_row != end_row and start_col != end_col) and abs(start_row - end_row) == abs(start_col - end_col):
                        blocker_to_check = self.check_if_diagonal_blocked(board, start_row, start_col, end_row, end_col)
                        # print([board[start_row][start_col], blocker_to_check, [start_row, start_col, end_row, end_col], end_square_taken])
                elif start_row == end_row or start_col == end_col:
                        blocker_to_check = self.check_if_row_or_column_blocked(board, start_row, start_col, end_row, end_col)
                else: 
                        return True
                return any([
                        (blocker_to_check),
                        (end_square_taken)
                        ])
