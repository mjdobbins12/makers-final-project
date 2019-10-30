import pawn
import knight

class ChessBoard:
        def __init__(self):
                self.board = [
                        ["R",knight.Knight("Black"),"B","Q","K","B",knight.Knight("Black"),"R"],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        ["R",knight.Knight("White"),"B","Q","K","B",knight.Knight("White"),"R"]
                        ]

        def move(self, start_row, start_col, end_row, end_col):
                if self.__invalid_move(start_row, start_col, end_row, end_col):
                        raise ValueError("Invalid Move")
                piece_to_move = self.board[start_row][start_col]
                self.board[start_row][start_col] = "-"
                self.board[end_row][end_col] = piece_to_move

        # private methods

        def __invalid_move(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                return any(
                        [self.__check_within_board_boundary(end_row,end_col),
                        piece_to_move.illegal_directions(start_row, start_col, end_row, end_col), # checks pawn allowed vectors
                        self.__knight_specific_board_constraints(start_row, start_col, end_row, end_col), # references board to check possibility of moves
                        self.__pawn_specific_board_constraints(start_row, start_col, end_row, end_col) # references board to check possibility of moves
                        ]
                        )


        def __check_within_board_boundary(self, end_row, end_col):
                return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)

        def __pawn_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, pawn.Pawn):
                        return any([start_col == end_col and isinstance(self.board[end_row][end_col], pawn.Pawn), # cannot move forward one space into another pawn
                                (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1 and not isinstance(self.board[end_row][end_col], pawn.Pawn)), # can only strike if pawn on target square
                                piece_to_move.colour == "White" and abs(end_row - start_row) == 2 and isinstance(self.board[end_row+1][end_col], pawn.Pawn), # black cannot jump over pawn
                                piece_to_move.colour == "Black" and abs(end_row - start_row) == 2 and isinstance(self.board[end_row-1][end_col], pawn.Pawn) # white cannot jump over pawn
                                ]
                                )
                
        def __knight_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, knight.Knight):
                        return any([
                                hasattr(self.board[end_row][end_col], 'colour') and 
                                        piece_to_move.colour == self.board[end_row][end_col].colour # knight cannot take any piece of same colour
                                ]
                                )

                
                
                
                