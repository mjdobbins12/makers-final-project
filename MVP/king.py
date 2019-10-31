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
                    if [start_row,start_col] in board[i][j].available_moves(board, i, j):
                        check_evaluations.append(True)
                    else:
                        check_evaluations.append(False)
        if True in check_evaluations:
            return True
        else:
            return False

    def is_checkmate(self, board, target_king_row, target_king_col):
        checkmate_evaluations = []
        possible_king_moves_array = self.available_moves(board, target_king_row, target_king_col)
        for coords in possible_king_moves_array:
            if self.in_check(board, coords[0], coords[1]):
                checkmate_evaluations.append(True)
            else:
                checkmate_evaluations.append(False)
        if True in checkmate_evaluations:
            return True
        else:
            return False






    def illegal_directions(self, board, start_row, start_col, end_row, end_col):
        return any([
            (self.invalid_move_types(start_row, start_col, end_row, end_col)),
            (self.__king_specific_board_constraints(board, start_row, start_col, end_row, end_col))
            ])

    def invalid_move_types(self, start_row, start_col, end_row, end_col):
        if (start_row != end_row and start_col != end_col) and (abs(start_row - end_row) != abs(start_col - end_col)):
            return True
        else:
            return False

    def __king_specific_board_constraints(self, board, start_row, start_col, end_row, end_col):
        piece_to_move = board[start_row][start_col]
        return any([
            (abs(start_row - end_row) > 1),
            (abs(start_col - end_col) > 1),
            (isinstance(board[end_row][end_col], Piece) and board[end_row][end_col].colour == piece_to_move.colour)
            ])
