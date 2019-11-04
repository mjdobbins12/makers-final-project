import game
import minimax
import pytest

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = game.Game('p1', 'p2')
        return test_game

class TestInputOutput:
        def test_accepts_two_args(self, run_before_tests):
                test_game = run_before_tests
                new_minimax = minimax.Minimax(test_game, test_game.p1_turn)
