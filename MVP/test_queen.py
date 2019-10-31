import pytest
from piece import Piece
import queen
from chessboard import ChessBoard

test_queen_b = queen.Queen("Black")
test_queen_w = queen.Queen("White")

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = ChessBoard()
        return test_board

class TestQueenProperties:

        def test_queen_name(self):
          assert test_queen_b.name == "Queen"
          assert test_queen_w.name == "Queen"

        def test_queen_symbol(self):
          assert test_queen_b.symbol == '♛'
          assert test_queen_w.symbol == '♕'


class TestLegalMoves:

        def test_queen_can_move_diagonally(self):
          assert test_queen_b.invalid_move_types(5, 5, 4, 4) == False

        def test_queen_can_move_laterally(self):
          assert test_queen_b.invalid_move_types(5, 5, 5, 6) == False

        def test_queen_cant_move_like_knight(self):
          assert test_queen_b.invalid_move_types(5,5,7,4) == True

class TestQueenTaking:

        def test_queen_can_take_diagonally(self, run_before_tests):
          test_board = run_before_tests
          test_board.move(6,4,4,4)
          test_board.move(1,6,3,6)
          test_board.move(6,0,4,0)
          test_board.move(3,6,4,6)
          test_board.move(7,3,4,6)

        def test_queen_can_take_diagonally(self, run_before_tests):
          test_board = run_before_tests
          test_board.move(6,3,4,3)
          test_board.move(1,5,3,5)
          test_board.move(7,3,5,3)
          test_board.move(1,0,3,0)
          test_board.move(5,3,3,5)

        def test_queen_cant_move_if_blocked_forward(self, run_before_tests):
          test_board = run_before_tests
          test_board.move(6,3,4,3)
          test_board.move(1,5,3,5)
          with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(7,3,3,3)

        def test_queen_cant_move_if_blocked(self, run_before_tests):
          test_board = run_before_tests
          with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(7,3,4,0)

        def test_queen_cant_jump(self, run_before_tests):
          test_board = run_before_tests
          with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(7,3,5,1)
