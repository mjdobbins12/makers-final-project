import pytest
import game
import pawn

test_game = game.Game('test1', 'test2')

class TestGame:

        def test_game_to_have_player_1_start(self):
            assert test_game.p1_turn == True

        
