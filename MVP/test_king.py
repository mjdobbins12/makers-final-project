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

# class TestKingProperties:
#     def test_king_name(self):
#         assert test_king_b.name == "King"
#         assert test_king_w.name == "King"

#     def test_king_symbol(self):
#         assert test_king_b.symbol == "♚"
#         assert test_king_w.symbol == "♔"

#     def test_king_counter(self):
#         assert test_king_b.counter == 0
#         assert test_king_w.counter == 0

# class TestKingMovement:
#     def test_king_can_move_up(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,4,4,3,4) == False

#     def test_king_can_move_down(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,4,4,5,4) == False

#     def test_king_can_move_sideways(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,4,4,4,5) == False

#     def test_king_can_move_diagonally(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,4,4,3,3) == False

#     def test_king_cannot_move_two_squares_laterally(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,4,4,4,2) == True

#     def test_king_cannot_move_two_squares_vertically(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,3,4,5,4) == True

#     def test_king_cannot_move_two_squares_diagonally(self, board_before_tests):
#         test_board = board_before_tests
#         assert test_king_b.illegal_directions(test_board.board,4,4,2,2) == True

class TestCastling:

    def test_king_can_castle_if_it_and_rook_havent_moved(self, board_before_tests):
        test_board = board_before_tests
        test_board.move(6,6,5,6)
        test_board.move(1,0,3,0)
        test_board.move(7,5,6,6)
        test_board.move(1,1,3,1)
        test_board.move(7,6,5,5)
        test_board.move(1,2,3,2)
        test_board.move(7,4,7,6)
        assert isinstance(test_board.board[7][6], king.King)
        assert isinstance(test_board.board[7][5], rook.Rook)
        assert test_board.board[7][4] == '-'
        assert test_board.board[7][7] == '-'

    def test_castling_forbidden_if_king_has_moved(self, board_before_tests):
        test_board = board_before_tests
        test_board.move(6,6,5,6)
        test_board.move(1,0,3,0)
        test_board.move(7,5,6,6)
        test_board.move(1,1,3,1)
        test_board.move(7,6,5,5)
        test_board.move(1,2,3,2)
        test_board.move(7,4,7,5)
        test_board.move(1,3,3,3)
        test_board.move(7,5,7,4)
        test_board.move(1,4,3,4)
        with pytest.raises(ValueError, match=r"Invalid Move"):
                    test_board.move(7,4,7,6)

    def test_castling_forbidden_if_rook_has_moved(self, board_before_tests):
        test_board = board_before_tests
        test_board.move(6,6,5,6)
        test_board.move(1,0,3,0)
        test_board.move(7,5,6,6)
        test_board.move(1,1,3,1)
        test_board.move(7,6,5,5)
        test_board.move(1,2,3,2)
        test_board.move(7,7,7,6)
        test_board.move(1,3,3,3)
        test_board.move(7,6,7,7)
        test_board.move(1,4,3,4)
        with pytest.raises(ValueError, match=r"Invalid Move"):
                    test_board.move(7,4,7,6)

    def test_king_cant_castle_over_other_piece(self, board_before_tests):
        test_board = board_before_tests
        test_board.move(7,6,5,5)
        with pytest.raises(ValueError, match=r"Invalid Move"):
                    test_board.move(7,4,7,6)

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
        with pytest.raises(ValueError, match=r"Invalid Move"):
                    test_game.execute_turn(2,5,3,6)

    def test_kings_cant_be_adjacent2(self, game_before_tests):
        test_game = game_before_tests
        test_game.execute_turn(6,4,4,4)
        test_game.execute_turn(1,4,3,4)
        test_game.execute_turn(7,4,6,4)
        test_game.execute_turn(0,4,1,4)
        test_game.execute_turn(6,4,5,3)
        test_game.execute_turn(1,4,2,3)
        test_game.execute_turn(5,3,4,2)
        with pytest.raises(ValueError, match=r"Invalid Move"):
                    test_game.execute_turn(2,3,3,2)

        

