import pytest
from piece import Piece
import chessboard
import king
import rook

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

    def test_king_counter(self):
        assert test_king_b.counter == 0
        assert test_king_w.counter == 0

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
        assert test_king_b.illegal_directions(board.board,4,4,4,2) == True

    def test_king_cannot_move_two_squares_vertically(self):
        assert test_king_b.illegal_directions(board.board,3,4,5,4) == True

    def test_king_cannot_move_two_squares_diagonally(self):
        assert test_king_b.illegal_directions(board.board,4,4,2,2) == True

class TestCastling:

    def test_king_can_castle_if_it_and_rook_havent_moved(self):
        board.move(6,6,5,6)
        board.move(1,0,3,0)
        board.move(7,5,6,6)
        board.move(1,1,3,1)
        board.move(7,6,5,5)
        board.move(1,2,3,2)
        board.move(7,4,7,6)
        assert isinstance(board.board[7][6], king.King)
        assert isinstance(board.board[7][5], rook.Rook)
        print(board.board[7][7])
        assert board.board[7][4] == '-'
        assert board.board[7][7] == '-'
