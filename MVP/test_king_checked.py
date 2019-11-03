import pytest
from piece import Piece
from king import King
from game import Game

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = Game("p1", "p2")
        return test_game

class TestKingInCheck:

        def test_starting_king_not_in_check(self, run_before_tests):
                test_game = run_before_tests
                assert test_game.board.board[0][4].in_check(test_game.board.board, 0, 4) == False

        def test_king_not_in_check_from_own_pieces(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,4,4,4)
                test_game.execute_turn(1,4,3,4)
                test_game.execute_turn(7,4,6,4)
                test_game.execute_turn(0,4,1,4)
                test_game.execute_turn(6,4,5,4)
                assert test_game.board.board[5][4].in_check(test_game.board.board, 5, 4) == False
        
        def test_king_can_be_in_check(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6,3,4,3)
                test_game.execute_turn(1,2,2,2)
                test_game.execute_turn(6,7,4,7)
                test_game.execute_turn(0,3,3,0)
                assert test_game.board.board[7][4].in_check(test_game.board.board, 7, 4) == True 