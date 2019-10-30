import pytest
import game
import pawn

test_game = game.Game('test1', 'test2')

class TestGame:

        def test_game_to_have_player_1_start(self):
            assert test_game.p1_turn == True

        # def test_get_names(self):
        #     input = ['Batman', 'Superman']
        #     game.ui.input = lambda x: input.pop(0)
        #     test_game = game.Game()
        #     test_game.ui.get_names()
        #     assert test_game.p1_name == 'Batman'
        #     assert test_game.p2_name == 'Superman'
        # test needs to be brought into UI test

        def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
            game.Game.input = input
