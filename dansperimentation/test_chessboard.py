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
                assert test_board.show_board() == test_board.board

        def test_referencing_board(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[0][1] == ("N")
                assert test_board.board[5][3] == ("-")
                assert test_board.board[7][7] == ("R")
                assert test_board.board[0][3] != ("p")
                
class TestPawnAllowedMoves:
        def test_black_pawn_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,5,1)
                assert isinstance(test_board.board[5][1], pawn.Pawn)
                assert test_board.board[5][1].colour == "Black"
                assert test_board.show_board()[6][1] == ("-")

        def test_white_pawn_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,2,2)
                assert isinstance(test_board.board[2][2], pawn.Pawn)
                assert test_board.board[2][2].colour == "White"
                assert test_board.show_board()[1][2] == ('-')

        def test_black_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                assert isinstance(test_board.board[4][1], pawn.Pawn)
                assert test_board.board[4][1].colour == "Black"
                assert test_board.show_board()[6][1] == ("-")

        def test_white_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,3,2)
                assert isinstance(test_board.board[3][2], pawn.Pawn)
                assert test_board.board[3][2].colour == "White"
                assert test_board.show_board()[1][2] == ('-')
                
        def test_black_pawn_can_move_1_further_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                test_board.move(4,1,3,1)
                assert isinstance(test_board.board[3][1], pawn.Pawn)
                assert test_board.board[3][1].colour == "Black"
                assert test_board.show_board()[4][1] == ("-")
                
        def test_white_pawn_can_move_1_further_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,3,2)
                test_board.move(3,2,4,2)
                assert isinstance(test_board.board[4][2], pawn.Pawn)
                assert test_board.board[4][2].colour == "White"
                assert test_board.show_board()[3][2] == ("-")

        def test_pawn_object_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,6,5,6)
                assert isinstance(test_board.board[5][6], pawn.Pawn)
                assert test_board.show_board()[6][6] == ("-")
                
class TestPawnStriking:
        def test_black_pawn_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,4,3)
                test_board.move(1,5,3,5)
                test_board.move(4,3,3,5)
                assert test_board.show_board()[1][5] == ("-")
                assert test_board.show_board()[6][3] == ("-")
                assert test_board.show_board()[4][3] == ("-")
                assert isinstance(test_board.board[3][5], pawn.Pawn)
                assert test_board.board[3][5].colour == "Black"
                
        def test_white_pawn_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,4,3)
                test_board.move(1,5,3,5)
                test_board.move(3,5,4,3)
                assert test_board.show_board()[1][5] == ("-")
                assert test_board.show_board()[6][3] == ("-")
                assert test_board.show_board()[3][5] == ("-")
                assert isinstance(test_board.board[4][3], pawn.Pawn)
                assert test_board.board[4][3].colour == "White"


class TestPieceObjects:
        def test_pawn_objects_are_stored_in_board(self, run_before_tests):
                test_board = run_before_tests
                assert isinstance(test_board.board[6][6], pawn.Pawn)

        def test_pawn_objects_can_have_colour_property(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[6][6].colour == ("Black")

        def test_pawn_objects__can_have_colour_property_white(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[1][7].colour == ("White")

        

class TestPawnDirection:
        def test_black_pawn_can_only_move_forwards(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,1,7,1)

        def test_white_pawn_can_only_move_forwards(self, run_before_tests):
                test_board = run_before_tests
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(1,1,0,1)
# class TestBoardBoundaries:
#         def test_pawn_cannot_move_
        
        
        
        
        
        
        
                
        

                
                
                
        
        



        # def test_pawn_cannot_move_3_spaces(self):
        #         with pytest.raises(ValueError, match=r"Invalid Move"):
        #                 test_board.move(6,1,3,1)
 
