import chessboard
import pawn
import knight
import pytest


@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board


class TestKnightAllowedMoves:
        def test_white_knight_left_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(7,1,5,0)
                assert isinstance(test_board.board[5][0], knight.Knight)
                assert test_board.board[5][0].colour == "White"
                assert test_board.board[7][1] == ("-")
                
        def test_white_knight_left_can_move_forward_right(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(7,1,5,2)
                assert isinstance(test_board.board[5][2], knight.Knight)
                assert test_board.board[5][2].colour == "White"
                assert test_board.board[7][1] == ("-")