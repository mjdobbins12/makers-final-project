import pawn
import bishop
import rook
import piece
import knight
import king
import queen

class Turn:
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.board = chessboard.board
        # self.player = player

    def move(self, start_row, start_col, end_row, end_col):
        if self.__invalid_move(start_row, start_col, end_row, end_col):
            raise ValueError("Invalid Move")
        piece_to_move = self.board[start_row][start_col]
        if self.__check_castling(piece_to_move, end_row, start_col, end_col) == 'invalid move':
            raise ValueError("Invalid Move")
        self.board[start_row][start_col] = "-"
        self.__store_piece_if_struck(end_row, end_col)
        self.board[end_row][end_col] = piece_to_move
        piece_to_move.increment_counter()
        self.__apply_promotion(piece_to_move, end_row, end_col)

    # private methods

    def __invalid_move(self, start_row, start_col, end_row, end_col):
        current_board = self.board
        piece_to_move = self.board[start_row][start_col]
        return any(
            [self.__check_within_board_boundary(end_row, end_col),
            (piece_to_move.illegal_directions(current_board, start_row, start_col, end_row, end_col)) # checks pawn allowed vectors
            ]
            )

    def __apply_promotion(self, piece, row, col):
        current_board = self.board
        if piece.name == "Pawn" and (row == 0 or row == 7):
            current_board[row][col] = queen.Queen(piece.colour)

    def __check_within_board_boundary(self, end_row, end_col):
        return (end_row > 7 or end_col > 7 or end_row < 0 or end_col < 0)

    def __store_piece_if_struck(self, end_row, end_col):
        if self.board[end_row][end_col] != '-' and self.board[end_row][end_col].colour == 'White':
            self.chessboard.taken_white.append(self.board[end_row][end_col])
            return self.board[end_row][end_col]
        if self.board[end_row][end_col] != '-' and self.board[end_row][end_col].colour == 'Black':
            self.chessboard.taken_black.append(self.board[end_row][end_col])

    def __check_castling(self, piece_to_move, end_row, start_col, end_col):
        if isinstance(piece_to_move, king.King) and (abs(start_col - end_col) == 2):
            try:
                self.__iscastling(end_row, end_col)
            except:
                return 'invalid move'

    def __iscastling(self, end_row, end_col):
        if (end_col == 6) and (self.board[end_row][7].counter == 0):
            self.board[end_row][5] = self.board[end_row][7]
            self.board[end_row][7] = '-'
        elif (end_col == 2) and (self.board[end_row][0].counter == 0):
            self.board[end_row][3] = self.board[end_row][0]
            self.board[end_row][0] = '-'
        else:
            raise ValueError("Invalid Move")
