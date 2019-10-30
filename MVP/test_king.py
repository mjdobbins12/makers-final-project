import pytest
from piece import Piece
import chessboard
import king

test_king_b = king.King("Black")
test_king_w = king.King("White")
board = chessboard.ChessBoard()

class TestKingProperties:
    def test_king_name(self):
        assert test_king_b.name == "King"
        assert test_king_w.name == "King"

    def test_king_symbol(self):
        assert test_king_b.symbol == "♚"
        assert test_king_w.symbol == "♔"

class TestKingMovement:
    def test_king_can_move_up(self):
        assert test_king_b.illegal_directions(board.board,4,4,3,4) == False

    def test_king_can_move_down(self):
        assert test_king_b.illegal_directions(board.board,4,4,5,4) == False

    def test_king_can_move_sideways(self):
        assert test_king_b.illegal_directions(board.board,4,4,4,5) == False

    def test_king_can_move_diagonally(self):
        assert test_king_b.illegal_directions(board.board,4,4,3,3) == False

    def test_king_cannot_move_two_squares_laterally(self):
        assert test_king_b.illegal_directions(board.board,4,4,2,4) == True

    def test_king_cannot_move_two_squares_vertically(self):
        assert test_king_b.illegal_directions(board.board,3,4,5,4) == True

    def test_king_cannot_move_two_squares_diagonally(self):
        assert test_king_b.illegal_directions(board.board,4,4,2,2) == True
