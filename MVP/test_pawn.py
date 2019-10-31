import pytest
import pawn
from piece import Piece
import chessboard


test_pawn_b = pawn.Pawn("Black")
test_pawn_w = pawn.Pawn("White")

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board

class TestpawnProperties:

    def test_pawn_name(self):
      assert test_pawn_b.name == "Pawn"
      assert test_pawn_w.name == "Pawn"
      
    def test_pawn_symbol(self):
      assert test_pawn_b.symbol == '♟'
      assert test_pawn_w.symbol == "♙"

class TestIllegalMoves:

    def test_pawn_cannot_move_backwards(self):
      assert test_pawn_b.invalid_move_types(1, 0, 0, 0) == True
      assert test_pawn_w.invalid_move_types(6, 2, 7, 2) == True

    def test_pawn_cannot_move_laterally(self):
      assert test_pawn_b.invalid_move_types(5, 5, 5, 6) == True

    def test_pawn_cannot_move_more_than_2_spaces(self):
      assert test_pawn_b.invalid_move_types(1, 0, 4, 0) == True

    def test_pawn_cannot_move_more_than_1_space_after_first_move(self):
      assert test_pawn_b.invalid_move_types(3, 0, 5, 0) == True

    def test_pawn_cannot_move_more_than_1_space_after_first_move(self):
      assert test_pawn_b.invalid_move_types(3, 0, 5, 0) == True

    def test_pawn_cannot_move_diagonally_more_than_1_space(self):
      assert test_pawn_b.invalid_move_types(3, 1, 5, 3) == True

    def test_pawn_cannot_move_a_knight_move(self):
      assert test_pawn_b.invalid_move_types(3, 1, 5, 2) == True

class TestAvailableMoves:
    
    def test_available_moves_is_array_of_allowed_moves(self, run_before_tests):
      test_board = run_before_tests
      assert test_board.board[6][6].available_moves(test_board.board,6,6) == [[4,6],[5,6]]