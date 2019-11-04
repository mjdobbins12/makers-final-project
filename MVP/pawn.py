from piece import Piece

class Pawn(Piece):
        def __init__(self, colour):
                self.colour = colour
                self.name = "Pawn"

                if self.colour == "Black":
                        self.symbol = '♟'
                        self.value = -1
                elif self.colour == "White":
                        self.symbol = "♙"
                        self.value = 1

        def illegal_directions(self, board, start_row, start_col, end_row, end_col):
                return any([
                        self.invalid_move_types(start_row, start_col, end_row, end_col),
                        self.__pawn_specific_board_constraints(board, start_row, start_col, end_row, end_col)
                        ]
                        )

        def invalid_move_types(self, start_row, start_col, end_row, end_col):
                return any([self.colour == "Black" and end_row < start_row,
                        self.colour == "White" and end_row > start_row,
                        start_row == end_row, # cannot move sideways
                        
                        abs(start_row - end_row) > 2, # cannot move more than 2 spaces
                        (start_row != 6 and start_row != 1) and abs(start_row - end_row) >= 2, # cannot move 2 spaces after 1st move
                        abs(start_col - end_col) > 1, # can't move diagonally more than 1 space
                        abs(start_row - end_row) == 2 and start_col != end_col # can't move two spaces forward and sideways
                        ]
                        )


        def __pawn_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
                piece_to_move = board[start_row][start_col]
                if isinstance(piece_to_move, Pawn):
                        return any([start_col == end_col and isinstance(board[end_row][end_col], Piece),  # cannot move forward one space into another pawn
                                (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1 and not isinstance(
                                board[end_row][end_col], Piece)),  # can only strike if pawn on target square
                                piece_to_move.colour == "White" and abs(end_row - start_row) == 2 and end_row < 7 and isinstance(
                                board[end_row+1][end_col], Piece),  # black cannot jump over pawn
                                piece_to_move.colour == "Black" and abs(end_row - start_row) == 2 and end_row > 0 and isinstance(
                                board[end_row-1][end_col], Piece),  # white cannot jump over pawn
                                hasattr(board[end_row][end_col], 'colour') and
                                        piece_to_move.colour == board[end_row][end_col].colour # cannot take any pieces of same colour
                                ]
                                )
