import pytest
import rook

test_rook_b = rook.Rook("Black")
test_rook_w = rook.Rook("White")

class TestRookProperties:

	def test_rook_name(self):
		assert test_rook_b.name == "Rook"
		assert test_rook_w.name == "Rook"
		
	def test_rook_symbol(self):
		assert test_rook_b.symbol == '♜'
		assert test_rook_w.symbol == '♖'