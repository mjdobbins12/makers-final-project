import pawn
import bishop
import rook
import piece
import knight
import king
import queen
import turn

import standard_rules

import many_queens_ruleset

class ChessBoard:
        def __init__(self):
                self.rule_set = many_queens_ruleset.ManyQueens()
                self.board = self.rule_set.starting_board

<<<<<<< HEAD
        def move(self, start_row, start_col, end_row, end_col):
                if self.rule_set.invalid_move(self.board, start_row, start_col, end_row, end_col):
                        raise ValueError("Invalid Move")
                piece_to_move = self.board[start_row][start_col]
                self.board[start_row][start_col] = "-"
                self.board[end_row][end_col] = piece_to_move


=======
# these just pass through for testing purposes - do not reference these in new tests !!!!!!

        def move(self, start_row, start_col, end_row, end_col):
                turn.Turn(self).move(start_row, start_col, end_row, end_col)
>>>>>>> bc256f317fd210353c0449d87f3bdfe2a76f7936
