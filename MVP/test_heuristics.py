import game
import heuristics
import pytest

@pytest.fixture(autouse=True)
def run_before_tests():
        new_game = game.Game('p1', 'p2', ) 
        return new_game

class TestOutputHeuristics:
        def test_returns_an_integer(self, run_before_tests):
                test_game = run_before_tests
                new_heuristic = heuristics.Heuristics(test_game)
                assert isinstance(new_heuristic.evaluate(new_heuristic.game), int)

        def  test_heuristics_of_starting_board(self, run_before_tests):
                test_game = run_before_tests
                new_heuristic2 = heuristics.Heuristics(test_game)
