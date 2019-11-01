import pytest
from piece import Piece
import chessboard
import king
import rook
import game

@pytest.fixture(autouse=True)
def board_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board

@pytest.fixture(autouse=True)   
def game_before_tests():
        test_game = game.Game("p1", "p2")
        return test_game

test_king_b = king.King("Black")
test_king_w = king.King("White")

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

class TestCastling:

    def test_king_can_castle_if_it_and_rook_havent_moved(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(6,6,5,6)
        test_game.execute_turn(1,0,3,0)
        test_game.execute_turn(7,5,6,6)
        test_game.execute_turn(1,1,3,1)
        test_game.execute_turn(7,6,5,5)
        test_game.execute_turn(1,2,3,2)
        test_game.execute_turn(7,4,7,6)
        assert isinstance(test_game.board.board[7][6], king.King)
        assert isinstance(test_game.board.board[7][5], rook.Rook)
        assert test_game.board.board[7][4] == '-'
        assert test_game.board.board[7][7] == '-'

    def test_castling_forbidden_if_king_has_moved(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(6,6,5,6)
        test_game.execute_turn(1,0,3,0)
        test_game.execute_turn(7,5,6,6)
        test_game.execute_turn(1,1,3,1)
        test_game.execute_turn(7,6,5,5)
        test_game.execute_turn(1,2,3,2)
        test_game.execute_turn(7,4,7,5)
        test_game.execute_turn(1,3,3,3)
        test_game.execute_turn(7,5,7,4)
        test_game.execute_turn(1,4,3,4)
        
        assert test_game.execute_turn(7,4,7,6) == 'invalid move'

    def test_castling_forbidden_if_rook_has_moved(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(6,6,5,6)
        test_game.execute_turn(1,0,3,0)
        test_game.execute_turn(7,5,6,6)
        test_game.execute_turn(1,1,3,1)
        test_game.execute_turn(7,6,5,5)
        test_game.execute_turn(1,2,3,2)
        test_game.execute_turn(7,7,7,6)
        test_game.execute_turn(1,3,3,3)
        test_game.execute_turn(7,6,7,7)
        test_game.execute_turn(1,4,3,4)
        assert test_game.execute_turn(7,4,7,6)  == 'invalid move'

    def test_king_cant_castle_over_other_piece(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(7,6,5,5)
        assert test_game.execute_turn(7,4,7,6)  == 'invalid move'

class TestKingsCantBeAdjacent:
    def test_kings_cant_be_adjacent(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(6,4,4,4)
        test_game.execute_turn(1,4,3,4)
        test_game.execute_turn(7,4,6,4)
        test_game.execute_turn(0,4,1,4)
        test_game.execute_turn(6,4,5,5)
        test_game.execute_turn(1,4,2,5)
        test_game.execute_turn(5,5,4,6)
        assert test_game.execute_turn(2,5,3,6) == 'invalid move'

    def test_kings_cant_be_adjacent2(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(6,4,4,4)
        test_game.execute_turn(1,4,3,4)
        test_game.execute_turn(7,4,6,4)
        test_game.execute_turn(0,4,1,4)
        test_game.execute_turn(6,4,5,3)
        test_game.execute_turn(1,4,2,3)
        test_game.execute_turn(5,3,4,2)
        assert test_game.execute_turn(2,3,3,2) == 'invalid move'

        

