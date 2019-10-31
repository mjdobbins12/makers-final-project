import pytest
from piece import Piece
from chessboard import ChessBoard
from king import King

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = ChessBoard()
        return test_board

class TestKingInCheck:
        def test_king_is_in_correct_place(self, run_before_tests):
                test_board = run_before_tests
                assert isinstance(test_board.board[0][4], King)

        def test_starting_king_not_in_check(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[0][4].in_check() == False