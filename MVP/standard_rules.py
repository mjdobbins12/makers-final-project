import piece
import king
import queen
import rook
import bishop
import knight
import pawn
import copy

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

        
    # counter trigger container method
    def check_special_events(self, board, piece, log):
              return

# Check

    def check_if_move_into_check(self, board, start_row, start_col, end_row, end_col):
        piece_to_move = board[start_row][start_col]
        colour = piece_to_move.colour
        changed_board = copy.deepcopy(board)
        changed_board[start_row][start_col] = "-"
        changed_board[end_row][end_col] = piece_to_move
        if self.__check_current_player_king(changed_board, colour) == True:
            return 'invalid move'

    def __check_current_player_king(self, changed_board, colour):
        for i in range(0,8):
            for j in range(0,8):
                if isinstance(changed_board[i][j], king.King):
                    if changed_board[i][j].colour == colour:
                        return changed_board[i][j].in_check(changed_board, i, j)

# Invalid moves

    def check_for_invalid_move(self, board, start_row, start_col, end_row, end_col):
        piece_to_move = board[start_row][start_col]
        return any(
                [self.__check_within_board_boundary(board, end_row, end_col),
                (piece_to_move.illegal_directions(board, start_row, start_col, end_row, end_col))
                ]
                )

    def __check_within_board_boundary(self, board, end_row, end_col):
        return (end_row > (len(board) - 1) or end_col > (len(board[0]) - 1) or end_row < 0 or end_col < 0)


# Pawn promotion

    def check_pawn_promotion(self, board, piece, row, col):
        if piece.name == "Pawn" and (row == 0 or row == 7):
            board[row][col] = queen.Queen(piece.colour)
