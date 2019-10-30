import pawn
import bishop
import rook
import piece
import knight

class ChessBoard:
        def __init__(self):
                self.board = [
                        [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),"Q","K",bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),"Q","K",bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]
                        ]

        def move(self, start_row, start_col, end_row, end_col):
                if self.__invalid_move(start_row, start_col, end_row, end_col):
                        raise ValueError("Invalid Move")
                piece_to_move = self.board[start_row][start_col]
                self.board[start_row][start_col] = "-"
                self.board[end_row][end_col] = piece_to_move

        # private methods

        def __invalid_move(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                return any(
                        [self.__check_within_board_boundary(end_row,end_col),
                        piece_to_move.illegal_directions(start_row, start_col, end_row, end_col), # checks pawn allowed vectors
                        self.__pawn_specific_board_constraints(start_row, start_col, end_row, end_col), # references board to check possibility of moves
                        self.__bishop_specific_board_constraints(start_row, start_col, end_row, end_col),
                        self.__knight_specific_board_constraints(start_row, start_col, end_row, end_col), # references board to check possibility of moves
                        self.__rook_specific_board_constraints(start_row, start_col, end_row, end_col)
                        ]
                        )

        def __check_within_board_boundary(self, end_row, end_col):
                return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)

        def __pawn_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, pawn.Pawn):
                        return any([start_col == end_col and isinstance(self.board[end_row][end_col], piece.Piece), # cannot move forward one space into another pawn
                                (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1 and not isinstance(self.board[end_row][end_col], piece.Piece)), # can only strike if pawn on target square
                                piece_to_move.colour == "White" and abs(end_row - start_row) == 2 and isinstance(self.board[end_row+1][end_col], piece.Piece), # black cannot jump over pawn
                                piece_to_move.colour == "Black" and abs(end_row - start_row) == 2 and isinstance(self.board[end_row-1][end_col], piece.Piece) # white cannot jump over pawn
                                ]
                                )

        def __rook_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, rook.Rook):
                        return any([(self.__check_if_row_or_column_blocked(start_row, start_col, end_row, end_col)),
                                (isinstance(self.board[end_row][end_col], piece.Piece) and self.board[end_row][end_col].colour == piece_to_move.colour), #
                                ]
                                )

        def __check_if_row_or_column_blocked(self, start_row, start_col, end_row, end_col):
                if start_row == end_row:
                        if start_col > end_col:
                                squares_between = list(range(end_col + 1, start_col))
                        else:
                                squares_between = list(range(start_col + 1, end_col))
                        squares_between[:] = [self.board[start_row][element] for element in squares_between]
                        if any(isinstance(x, piece.Piece) for x in squares_between):
                                return True
                else:
                        if start_row > end_row:
                                squares_between = list(range(end_row + 1, start_row))
                        else:
                                squares_between = list(range(start_row + 1, end_row))
                        squares_between[:] = [self.board[element][start_col] for element in squares_between]
                        if any(isinstance(x, piece.Piece) for x in squares_between):
                                return True

        def __knight_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, knight.Knight):
                        return any([
                                hasattr(self.board[end_row][end_col], 'colour') and
                                        piece_to_move.colour == self.board[end_row][end_col].colour # knight cannot take any piece of same colour
                                ]
                                )

        def __bishop_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, bishop.Bishop):
                        return (self.__check_if_diagonal_blocked(start_row, start_col, end_row, end_col))

        def __check_if_diagonal_blocked(self, start_row, start_col, end_row, end_col):
                if start_row < end_row and start_col < end_col:
                        check_square = self.board[start_row + 1][start_col + 1]
                        if isinstance(check_square, piece.Piece):
                                return True
                        elif check_square == self.board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(self, start_row + 1, start_col + 1, end_row, end_col)
                elif start_row > end_row and start_col > end_col:
                        check_square = self.board[start_row - 1][start_col - 1]
                        if isinstance(check_square, piece.Piece):
                                return True
                        elif check_square == self.board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(self, start_row - 1, start_col - 1, end_row, end_col)
                elif start_row < end_row and start_col > end_col:
                        check_square = self.board[start_row + 1][start_col - 1]
                        if isinstance(check_square, piece.Piece):
                                return True
                        elif check_square == self.board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(self, start_row + 1, start_col - 1, end_row, end_col)
                elif start_row > end_row and start_col < end_col:
                        check_square = self.board[start_row - 1][start_col + 1]
                        if isinstance(check_square, piece.Piece):
                                return True
                        elif check_square == self.board[end_row][end_col]:
                                return False
                        else:
                                self.__check_if_diagonal_blocked(self, start_row - 1, start_col + 1, end_row, end_col)
