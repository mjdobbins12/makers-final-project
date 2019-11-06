import pytest
import piece
import game
import pawn
import bishop 
import ex_bishops_mock
import standard_rules

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = game.Game('p1', 'p2', ruleset = ex_bishops_mock.ExBishopsMock())
        return test_game

class TestExBishop:
        def test_ruleset_inherits_from_standard_rules(self):
                test_ruleset = ex_bishops_mock.ExBishopsMock()
                assert isinstance(test_ruleset, standard_rules.StandardRules)

        def test_generates_random_trigger(self):
                test_ruleset = ex_bishops_mock.ExBishopsMock()
                assert isinstance(test_ruleset.first_trigger, int)
                
        def test_excommunication_of_bishops(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,0,5,0)
                assert isinstance(test_game.board[7][2], bishop.Bishop)
                print(test_game.board)
                test_game.execute_turn(1,0,2,0)
                test_game.execute_turn(6,1,5,1)
                test_game.execute_turn(1,1,2,1)
                assert test_game.board[7][2] == '-'
         