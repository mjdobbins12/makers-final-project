from piece import Piece

class Rook(Piece):

        def __init__(self, colour):
                self.colour = colour
                self.name = "Rook"
                if self.colour == "Black":
                        self.symbol = '♜'
                        self.value = -50
                elif self.colour == "White":
                        self.symbol = '♖'
                        self.value = 50

        def illegal_directions(self, board, start_row, start_col, end_row, end_col):
                return any([(self.invalid_move_types(start_row, start_col, end_row, end_col)),  # cant move diagonally
                        (self.__rook_specific_board_constraints(board, start_row, start_col, end_row, end_col))
                        ]
                        )

        def invalid_move_types(self, start_row, start_col, end_row, end_col):
                if start_row != end_row and start_col != end_col:
                        return True
                else:
                        return False

        def __rook_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
                piece_to_move = board[start_row][start_col]
                return any([(self.check_if_row_or_column_blocked(board, start_row, start_col, end_row, end_col)),
                                (isinstance(board[end_row][end_col], Piece)
                                and board[end_row][end_col].colour == piece_to_move.colour),
                                ]
                                )
