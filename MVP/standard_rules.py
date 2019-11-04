import piece
import king
import queen
import rook
import bishop
import knight
import pawn

# Allows rules to be extracted with tests passing. Starting board 
# is taken from rule set, then gameplay happens in that instance of board inside
# the ChessBoard instance. 
# Moves are checked against the current board by the ruleset, against its 
# stored rules. A bit of back and forth between ChessBoard and RuleSet, but clearly
# preferable to the game taking place within the ruleset's own version of the board object. 

# Board boundary is defined inside this object. 
# Piece specific rules remain on the pieces themselves. This does lead to 
# Some flexibility; by creating a different starting board below with special variants of pieces
# we could introduce different constraints to the game. However, would need more methods to 
# be able to change rules mid-game

class StandardRules:
        
        def __init__(self):
                self.starting_board = [
                        [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),queen.Queen("Black"),
                         king.King("Black"),bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),queen.Queen("White"),
                         king.King("White"),bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]
                        ]
