import chessboard

test_board = chessboard.ChessBoard()

class TestChessBoard:
        def test_board_displayed(self):
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

        def test_referencing_board(self):
                assert test_board.show_board()[0][1] == ("N")
                assert test_board.show_board()[5][3] == ("-")
                assert test_board.show_board()[7][7] == ("R")
                assert test_board.show_board()[0][3] != ("p")
 
