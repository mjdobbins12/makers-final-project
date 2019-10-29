import move
import pytest

board = move.Board()
board1 = move.Board()

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
            board1.grid[1][1] = '+'
            board1.move(0,0,1,1)
        assert "Invalid move" in str(excinfo.value)

    def test_cannot_jump(self):
        with pytest.raises(Exception) as excinfo:
            board1.grid[0][1] = '+'
            board1.move(0,0,0,2)
        assert "Invalid move" in str(excinfo.value)
