from checkmate import Checkmate
from draw import Draw
from king import King
import many_queens
from ex_bishops import ExBishops
from piece import Piece
import player
import standard_rules
import random_pieces

import turn

class Game:

    def __init__(self, p1_name, p2_name, ruleset = "none"):

        if ruleset == "many_queens":
            self.ruleset = many_queens.ManyQueens()
        elif ruleset == "random_pieces":
            self.ruleset = random_pieces.RandomPieces()
        elif ruleset == "ex_bishops":
            self.ruleset = ExBishops()
        else:
            self.ruleset = standard_rules.StandardRules()

        self.board = self.ruleset.starting_board
        self.player_1 = player.Player(p1_name, "White")
        self.player_2 = player.Player(p2_name, "Black")
        self.p1_turn = True
        self.log = []

    def execute_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        try:
            self.check_player_owns_piece(int(turn_from_x), int(turn_from_y))
            response = turn.Turn(self.ruleset, self.board, self.log, self.player_1, self.player_2).move(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.log_turn(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.p1_turn = not self.p1_turn
            if response == 'excommunication':
                return 'excommunication'
            elif response == 'rooksale':
                return "rooksale"
            elif response == 'rooksign':
                return "rooksign"
            elif response == 'knight_honour':
                return 'knight_honour'
            elif response == 'knight_normal':
                return 'knight_normal'
            else:
                return 'valid move'
        except:
            return 'invalid move'

    def revert_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y, original_object, target_object):
        self.board[turn_from_x][turn_from_y] = original_object
        self.board[turn_to_x][turn_to_y] = target_object
        self.p1_turn = not self.p1_turn

    def get_original_pieces(self, board, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        original_square = board[turn_from_x][turn_from_y]
        moved_to = board[turn_to_x][turn_to_y]
        return [original_square, moved_to]

    def is_checkmate(self):
        if Checkmate(self).is_checkmate():
            return True
        else:
            return False

    def is_draw(self):
        if Draw(self).is_draw():
            return True
        else:
            return False

    def log_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        colour = 'White' if self.p1_turn else 'Black'
        self.log.append([colour, turn_from_x, turn_from_y, turn_to_x, turn_to_y])

    def check_player_owns_piece(self, x, y):
        colour = 'White' if self.p1_turn else 'Black'
        if self.board[x][y].colour != colour:
            raise ValueError("PlayerDoesNotOwnPiece")

    def check_if_self_in_check(self, start_row, start_col, end_row, end_col):
        turn.Turn(self.ruleset, self.board, self.log, self.player_1, self.player_2).check_if_self_in_check(start_row, start_col, end_row, end_col)
