from piece import Piece
import pytest
import game
import pawn

test_game = game.Game('test1', 'test2')

class TestGame:

        def test_game_to_have_player_1_start(self):
            assert test_game.p1_turn == True


        def test_game_moves_to_log(self):
            test_game.execute_turn('6', '0', '4', '0')
            test_game.execute_turn('1', '7', '3', '7')
            assert test_game.log[0] == ['White', 6, 0, 4, 0]
            assert test_game.log[1] == ['Black', 1, 7, 3, 7]

        def test_move_other_player_figure_prohibited(self):
            assert test_game.p1_turn == True
            assert test_game.execute_turn('1', '6', '3', '6') == 'invalid move'
