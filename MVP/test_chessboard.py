import chessboard
import pawn
import bishop
import pytest
import queen
from piece import Piece

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board

class TestStartingBoard:
        def test_board_displayed(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board == test_board.board

class TestPawnAllowedMoves:
        def test_black_pawn_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,5,1)
                assert isinstance(test_board.board[5][1], pawn.Pawn)
                assert test_board.board[5][1].colour == "White"
                assert test_board.board[6][1] == ("-")

        def test_white_pawn_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,2,2)
                assert isinstance(test_board.board[2][2], pawn.Pawn)
                assert test_board.board[2][2].colour == "Black"
                assert test_board.board[1][2] == ('-')

        def test_black_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                assert isinstance(test_board.board[4][1], pawn.Pawn)
                assert test_board.board[4][1].colour == "White"
                assert test_board.board[6][1] == ("-")

        def test_white_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,3,2)
                assert isinstance(test_board.board[3][2], pawn.Pawn)
                assert test_board.board[3][2].colour == "Black"
                assert test_board.board[1][2] == ('-')

        def test_black_pawn_can_move_1_further_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                test_board.move(4,1,3,1)
                assert isinstance(test_board.board[3][1], pawn.Pawn)
                assert test_board.board[3][1].colour == "White"
                assert test_board.board[4][1] == ("-")

        def test_white_pawn_can_move_1_further_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,3,2)
                test_board.move(3,2,4,2)
                assert isinstance(test_board.board[4][2], pawn.Pawn)
                assert test_board.board[4][2].colour == "Black"
                assert test_board.board[3][2] == ("-")

        def test_pawn_object_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,6,5,6)
                assert isinstance(test_board.board[5][6], pawn.Pawn)
                assert test_board.board[6][6] == ("-")

class TestPawnStriking:
        def test_black_pawn_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,4,4,4)
                test_board.move(1,5,3,5)
                test_board.move(4,4,3,5)
                assert test_board.board[1][5] == ("-")
                assert test_board.board[6][4] == ("-")
                assert test_board.board[4][4] == ("-")
                assert isinstance(test_board.board[3][5], pawn.Pawn)
                assert test_board.board[3][5].colour == "White"

        def test_white_pawn_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,4,4,4)
                test_board.move(1,5,3,5)
                test_board.move(3,5,4,4)
                assert test_board.board[1][5] == ("-")
                assert test_board.board[6][4] == ("-")
                assert test_board.board[3][5] == ("-")
                assert isinstance(test_board.board[4][4], pawn.Pawn)
                assert test_board.board[4][4].colour == "Black"

        def test_pawn_can_only_move_diagonally_to_strike(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,4,4,4)
                test_board.move(1,0,3,0)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(4,4,3,3)


class TestPieceObjects:
        def test_pawn_objects_are_stored_in_board(self, run_before_tests):
                test_board = run_before_tests
                assert isinstance(test_board.board[6][6], pawn.Pawn)

        def test_pawn_objects_can_have_colour_property(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[6][6].colour == ("White")

        def test_pawn_objects__can_have_colour_property_white(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[1][7].colour == ("Black")

class TestPawnDirection:
        def test_black_pawn_cannot_move_backwards(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,1,7,1)

        def test_white_pawn_cannot_move_backwards(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(1,1,0,1)

        def test_black_pawn_cannot_move_sideways(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,1,6,2)

        def test_white_pawn_cannot_move_sideways(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(1,1,1,2)

        def test_white_pawn_cannot_move_2_spaces_forward_and_sideways(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(1,2,3,3)

class TestBoardBoundaries:
        def test_pawn_cannot_move_outside_rows(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,4,4,4)
                test_board.move(1,5,3,5)
                test_board.move(4,4,3,5)
                test_board.move(1,7,3,7)
                test_board.move(3,5,2,5)
                test_board.move(3,7,4,7)
                test_board.move(2,5,1,5)
                test_board.move(1,0,3,0)
                test_board.move(1,5,0,6)
                test_board.move(3,0,4,0)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(0,5,-1,5)

        def test_pawn_cannot_move_outside_columns(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,7,6,8)

        def test_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                assert isinstance(test_board.board[4][1], pawn.Pawn)
                assert test_board.board[6][1] == ("-")


class TestPawnMoveLength:
        def test_pawn_cannot_move_3_spaces(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,1,3,1)


        def test_pawn_cannot_move_2_spaces_twice(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(4,1,2,1)

        def test_pawn_cannot_strike_2_spaces_away_diagonally(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                test_board.move(1,7,3,7)
                test_board.move(4,1,3,1)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(1,3,3,1)

class TestPawnWhenBlocked:
        def test_pawn_cannot_move_one_space_when_blocked(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,4,4,4)
                test_board.move(1,4,3,4)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(4,4,3,4)

        def test_pawn_cannot_move_jump_over_pawn(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,4,3,4)
                test_board.move(6,0,4,0)
                test_board.move(3,4,4,4)
                test_board.move(4,0,3,0)
                test_board.move(4,4,5,4)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,4,4,4)

class TestBishopAllowedMoves:
        def test_bishop_can_move_one_space_diagonally(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,5,1)
                test_board.move(1,4,3,4)
                test_board.move(7,2,6,1)
                assert isinstance(test_board.board[6][1], bishop.Bishop)
                assert test_board.board[6][1].colour == "White"
                assert test_board.board[7][2] == ("-")

        def test_bishop_can_move_two_spaces_diagonally(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,4,3)
                test_board.move(1,4,3,4)
                test_board.move(7,2,5,4)
                assert isinstance(test_board.board[5][4], bishop.Bishop)
                assert test_board.board[5][4].colour == "White"
                assert test_board.board[7][2] == ("-")

        def test_bishop_can_move_in_different_diagonal_directions(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,5,3)
                test_board.move(1,4,3,4)
                test_board.move(7,2,5,4)
                test_board.move(1,5,3,5)
                test_board.move(5,4,3,2)
                assert isinstance(test_board.board[3][2], bishop.Bishop)
                assert test_board.board[3][2].colour == "White"
                assert test_board.board[5][4] == ("-")

        def test_bishop_can_move_diagonally_backwards(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,5,3)
                test_board.move(1,4,3,4)
                test_board.move(7,2,5,4)
                test_board.move(1,5,3,5)
                test_board.move(5,4,7,2)
                assert isinstance(test_board.board[7][2], bishop.Bishop)
                assert test_board.board[7][2].colour == "White"
                assert test_board.board[5][4] == ("-")

        def test_bishop_cannot_move_if_blocked(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,4,3)
                test_board.move(1,3,3,3)
                test_board.move(7,2,5,4)
                test_board.move(1,4,3,4)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                    test_board.move(5,4,3,2)

class TestRookWhenBlocked:
        def test_rook_cannot_move_jump_over_piece(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,0,4,0)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(7,0,3,0)

        def test_rook_cannot_move_jump_over_piece(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,0,3,0)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(0,0,5,0)


class TestRookCanMoveAsNormal:
        def test_rook_can_move_normally(self, run_before_tests):
                        test_board = run_before_tests
                        test_board.move(6,0,4,0)
                        test_board.move(1,5,3,5)
                        test_board.move(7,0,5,0)

class TestRookTaking:
        def test_rook_can_take_piece_upwards(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,0,4,0)
                test_board.move(1,5,3,5)
                test_board.move(7,0,5,0)
                test_board.move(3,5,4,5)
                test_board.move(5,0,5,5)
                test_board.move(1,7,3,7)
                test_board.move(5,5,4,5)

        def test_rook_can_take_piece_rightwards(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,0,4,0)
                test_board.move(1,5,3,5)
                test_board.move(7,0,5,0)
                test_board.move(3,5,4,5)
                test_board.move(6,7,4,7)
                test_board.move(4,5,5,5)
                test_board.move(5,0,5,5)

        def test_rook_can_take_piece_leftwards(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,7,4,7)
                test_board.move(1,5,3,5)
                test_board.move(7,7,5,7)
                test_board.move(3,5,4,5)
                test_board.move(6,0,4,0)
                test_board.move(4,5,5,5)
                test_board.move(5,7,5,5)


        def test_rook_cannot_take_own_piece(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,0,4,0)
                test_board.move(1,0,3,0)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(7,0,4,0)


class TestQueenMoving:
        def test_queen_can_move_laterally(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6, 3, 4, 3)
                test_board.move(1, 5, 3, 5)
                test_board.move(7, 3, 5, 3)
                test_board.move(3, 5, 4, 5)
                test_board.move(5, 3, 5, 7)

        def test_queen_can_move_diagonally(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6, 3, 4, 3)
                test_board.move(1, 5, 3, 5)
                test_board.move(7, 3, 5, 3)
                test_board.move(3, 5, 4, 5)
                test_board.move(5, 3, 3, 5)
                
class TestPawnPromotion:
        def test_white_pawn_becomes_queen_at_eighth_rank(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,0,4,0)
                test_board.move(1,1,3,1)
                test_board.move(4,0,3,1)
                test_board.move(0,1,2,2)
                test_board.move(3,1,2,1)
                test_board.move(1,5,2,5)
                test_board.move(2,1,1,1)
                test_board.move(2,5,3,5)
                test_board.move(1,1,0,1)
                assert isinstance(test_board.board[0][1], queen.Queen)
                assert test_board.board[0][1].colour == "White"
                
        def test_black_pawn_becomes_queen_at_first_rank(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,7,3,7)
                test_board.move(6,6,4,6)
                test_board.move(3,7,4,6)
                test_board.move(7,6,5,5)
                test_board.move(4,6,5,6)
                test_board.move(6,1,5,1)
                test_board.move(5,6,6,6)
                test_board.move(5,1,4,1)
                test_board.move(6,6,7,6)
                assert isinstance(test_board.board[7][6], queen.Queen)
                assert test_board.board[7][6].colour == "Black"   
