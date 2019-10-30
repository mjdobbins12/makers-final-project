import pawn
import bishop
import rook
import piece
import knight
import king
import queen

import standard_rules

class ChessBoard:
        def __init__(self):
<<<<<<< HEAD
                self.board = [
                        [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),queen.Queen(
                        "Black"),king.King("Black"),bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),queen.Queen("White"),king.King("White"),bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]
                        ]
=======
                self.rule_set = standard_rules.StandardRules()
                self.board = self.rule_set.starting_board
>>>>>>> Extract starting board to ruleset

        def move(self, start_row, start_col, end_row, end_col):
                if self.rule_set.invalid_move(self.board, start_row, start_col, end_row, end_col):
                        raise ValueError("Invalid Move")
                piece_to_move = self.board[start_row][start_col]
                self.board[start_row][start_col] = "-"
                self.board[end_row][end_col] = piece_to_move

        # private methods

<<<<<<< HEAD
        def __invalid_move(self, start_row, start_col, end_row, end_col):
                current_board = self.board
                piece_to_move = self.board[start_row][start_col]
                return any(
                        [self.__check_within_board_boundary(end_row,end_col),
                        (piece_to_move.illegal_directions(current_board, start_row, start_col, end_row, end_col)) # checks pawn allowed vectors
                        ]
                        )

        def __check_within_board_boundary(self, end_row, end_col):
                return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)
=======
        # def __invalid_move(self, start_row, start_col, end_row, end_col):
        #         current_board = self.board
        #         piece_to_move = self.board[start_row][start_col]
        #         print(piece_to_move)
        #         return any(
        #                 [self.__check_within_board_boundary(end_row,end_col),
        #                 (piece_to_move.illegal_directions(current_board, start_row, start_col, end_row, end_col)) # checks pawn allowed vectors
        #                 ]
        #                 )

        # def __check_within_board_boundary(self, end_row, end_col):
        #         return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)

        
>>>>>>> Extract starting board to ruleset
