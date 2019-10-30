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
                current_board = self.board
                piece_to_move = self.board[start_row][start_col]
                print(piece_to_move)
                return any(
                        [self.__check_within_board_boundary(end_row,end_col),
                        (piece_to_move.illegal_directions(current_board, start_row, start_col, end_row, end_col)), # checks pawn allowed vectors
                        self.__bishop_specific_board_constraints(start_row, start_col, end_row, end_col)
                        ]
                        )

        def __check_within_board_boundary(self, end_row, end_col):
                return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)

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
