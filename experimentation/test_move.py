import move
import pytest

board = move.Board()

class TestMove:
    def test_move(self):
        board.move(0,0,2,2)
        assert board.show_board() == [
    		['B','B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B','B'],
            ['B','B','*','B','B','B','B','B'],
            ['B','B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B','B'],
    		['B','B','B','B','B','B','B','B']
            ]

    def test_blocking(self):
        with pytest.raises(Exception) as excinfo:
            board.grid[1][1] = '+'
            board.move(0,0,1,1)
        assert "Invalid move" in str(excinfo.value)
