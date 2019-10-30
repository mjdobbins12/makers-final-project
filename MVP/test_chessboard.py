import chessboard
import pawn
import pytest


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
                test_board.move(1,5,0,5)
                test_board.move(3,0,4,0)
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(0,5,-1,5)

        def test_pawn_cannot_move_outside_columns(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,7,6,8)

        # the below test seems not to be running?
        def pawn_can_move_2_spaces_forward(self):
                test_board.move(6,1,4,1)
                assert test_board.board[4][1] == ("p")
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
