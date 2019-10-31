import pawn
import bishop
import rook
import piece
import knight
import king
import queen

import standard_rules

import standard_rules

class ChessBoard:
        def __init__(self):
                self.rule_set = standard_rules.StandardRules()
                self.board = self.rule_set.starting_board

        def move(self, start_row, start_col, end_row, end_col):
                if self.rule_set.invalid_move(self.board, start_row, start_col, end_row, end_col):
                        raise ValueError("Invalid Move")
                piece_to_move = self.board[start_row][start_col]
                self.board[start_row][start_col] = "-"
                self.board[end_row][end_col] = piece_to_move


