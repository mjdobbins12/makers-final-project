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

    def move(self, start_row, start_col, end_row, end_col):
        piece_to_move = self.board[start_row][start_col]
        if self.__invalid_move(start_row, start_col, end_row, end_col):
            raise ValueError("Invalid Move")
        if self.__try_castling(piece_to_move, end_row, start_col, end_col) == 'invalid move':
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
            (piece_to_move.illegal_directions(current_board, start_row, start_col, end_row, end_col))
            ]
            )

    def __apply_promotion(self, piece, row, col):
        current_board = self.board
        if piece.name == "Pawn" and (row == 0 or row == 7):
            current_board[row][col] = queen.Queen(piece.colour)

    def __check_within_board_boundary(self, end_row, end_col):
        return (end_row > (len(self.board) - 1) or end_col > (len(self.board[0]) - 1) or end_row < 0 or end_col < 0)

    def __store_piece_if_struck(self, end_row, end_col):
        if self.board[end_row][end_col] != '-' and self.board[end_row][end_col].colour == 'White':
            self.chessboard.taken_white.append(self.board[end_row][end_col])
        if self.board[end_row][end_col] != '-' and self.board[end_row][end_col].colour == 'Black':
            self.chessboard.taken_black.append(self.board[end_row][end_col])


    # all castling checks:

    def __try_castling(self, piece_to_move, end_row, start_col, end_col):
        if isinstance(piece_to_move, king.King) and (abs(start_col - end_col) == 2):
            try:
                self.__iscastling(end_row, end_col)
            except:
                return 'invalid move'

    def __iscastling(self, end_row, end_col):
        if self.__check_castle_king_side(end_row, end_col):
            self.board[end_row][5] = self.board[end_row][7]
            self.board[end_row][7] = '-'
        elif self.__check_castle_queen_side(end_row, end_col):
            self.board[end_row][3] = self.board[end_row][0]
            self.board[end_row][0] = '-'
        else:
            raise ValueError("Invalid Move")

    def __check_castle_queen_side(self, end_row, end_col):
            return all([
                    (end_col == 2),
                    (self.board[end_row][4].counter == 0),
                    (self.board[end_row][0].counter == 0),
                    (not isinstance(self.board[end_row][1], piece.Piece)),
                    (not isinstance(self.board[end_row][2], piece.Piece)),
                    (not isinstance(self.board[end_row][3], piece.Piece))
                ])
    
    def __check_castle_king_side(self, end_row, end_col):
            return all([
                    (end_col == 6),
                    (self.board[end_row][4].counter == 0),
                    (self.board[end_row][7].counter == 0),
                    (not isinstance(self.board[end_row][5], piece.Piece)),
                    (not isinstance(self.board[end_row][6], piece.Piece)),
                ])
    
