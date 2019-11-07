import pytest
import sp_knight

test_sp_knight_b = sp_knight.SpKnight("Black")
test_sp_knight_w = sp_knight.SpKnight("White")

class TestSpKnight:
        def test_sp_knight_name(self):
            assert test_sp_knight_b.name == "Knight"
            assert test_sp_knight_w.name == "Knight"

        def test_sp_knight_symbol(self):
            assert test_sp_knight_b.symbol == '♞'
            assert test_sp_knight_w.symbol == '♘'
            
        def test_sp_knight_value(self):
            assert test_sp_knight_b.value == -30
            assert test_sp_knight_w.value == 30
            
        