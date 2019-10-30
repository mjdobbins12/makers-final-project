from piece import Piece

class Queen(Piece):
        def __init__(self, colour):
                self.colour = colour
                self.name = "Queen"
                if self.colour == "Black":
                        self.symbol = '♛'
                elif self.colour == "White":
                        self.symbol = '♕'

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
                return any([
                        (self.__check_if_diagonal_blocked(board, start_row, start_col, end_row, end_col)),
                        (self.__check_if_row_or_column_blocked(board, start_row, start_col, end_row, end_col)),
                        (isinstance(board[end_row][end_col], Piece) and board[end_row][end_col].colour == piece_to_move.colour)
                        ])

        # below methods only referenced in the queen specific board constraints method

        def __check_if_row_or_column_blocked(self, board, start_row, start_col, end_row, end_col):
                if start_row == end_row:
                        if start_col > end_col:
                                squares_between = list(
                                range(end_col + 1, start_col))
                        else:
                                squares_between = list(
                                range(start_col + 1, end_col))
                        squares_between[:] = [board[start_row][element]
                                        for element in squares_between]
                        if any(isinstance(x, Piece) for x in squares_between):
                                return True
                else:
                        if start_row > end_row:
                                squares_between = list(
                                range(end_row + 1, start_row))
                        else:
                                squares_between = list(
                                range(start_row + 1, end_row))
                        squares_between[:] = [board[element][start_col]
                                        for element in squares_between]
                        if any(isinstance(x, Piece) for x in squares_between):
                                return True

        def __check_if_diagonal_blocked(self, board, start_row, start_col, end_row, end_col):
                if start_row < end_row and start_col < end_col:
                        check_square = board[start_row + 1][start_col + 1]
                        if isinstance(check_square, Piece):
                                return True
                        elif check_square == board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(
                                self, start_row + 1, start_col + 1, end_row, end_col)
                elif start_row > end_row and start_col > end_col:
                        check_square = board[start_row - 1][start_col - 1]
                        if isinstance(check_square, Piece):
                                return True
                        elif check_square == board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(
                                self, start_row - 1, start_col - 1, end_row, end_col)
                elif start_row < end_row and start_col > end_col:
                        check_square = board[start_row + 1][start_col - 1]
                        if isinstance(check_square, Piece):
                                return True
                        elif check_square == board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(
                                self, start_row + 1, start_col - 1, end_row, end_col)
                elif start_row > end_row and start_col < end_col:
                        check_square = board[start_row - 1][start_col + 1]
                        if isinstance(check_square, Piece):
                                return True
                        elif check_square == board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(
                                self, start_row - 1, start_col + 1, end_row, end_col)
