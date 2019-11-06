
import pytest
import piece
import game
import pawn
import bishop 
import ex_bishops
import ex_bishops_mock
import standard_rules
import un_rook
import rook
import knight
import sp_knight

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = game.Game('p1', 'p2')
        test_game.ruleset = ex_bishops.ExBishops()
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
                test_game.execute_turn(1,0,2,0)
                test_game.execute_turn(6,1,5,1)
                test_game.execute_turn(1,1,2,1)
                assert test_game.board[7][2] == '-'
                
        def test_initial_sale_of_rooks(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,0,5,0)
                test_game.execute_turn(1,0,2,0)
                test_game.execute_turn(6,1,5,1)
                test_game.execute_turn(1,1,2,1)
                test_game.execute_turn(6,2,5,2)
                test_game.execute_turn(1,2,2,2) 
                test_game.execute_turn(6,3,5,3)
                assert isinstance(test_game.board[7][0], un_rook.UnRook)
                
        def test_complete_sale_of_rooks(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,0,5,0)
                test_game.execute_turn(1,0,2,0)
                test_game.execute_turn(6,1,5,1)
                test_game.execute_turn(1,1,2,1)
                test_game.execute_turn(6,2,5,2)
                test_game.execute_turn(1,2,2,2) 
                test_game.execute_turn(6,3,5,3)
                test_game.execute_turn(1,3,2,3) 
                assert isinstance(test_game.board[7][0], rook.Rook)
                
        def test_honour_for_knights(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,0,5,0)
                test_game.execute_turn(1,0,2,0)
                test_game.execute_turn(6,1,5,1)
                test_game.execute_turn(1,1,2,1)
                test_game.execute_turn(6,2,5,2)
                test_game.execute_turn(1,2,2,2) 
                test_game.execute_turn(6,3,5,3)
                test_game.execute_turn(1,3,2,3) 
                test_game.execute_turn(6,4,5,4)
                test_game.execute_turn(1,4,2,4) 
                assert isinstance(test_game.board[7][1], sp_knight.SpKnight)
                
        def test_knights_back_to_normal(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,0,5,0)
                test_game.execute_turn(1,0,2,0)
                test_game.execute_turn(6,1,5,1)
                test_game.execute_turn(1,1,2,1)
                test_game.execute_turn(6,2,5,2)
                test_game.execute_turn(1,2,2,2) 
                test_game.execute_turn(6,3,5,3)
                test_game.execute_turn(1,3,2,3) 
                test_game.execute_turn(6,4,5,4)
                test_game.execute_turn(1,4,2,4) 
                assert isinstance(test_game.board[7][1], sp_knight.SpKnight)
                test_game.execute_turn(6,5,5,5)
                test_game.execute_turn(1,5,2,5)
                assert isinstance(test_game.board[7][1], knight.Knight)

      

