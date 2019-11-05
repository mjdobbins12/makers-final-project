import piece
import king
import queen
import rook
import bishop
import knight
import pawn
import random

from standard_rules import StandardRules

class RandomPieces(StandardRules):
        def __init__(self):
 
                self.pieces = [pawn.Pawn("Black"),
                                rook.Rook("Black"),
                                knight.Knight("Black"),
                                bishop.Bishop("Black"),
                                queen.Queen("Black"), 
                                king.King("Black"),
                                pawn.Pawn("White"),
                                rook.Rook("White"),
                                knight.Knight("White"),
                                bishop.Bishop("White"),
                                queen.Queen("White"), 
                                king.King("White")]
                
                self.rank_1 = self.build_rank_with_king(0, 4)
                self.rank_2 = self.build_rank_without_king(0, 4)
                self.rank_3 = ["-","-","-","-","-","-","-","-"]
                self.rank_4 = ["-","-","-","-","-","-","-","-"]
                self.rank_5 = ["-","-","-","-","-","-","-","-"]
                self.rank_6 = ["-","-","-","-","-","-","-","-"]
                self.rank_7 = self.build_rank_without_king(6, 10)
                self.rank_8 = self.build_rank_with_king(6, 10)
                
                self.starting_board = self.build_board()
                
        def build_rank_with_king(self, start, finish):
                rank = []
                for i in range(0,8):
                        rank.append(self.pieces[random.randint(start,finish)])
                rank[random.randint(0,8)] = self.pieces[finish+1] 
                return rank
        
        def build_rank_without_king(self, start, finish):
                rank = []
                for i in range(0,8):
                        rank.append(self.pieces[random.randint(start,finish)])
                return rank
           
        def build_board(self):
                board = []
                board.append(self.rank_1)
                board.append(self.rank_2)
                board.append(self.rank_3)
                board.append(self.rank_4)
                board.append(self.rank_5)
                board.append(self.rank_6)
                board.append(self.rank_7)
                board.append(self.rank_8)
                return board



             
             
             
             
# self.rank_1 = [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),queen.Queen("Black"),
#         king.King("Black"),bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")]
        
# self.rank_2 = [queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black"),
#         queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black"),queen.Queen("Black")]
        
# self.rank_3 = ["-","-","-","-","-","-","-","-"],
# self.rank_4 = ["-","-","-","-","-","-","-","-"],
# self.rank_5 = ["-","-","-","-","-","-","-","-"],
# self.rank_6 = ["-","-","-","-","-","-","-","-"],
        
# self.rank_7 = [queen.Queen("White"),queen.Queen("White"),queen.Queen("White"),queen.Queen("White"),
#        queen.Queen("White"),queen.Queen("White"),queen.Queen("White"),queen.Queen("White")],
# self.rank_8 = [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),queen.Queen("White"),
#         king.King("White"),bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]

                
        