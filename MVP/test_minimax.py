import game
import minimax
import pytest

game = game.Game('p1', 'p2')

@pytest.fixture(autouse=True)
def run_before_tests():        
        test_minimax = minimax.Minimax(game, game.p1_turn)
        return test_minimax

class TestInputOutput:
        def test_accepts_two_args(self, run_before_tests):
                test_minimax = run_before_tests
                new_minimax = minimax.Minimax(test_minimax.game, test_minimax.game.p1_turn)

        def test_outputs_a_move(self, run_before_tests):
                test_minimax = run_before_tests
                test_minimax.game.execute_turn(6, 4, 4, 4)
                assert isinstance(test_minimax.execute_turn(), list)


