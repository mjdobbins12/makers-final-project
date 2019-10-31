import pytest
from piece import Piece
from chessboard import ChessBoard
from king import King

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = ChessBoard()
        return test_board

class TestKingInCheck:
        def test_king_is_not_in_checkmate(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[0][4].is_checkmate(test_board.board, 0, 4) == False

        def test_is_checkmate(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,5,5,5)
                test_board.move(1,4,3,4)
                test_board.move(6,6,4,6)
                test_board.move(0,3,4,7)
                assert test_board.board[0][4].is_checkmate(test_board.board, 7, 4) == True