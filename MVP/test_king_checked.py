import pytest
from piece import Piece
from chessboard import ChessBoard
from king import King

test_king_w = King("White")


@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = ChessBoard()
        return test_board

class TestKingInCheck:
        def test_king_is_not_in_check(self, run_before_tests):
                test_board = run_before_tests
                assert isinstance(test_board.board[0][4], King)