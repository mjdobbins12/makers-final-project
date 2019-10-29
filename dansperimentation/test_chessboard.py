import chessboard
import pytest

@pytest.fixture(autouse=True)
def run_before_tests():
        test_board = chessboard.ChessBoard()
        return test_board


class TestStartingBoard:
        def test_board_displayed(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.show_board() == [
                ["R","N","B","K","Q","B","N","R"],
                ['p','p','p','p','p','p','p','p'],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ['p','p','p','p','p','p','p','p'],
                ["R","N","B","Q","K","B","N","R"]
                ]

        def test_referencing_board(self, run_before_tests):
                test_board = run_before_tests
                assert test_board.board[0][1] == ("N")
                assert test_board.board[5][3] == ("-")
                assert test_board.board[7][7] == ("R")
                assert test_board.board[0][3] != ("p")
                
                
class TestPawnAllowedMoves:
        def test_white_pawn_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,5,1)
                assert test_board.show_board()[5][1] == ("p")
                assert test_board.show_board()[6][1] == ("-")

        def test_black_pawn_can_move_1_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,2,2)
                assert test_board.show_board()[2][2] == ('p')
                assert test_board.show_board()[1][2] == ('-')

        def test_white_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                assert test_board.show_board()[4][1] == ("p")
                assert test_board.show_board()[6][1] == ("-")

        def test_black_pawn_can_move_2_spaces_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,3,2)
                assert test_board.show_board()[3][2] == ('p')
                assert test_board.show_board()[1][2] == ('-')
                
        def test_white_pawn_can_move_1_further_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,1,4,1)
                test_board.move(4,1,3,1)
                assert test_board.show_board()[3][1] == ("p")
                assert test_board.show_board()[4][1] == ("-")
                
        def test_black_pawn_can_move_1_further_space_forward(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(1,2,3,2)
                test_board.move(3,2,4,2)
                assert test_board.show_board()[4][2] == ("p")
                assert test_board.show_board()[3][2] == ("-")
                
class TestPawnStriking:
        def test_white_pawn_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,4,3)
                test_board.move(1,5,3,5)
                test_board.move(4,3,3,5)
                assert test_board.show_board()[1][5] == ("-")
                assert test_board.show_board()[6][3] == ("-")
                assert test_board.show_board()[4][3] == ("-")
                assert test_board.show_board()[3][5] == ("p")
                
        def test_black_pawn_can_move_forward_left(self, run_before_tests):
                test_board = run_before_tests
                test_board.move(6,3,4,3)
                test_board.move(1,5,3,5)
                test_board.move(3,5,4,3)
                assert test_board.show_board()[1][5] == ("-")
                assert test_board.show_board()[6][3] == ("-")
                assert test_board.show_board()[3][5] == ("-")
                assert test_board.show_board()[4][3] == ("p")
        
        
        
        
        
                
        

                
                
                
        
        



        # def test_pawn_cannot_move_3_spaces(self):
        #         with pytest.raises(ValueError, match=r"Invalid Move"):
        #                 test_board.move(6,1,3,1)
 
