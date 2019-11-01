import chessboard
import turn
from king import King
from piece import Piece
from game import Game

class Checkmate:

        def is_checkmate(self, game):
                king_coords = game.__find_current_colour_king(self.board.board)
                king_in_question = self.board.board[king_coords[0]][king_coords[1]]
                checkmate_evaluations = []
                if king_in_question.in_check(self.board.board, king_coords[0], king_coords[1]) == True:
                    possible_king_moves_array = self.available_moves(self.board.board, king_coords[0], king_coords[1])
                    for coords in possible_king_moves_array:
                        if self.in_check(self.board.board, coords[0], coords[1]):
                            checkmate_evaluations.append(True)
                        else:
                            checkmate_evaluations.append(False)
                    print(checkmate_evaluations)
                    if False not in checkmate_evaluations:
                        return True
                    else:
                        return False
                else:
                    return False

        def __find_current_colour_king(self, game):
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