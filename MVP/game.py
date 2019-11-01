import chessboard
import turn
import player
from king import King
from piece import Piece

class Game:

    def __init__(self, p1_name, p2_name):
        self.board = chessboard.ChessBoard()
        self.player_1 = player.Player("p1_name", "White")
        self.player_2 = player.Player("p2_name", "Black")
        self.p1_turn = True
        self.log = []


    def execute_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        try:
            self.check_player_owns_piece(int(turn_from_x), int(turn_from_y))
            turn.Turn(self.board).move(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.log_turn(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.p1_turn = not self.p1_turn
            return 'valid move'
        except:
            return 'invalid move'

    def log_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        colour = 'White' if self.p1_turn else 'Black'
        self.log.append([colour, turn_from_x, turn_from_y, turn_to_x, turn_to_y])

    def check_player_owns_piece(self, x, y):
        colour = 'White' if self.p1_turn else 'Black'
        if self.board.board[x][y].colour != colour:
            raise ValueError("PlayerDoesNotOwnPiece")


    def in_check(self, board):
        check_evaluations = []
        king_coordinates = self.__find_current_colour_king(board)
        for i in range(0,8):
            for j in range(0,8):
                if isinstance(board[i][j], Piece):
                    if [king_coordinates[0],king_coordinates[1]] in board[i][j].available_moves(board, i, j):
                        check_evaluations.append(True)
                    else:
                        check_evaluations.append(False)
        if True in check_evaluations:
            return True
        else:
            return False
    
    def __find_current_colour_king(self, board):
        for i in range(0,8):
            for j in range(0,8):
                if self.p1_turn:
                    if isinstance(board[i][j], King):
                        if board[i][j].colour == "White":
                            return [i,j]
                else:
                    if isinstance(board[i][j], King):
                        if board[i][j].colour == "Black":
                            return [i,j]

