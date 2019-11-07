import pytest
import game
import board_render
from standard_rules import StandardRules

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = game.Game('p1', 'p2', ruleset = StandardRules())
        return test_game

class TestBoardRender:
        
        def test_can_init_no_dramas(self, run_before_tests):
                test_game = run_before_tests
                render = board_render.BoardRender(test_game)
                draw_board = render.draw_board()
                assert draw_board == 2
                