import pytest
from piece import Piece
import chessboard
import king

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board

class TestAvailableMoves:
        def test_pawn_has_only_2_available_start_moves(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[6][0].available_moves(test_board.board, 6, 0) == [[4,0],[5,0]]

        def test_knight_has_only_2_available_start_moves(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[0][1].available_moves(test_board.board, 0, 1) == [[2,0],[2,2]]

        def test_Queen_has_only_2_available_moves_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6, 3, 4, 3)
                test_board.move(1, 5, 3, 5)
                assert test_board.board[7][3].available_moves(test_board.board, 7, 3) == [[5,3],[6,3]]

        def test_Queen_has_only_4_available_moves_diagonally(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6, 4, 4, 4)
                test_board.move(1, 5, 3, 5)
                assert test_board.board[7][3].available_moves(test_board.board, 7, 3) == [[6,4],[5,5],[4,6],[3,7]]