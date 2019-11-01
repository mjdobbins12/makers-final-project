import pawn
import bishop
import rook
import piece
import knight
import king
import queen
import turn

class ChessBoard:
        def __init__(self):
                self.board = [
                        [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),queen.Queen(
                        "Black"),king.King("Black"),bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),queen.Queen("White"),king.King("White"),bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]
                        ]
                self.taken_white = []
                self.taken_black = []


# these just pass through for testing purposes - do not reference these in new tests !!!!!!

        def move(self, start_row, start_col, end_row, end_col):
                turn.Turn(self).move(start_row, start_col, end_row, end_col)
