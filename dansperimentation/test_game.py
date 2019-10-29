import pytest
import game

test_game = game.Game()

class TestGame:
        def test_game_to_have_board_init(self):
                assert test_game.board.show_board() == [
                ["R","N","B","K","Q","B","N","R"],
                ['p','p','p','p','p','p','p','p'],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ['p','p','p','p','p','p','p','p'],
                ["R","N","B","Q","K","B","N","R"]
                ]

        def test_game_to_have_player_1_start(self):
            assert test_game.p1_turn == True

        def test_get_names(self):
            input = ['Batman', 'Superman']
            test_game.input = lambda x: input.pop(0)
            test_game.get_names()
            assert test_game.p1_name == 'Batman'
            assert test_game.p2_name == 'Superman'

        def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
            game.Game.input = input
