import pytest
from piece import Piece
from chessboard import ChessBoard
from king import King
from game import Game

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = Game("p1", "p2")
        test_board = ChessBoard()
        return test_game

class TestKingInCheck:

        def test_starting_king_not_in_check(self, run_before_tests):
                test_game = run_before_tests
                assert test_game.in_check(test_game.board.board) == False
        
        def test_king_can_be_in_check(self, run_before_tests):
                test_game = run_before_tests
                test_game.board.move(6,3,4,3)
                test_game.board.move(1,2,2,2)
                test_game.board.move(6,7,4,7)
                test_game.board.move(0,3,3,0)
                assert test_game.in_check(test_game.board.board) == True