class Piece:


        # shared movement constraints, e.g. for bishop + queen, rook + queen

        def check_if_diagonal_blocked(self, board, start_row, start_col, end_row, end_col):
                piece_to_move = board[start_row][start_col]
                i = start_row
                j = start_col
                if start_row < end_row and start_col < end_col:
                    while (i < end_row):
                        check_square = board[i + 1][j + 1]
                        if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                            return True
                        else:
                            i += 1
                            j += 1
                elif start_row > end_row and start_col > end_col:
                    while (i > end_row):
                        check_square = board[i - 1][j - 1]
                        if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                            return True
                        else:
                            i -= 1
                            j -= 1
                elif start_row < end_row and start_col > end_col:
                    while (i < end_row):
                        check_square = board[i + 1][j - 1]
                        if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                            return True
                        else:
                            i += 1
                            j -= 1
                elif start_row > end_row and start_col < end_col:
                    while (i > end_row):
                        check_square = board[i - 1][j + 1]
                        if isinstance(check_square, Piece) and check_square.colour == piece_to_move.colour:
                            return True
                        else:
                            i -= 1
                            j += 1

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
