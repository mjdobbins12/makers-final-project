import pytest
import ui
import pawn

class TestUI:

        def test_get_names(self):
            input = ['Batman', 'Superman']
            ui.input = lambda x: input.pop(0)
            test_ui = ui.UI()
            output = test_ui.get_names()
            assert output[0] == 'Batman'
            assert output[1] == 'Superman'

        def test_feature_move_2_pawns_and_strike(self):
            input = ['Batman', 'Superman', 'a2', 'a4', 'b7', 'b5', 'a4', 'b5', 'quit']
            ui.input = lambda x: input.pop(0)
            test_ui = ui.UI()
            test_ui.start()
            assert test_ui.game.board[3][1].colour == 'White'
            assert isinstance(test_ui.game.board[3][1], pawn.Pawn)


        def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
            ui.input = input
