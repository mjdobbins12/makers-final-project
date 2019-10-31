import pytest
from piece import Piece
import chessboard
from king import King

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board

class TestCheckmate:

        def test_king_is_not_in_checkmate(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[0][4].is_checkmate(test_board.board, 0, 4) == False

        # fool's mate
        def test_fools_mate_is_checkmate(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,5,5,5)
                test_board.move(1,4,3,4)
                test_board.move(6,6,4,6)
                test_board.move(0,3,4,7)
                assert test_board.board[7][4].is_checkmate(test_board.board, 7, 4) == True

        # scholar's mate
        def test_scholars_mate_is_checkmate(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,4,4,4)
                test_board.move(1,4,3,4)
                test_board.move(7,5,4,2)
                test_board.move(1,0,2,0)
                test_board.move(7,3,5,5)
                test_board.move(2,0,3,0)
                test_board.move(5,5,1,5)
                assert test_board.board[0][4].is_checkmate(test_board.board, 0, 4) == True