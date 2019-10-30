import pawn
import knight

class ChessBoard:
        def __init__(self):
                self.board = [
                        ["R","N","B","Q","K","B","N","R"],
                        [pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),
                        pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black"),pawn.Pawn("Black")],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        ["-","-","-","-","-","-","-","-"],
                        [pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),
                        pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White"),pawn.Pawn("White")],
                        ["R",knight.Knight("White"),"B","Q","K","B","N","R"]
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
                if piece_to_move.name == "Pawn":
                        return any(
                                [self.__check_within_board_boundary(end_row,end_col),
                                piece_to_move.illegal_directions(start_row, start_col, end_row, end_col), # checks pawn allowed vectors
                                self.__pawn_specific_board_constraints(start_row, start_col, end_row, end_col) # references board to check possibility of moves
                                ]
                                )


        def __check_within_board_boundary(self, end_row, end_col):
                return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)

        def __pawn_specific_board_constraints(self, start_row, start_col, end_row, end_col):
                piece_to_move = self.board[start_row][start_col]
                return any([start_col == end_col and isinstance(self.board[end_row][end_col], pawn.Pawn), # cannot move forward one space into another pawn
                        (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1 and not isinstance(self.board[end_row][end_col], pawn.Pawn)), # can only strike if pawn on target square
                        piece_to_move.colour == "White" and abs(end_row - start_row) == 2 and isinstance(self.board[end_row+1][end_col], pawn.Pawn), # black cannot jump over pawn
                        piece_to_move.colour == "Black" and abs(end_row - start_row) == 2 and isinstance(self.board[end_row-1][end_col], pawn.Pawn) # white cannot jump over pawn
                        ]
                        )
