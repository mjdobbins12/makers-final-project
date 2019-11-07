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
                test_game.execute_turn(6,4,4,4)
                test_game.execute_turn(1,0,3,0)
                test_game.execute_turn(4,4,3,4)
                render = board_render.BoardRender(test_game)
                draw_board = render.draw_board()
                