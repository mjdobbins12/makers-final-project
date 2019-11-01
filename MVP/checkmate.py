from king import King
from game import Game

class Checkmate:
        def __init__(self, game):
                self.game = game

        def is_checkmate(self):
                king_coords = self.__find_current_colour_king()
                king_in_question = self.game.board.board[king_coords[0]][king_coords[1]]
                checkmate_evaluations = []
                if king_in_question.in_check(self.game.board.board, king_coords[0], king_coords[1]) == True:
                    possible_king_moves_array = king_in_question.available_moves(self.game.board.board, king_coords[0], king_coords[1])
                    for coords in possible_king_moves_array:
                        if king_in_question.in_check(self.game.board.board, coords[0], coords[1]):
                            checkmate_evaluations.append(True)
                        else:
                            checkmate_evaluations.append(False)
                    if False not in checkmate_evaluations:
                        return True
                    else:
                        return False
                else:
                    return False

        def __find_current_colour_king(self):
                for i in range(0,8):
                    for j in range(0,8):
                        if self.game.p1_turn:
                            if isinstance(self.game.board.board[i][j], King):
                                if self.game.board.board[i][j].colour == "White":
                                    return [i,j]
                        else:
                            if isinstance(self.game.board.board[i][j], King):
                                if self.game.board.board[i][j].colour == "Black":
                                    return [i,j]

      