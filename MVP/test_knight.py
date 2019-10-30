import chessboard
import pawn
import knight
import pytest


@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board


class TestKnightAllowedMoves:
        def test_black_knight_left_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(7,1,5,0)
                assert isinstance(test_board.board[5][0], knight.Knight)
                assert test_board.board[5][1].colour == "Black"
                assert test_board.board[7][1] == ("-")