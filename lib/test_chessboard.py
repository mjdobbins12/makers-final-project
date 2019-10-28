import chessboard

test_board = chessboard.ChessBoard()

class TestChessBoard:
        def test_board_displayed(self):
                assert test_board.show_board() == [
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"],
                ["-","-","-","-","-","-","-","-"]
                ]

        def test_referencing_board(self):
                assert test_board.show_board()[0][1] == ("-")
                assert test_board.show_board()[5][3] == ("-")
                assert test_board.show_board()[7][7] == ("-")