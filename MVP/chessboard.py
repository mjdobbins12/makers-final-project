import pawn
import rook
import piece

class ChessBoard:
        def __init__(self):
                self.board = [
                        [rook.Rook("Black"),"N","B","Q","K","B","N",rook.Rook("Black")],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        [rook.Rook("White"),"N","B","Q","K","B","N",rook.Rook("White")]
                        ]


        def show_board(self, p1_name, p2_name):
            print('')
            print(p2_name)
            print("| a | b | c | d | e | f | g | h |")
            print("_" * 33)
            ind = 8
            for row in self.board:
                x = "|"
                for el in row:
                    if isinstance(el, pawn.Pawn):
                        x += f" {el.name} |"
                    else:
                        x += f" {el} |"
                x += f" {ind}"
                ind -= 1
                print(x)
                print("-" * 33)
            print(p1_name)
            print('')

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
                        piece_to_move.illegal_directions(start_row, start_col, end_row, end_col), # checks piece allowed vectors
                        self.__pawn_specific_board_constraints(start_row, start_col, end_row, end_col),
                        self.__rook_specific_board_constraints(start_row, start_col, end_row, end_col) # references board to check possibility of moves
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

        def __rook_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if isinstance(piece_to_move, rook.Rook):
                        return any([(self.__check_if_row_or_column_blocked(start_row, start_col, end_row, end_col)),
                                ]
                                )

        def __check_if_row_or_column_blocked(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                if start_row == end_row:
                        squares_between = list(range(start_col + 1, end_col))
                        squares_between[:] = [self.board[start_row][element] for element in squares_between]
                        if any(isinstance(x, piece.Piece) for x in squares_between):
                                return True
                else:
                        if start_row > end_row:
                                squares_between = list(range(end_row + 1, start_row))
                        else:
                                squares_between = list(range(start_row + 1, end_row))
                        squares_between[:] = [self.board[element][start_col] for element in squares_between]
                        if any(isinstance(x, piece.Piece) for x in squares_between):
                                return True
