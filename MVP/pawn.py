from piece import Piece

class Pawn(Piece):
        def __init__(self, colour):
                self.colour = colour
                self.name = "Pawn"
                self.value = 1

                if self.colour == "Black":
                        self.symbol = '♟'
                elif self.colour == "White":
                        self.symbol = "♙"

        def illegal_directions(self, board, start_row, start_col, end_row, end_col):
                return any([
                        self.invalid_move_types(start_row, start_col, end_row, end_col),
                        self.__pawn_specific_board_constraints(board, start_row, start_col, end_row, end_col),
                        # self.move_leaves_king_in_check(board, end_row, end_col)
                        ]
                        )

        def invalid_move_types(self, start_row, start_col, end_row, end_col):
                return any([self.colour == "Black" and end_row < start_row,
                        self.colour == "White" and end_row > start_row,
                        start_row == end_row, # cannot move sideways
                        
                        abs(start_row - end_row) > 2, # cannot move more than 2 spaces
                        (start_row != 6 and start_row != 1) and abs(start_row - end_row) >= 2, # cannot move 2 spaces after 1st move
                        abs(start_col - end_col) > 1, # can't move diagonally more than 1 space
                        abs(start_row - end_row) == 2 and start_col != end_col, # can't move two spaces forward and sideways
                        ]
                        )


        def __pawn_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
                piece_to_move = board[start_row][start_col]
                if isinstance(piece_to_move, Pawn):
                        return any([start_col == end_col and isinstance(board[end_row][end_col], Piece),  # cannot move forward one space into another pawn
                                (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 1 and not isinstance(
                                board[end_row][end_col], Piece)),  # can only strike if pawn on target square
                                piece_to_move.colour == "White" and abs(end_row - start_row) == 2 and end_row < 7 and isinstance(
                                board[end_row+1][end_col], Piece),  # black cannot jump over pawn
                                piece_to_move.colour == "Black" and abs(end_row - start_row) == 2 and end_row > 0 and isinstance(
                                board[end_row-1][end_col], Piece),  # white cannot jump over pawn
                                hasattr(board[end_row][end_col], 'colour') and
                                        piece_to_move.colour == board[end_row][end_col].colour # cannot take any pieces of same colour
                                ]
                                )
                        
                        
        def move_leaves_king_in_check(self, board, end_row, end_col):
                # king_coords = [7,4] 
                king_coords = self.__find_current_colour_king(board)
                print(king_coords)
                king_in_question = board[king_coords[0]][king_coords[1]]
                print(king_in_question)
                if king_in_question.in_check(board, end_row, end_col): # check whether king would be in check after proposed move
                        print (f'{king_coords} IN CHECK')
                        return True
                else:
                        return False
        
        def __find_current_colour_king(self, board):
                import king
                return [7,4]
                for i in range(0,8):
                        for j in range(0,8):
                                if self.colour == "White":
                                        if isinstance(board[i][j], king.King):
                                                if board[i][j].colour == "White":
                                                        return [i,j]
                                elif self.colour == "Black":
                                        if isinstance(board[i][j], king.King):
                                                if board[i][j].colour == "Black":
                                                        return [i,j]
                

        
