import piece
import king
import queen
import rook
import bishop
import knight
import pawn

from standard_rules import StandardRules

class ManyQueens(StandardRules):
        def __init__(self):
                self.starting_board = [
                        [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),queen.Queen("Black"),
                        king.King("Black"),bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")],
                        [queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black"),
                        queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [queen.Queen("White"),queen.Queen("White"),queen.Queen("White"),queen.Queen("White"),
                        queen.Queen("White"),queen.Queen("White"),queen.Queen("White"),queen.Queen("White")],
                        [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),queen.Queen("White"),
                        king.King("White"),bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]
                        ]
        