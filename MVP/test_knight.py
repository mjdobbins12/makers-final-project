import chessboard
import pawn
import knight
import pytest


@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board


class TestKnightightFirstStandardMoves:
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
                
        def test_white_knight_right_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(7,6,5,5)
                assert isinstance(test_board.board[5][5], knight.Knight)
                assert test_board.board[5][5].colour == "White"
                assert test_board.board[7][6] == ("-")
                
        def test_white_knight_right_can_move_forward_right(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(7,6,5,7)
                assert isinstance(test_board.board[5][7], knight.Knight)
                assert test_board.board[5][7].colour == "White"
                assert test_board.board[7][6] == ("-")
                
        def test_black_knight_left_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(0,1,2,0)
                assert isinstance(test_board.board[2][0], knight.Knight)
                assert test_board.board[2][0].colour == "Black"
                assert test_board.board[0][1] == ("-")
                
        def test_black_knight_left_can_move_forward_right(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(0,1,2,2)
                assert isinstance(test_board.board[2][2], knight.Knight)
                assert test_board.board[2][2].colour == "Black"
                assert test_board.board[0][1] == ("-")
                
        def test_black_knight_right_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(0,6,2,5)
                assert isinstance(test_board.board[2][5], knight.Knight)
                assert test_board.board[2][5].colour == "Black"
                assert test_board.board[0][6] == ("-")
                
        def test_black_knight_right_can_move_forward_right(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(0,6,2,7)
                assert isinstance(test_board.board[2][7], knight.Knight)
                assert test_board.board[2][7].colour == "Black"
                assert test_board.board[0][6] == ("-")