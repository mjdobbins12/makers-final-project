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
                
                self.pieces = [pawn.Pawn("Black"), rook.Rook("Black"), knight.Knight("Black"),
                                bishop.Bishop("Black"), queen.Queen("Black"), king.King("Black"),
                                pawn.Pawn("White"), rook.Rook("White"), knight.Knight("White"),
                                bishop.Bishop("White"), queen.Queen("White"), king.King("White")]
                                
                self.starting_board = [
                        self.__build_rank_with_king(0, 4), 
                        self.__build_rank_without_king(0, 4), 
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        self.__build_rank_without_king(6, 10), 
                        self.__build_rank_with_king(6, 10) 
                        ]
                
        def __build_rank_with_king(self, low, high):
                rank = []
                for i in range(0, 8):
                        rank.append(self.pieces[random.randint(low, high)])
                rank[random.randint(0, 7)] = self.pieces[high+1] 
                return rank
        
        def __build_rank_without_king(self, low, high):
                rank = []
                for i in range(0, 8):
                        rank.append(self.pieces[random.randint(low, high)])
                return rank