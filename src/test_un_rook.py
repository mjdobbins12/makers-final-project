import pytest
from piece import Piece
from un_rook import UnRook


test_rook_b = UnRook("Black")
test_rook_w = UnRook("White")

class TestRookProperties:

	def test_rook_name(self):
		assert test_rook_b.name == "Rook"
		assert test_rook_w.name == "Rook"
		
	def test_rook_symbol(self):
		assert test_rook_b.symbol == '♜'
		assert test_rook_w.symbol == '♖'

class TestIllegalMoves:

	def test_un_rook_cannot_move_diagonally(self):
		assert test_rook_b.invalid_move_types(5, 5, 4, 4) == True

	def test_un_rook_cannot_move_laterally(self):
		assert test_rook_b.invalid_move_types(5, 5, 5, 6) == True


