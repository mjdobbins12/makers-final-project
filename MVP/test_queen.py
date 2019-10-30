import pytest
from piece import Piece
import queen

test_queen_b = queen.Queen("Black")
test_queen_w = queen.Queen("White")


class TestQueenProperties:

        def test_queen_name(self):
          assert test_queen_b.name == "Queen"
          assert test_queen_w.name == "Queen"

        def test_queen_symbol(self):
          assert test_queen_b.symbol == '♛'
          assert test_queen_w.symbol == '♕'


class TestLegalMoves:

        def test_queen_cannot_move_diagonally(self):
          assert test_queen_b.invalid_move_types(5, 5, 4, 4) == False

        def test_queen_can_move_laterally(self):
          assert test_queen_b.invalid_move_types(5, 5, 5, 6) == False

        def test_queen_cant_move_like_knight(self):
          assert test_queen_b.invalid_move_types(5,5,7,4) == True
