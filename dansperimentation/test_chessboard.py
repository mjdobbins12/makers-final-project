import chessboard
import pytest

test_board = chessboard.ChessBoard()

class TestChessBoard:
        def test_board_displayed(self):
                assert test_board.board == [
                ["R","N","B","K","Q","B","N","R"],
                ['p','p','p','p','p','p','p','p'],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ['p','p','p','p','p','p','p','p'],
                ["R","N","B","Q","K","B","N","R"]
                ]

        def test_referencing_board(self):
                assert test_board.board[0][1] == ("N")
                assert test_board.board[5][3] == ("-")
                assert test_board.board[7][7] == ("R")
                assert test_board.board[0][3] != ("p")

        def pawn_can_move_2_spaces_forward(self):
                test_board.move(6,1,4,1)
                assert test_board.board[4][1] == ("p")
                assert test_board.board[6][1] == ("-")

        def test_pawn_cannot_move_3_spaces(self):
                with pytest.raises(ValueError, match=r"Invalid Move"):
                        test_board.move(6,1,3,1)
