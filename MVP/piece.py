class Piece:

        def available_moves(self, board, start_row, start_col):
                piece_to_move = board[start_row][start_col]
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if piece_to_move.illegal_directions(board, start_row, start_col, i, j) == False:
                                        array.append([i,j])
                return array

        # shared movement constraints, e.g. for bishop + queen, rook + queen

        def check_if_diagonal_blocked(self, board, start_row, start_col, end_row, end_col):
                # piece_to_move = board[start_row][start_col]
                # if start_row > end_row:
                #                 rows_between = list(
                #                 range(end_row + 1, start_row))
                #         else:
                #                 rows_between = list(
                #                 range(start_row + 1, end_row))


                # if start_col > end_col:
                #                 cols_between = list(
                #                 range(end_col + 1, start_col))
                #         else:
                #                 cols_between = list(
                #                 range(start_col + 1, end_col))

                #         squares_between[:] = [board[element][start_col]
                #                         for element in squares_between]
                #         if any(isinstance(x, Piece) for x in squares_between):
                #                 return True


                if start_row < end_row and start_col < end_col:
                    check_square = board[start_row + 1][start_col + 1]
                    if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                        return True
                    elif check_square == board[end_row][end_col]:
                        return False
                    else:
                        self.check_if_diagonal_blocked(self, board, start_row + 1, start_col + 1, end_row, end_col)
                elif start_row > end_row and start_col > end_col:
                    check_square = board[start_row - 1][start_col - 1]
                    if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                        return True
                    elif check_square == board[end_row][end_col]:
                        return False
                    else:
                        self.check_if_diagonal_blocked(self, board, start_row - 1, start_col - 1, end_row, end_col)
                elif start_row < end_row and start_col > end_col:
                    check_square = board[start_row + 1][start_col - 1]
                    if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                        return True
                    elif check_square == board[end_row][end_col]:
                        return False
                    else:
                        self.check_if_diagonal_blocked(self, board, start_row + 1, start_col - 1, end_row, end_col)
                elif start_row > end_row and start_col < end_col:
                    check_square = board[start_row - 1][start_col + 1]
                    if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                        return True
                    elif check_square == board[end_row][end_col]:
                        return False
                    else:
                        self.check_if_diagonal_blocked(self, board, start_row - 1, start_col + 1, end_row, end_col)

        def check_if_row_or_column_blocked(self, board, start_row, start_col, end_row, end_col):
                if start_row == end_row:
                        if start_col > end_col:
                                squares_between = list(
                                range(end_col + 1, start_col))
                        else:
                                squares_between = list(
                                range(start_col + 1, end_col))
                        squares_between[:] = [board[start_row][element]
                                        for element in squares_between]
                        if any(isinstance(x, Piece) for x in squares_between):
                                return True
                else:
                        if start_row > end_row:
                                squares_between = list(
                                range(end_row + 1, start_row))
                        else:
                                squares_between = list(
                                range(start_row + 1, end_row))
                        squares_between[:] = [board[element][start_col]
                                        for element in squares_between]
                        if any(isinstance(x, Piece) for x in squares_between):
                                return True
