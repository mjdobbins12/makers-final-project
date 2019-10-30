import pawn
import bishop
import rook
import piece
import knight

# Allows rules to be extracted with tests passing. Starting board 
# is taken from rule set, then gameplay happens in that instance of board inside
# the ChessBoard instance. 
# Moves are checked against the current board by the ruleset, against its 
# stored rules. A bit of back and forth between ChessBoard and RuleSet, but clearly
# preferable to the game taking place within the ruleset object. 

# Board boundary is defined inside this object. 
# Piece specific rules remain on the pieces themselves. This does lead to 
# Some flexibility; by creating a different starting board below with special variants of pieces
# we could introduce different constraints to the game. However, would need more methods to 
# be able to change rules mid-game

class StandardRules:
        
        def __init__(self):
                self.starting_board = [
                        [rook.Rook("Black"),knight.Knight("Black"),bishop.Bishop("Black"),"Q","K",bishop.Bishop("Black"),knight.Knight("Black"),rook.Rook("Black")],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        [rook.Rook("White"),knight.Knight("White"),bishop.Bishop("White"),"Q","K",bishop.Bishop("White"),knight.Knight("White"),rook.Rook("White")]
                        ]
                
        def invalid_move(self, board, start_row, start_col, end_row, end_col):
                current_board = board
                piece_to_move = current_board[start_row][start_col]
                return any(
                        [self.check_within_board_boundary(end_row,end_col),
                        (piece_to_move.illegal_directions(current_board, start_row, start_col, end_row, end_col)) # checks pawn allowed vectors
                        ]
                        )

        def check_within_board_boundary(self, end_row, end_col):
                return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)
        
