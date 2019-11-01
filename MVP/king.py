from piece import Piece

class King(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.name = "King"
        if self.colour == "Black":
            self.symbol = '♚'
        elif self.colour == "White":
            self.symbol = '♔'

    def in_check(self, board, start_row, start_col):
        check_evaluations = []
        king_in_question = board[start_row][start_col]
        for i in range(0,8):
            for j in range(0,8):
                if isinstance(board[i][j], Piece):
                    # print([[board[i][j].name, board[i][j].colour], board[i][j].available_moves(board, i, j)])
                    if [start_row,start_col] in board[i][j].available_moves(board, i, j):
                        check_evaluations.append(True)
                    else:
                        check_evaluations.append(False)
        if True in check_evaluations:
            return True
        else:
            return False

    def illegal_directions(self, board, start_row, start_col, end_row, end_col):
        if abs(start_col - end_col) == 2:
            return any([
                (self.__invalid_castling(board, start_row, start_col, end_row, end_col))
                ])
        else:
            return any([
                (self.invalid_move_types(start_row, start_col, end_row, end_col)),
                (self.__king_specific_board_constraints(board, start_row, start_col, end_row, end_col))
                ])

    def invalid_move_types(self, start_row, start_col, end_row, end_col):
        if (start_row != end_row and start_col != end_col) and (abs(start_row - end_row) != abs(start_col - end_col)):
            return True
        else:
            return False

    def __invalid_castling(self, board, start_row, start_col, end_row, end_col):
        return any([
            self.counter > 0,
            start_row in range(1,7),
            start_row != end_row
            ])

    def __king_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
        piece_to_move = board[start_row][start_col]
        return any([
            (self.__check_king_adjacent_to_target_square(board, start_row, start_col, end_row, end_col)),
            (abs(start_row - end_row) > 1),
            (abs(start_col - end_col) > 1),
            (isinstance(board[end_row][end_col], Piece) and board[end_row][end_col].colour == piece_to_move.colour)
            ])

    def __check_king_adjacent_to_target_square(self, board, start_row, start_col, end_row, end_col):
        opposite_king_position = self.__find_opposite_colour_king(board, start_row, start_col)
        if abs(abs(end_row) - abs(opposite_king_position[0])) > 1 or abs(abs(end_col) - abs(opposite_king_position[1])) > 1:
            return False
        else:
            return True

    def __find_opposite_colour_king(self, board, start_row, start_col):
        if isinstance(board[start_row][start_col], King):
            if board[start_row][start_col].colour == "White":
                        for i in range(0,8):
                            for j in range(0,8):
                                if isinstance(board[i][j], King):
                                    if board[i][j].colour == "Black":
                                        return [i,j]
            elif board[start_row][start_col].colour == "Black":
                        for i in range(0,8):
                            for j in range(0,8):
                                if isinstance(board[i][j], King):
                                    if board[i][j].colour == "White":
                                        return [i,j]