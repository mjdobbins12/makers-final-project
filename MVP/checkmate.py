from king import King
from piece import Piece
from turn import Turn

class Checkmate:
        def __init__(self, game):
            self.game = game
            self.board = game.board
            if game.p1_turn == True:
                self.current_player = game.player_1.colour
            else:
                self.current_player = game.player_2.colour

        def is_checkmate(self):
            checkmate_evals = []
            for i in range(0,8):
                for j in range(0,8):
                    if isinstance(self.board[i][j], Piece) and self.board[i][j].colour == self.current_player:
                        for sq in self.board[i][j].available_moves(self.board, i, j):
                            checkmate_evals.append(Turn(self.game.ruleset, self.board, self.game.player_1, self.game.player_2).check_if_self_in_check(i, j, sq[0], sq[1]) == 'invalid move')
            print(self.current_player)
            # print(checkmate_evals)
            print(self.board[1][5])
            return all(checkmate_evals)

        def __find__king_in_check(self):
            for i in range(0,8):
                for j in range(0,8):
                    if isinstance(self.game.board[i][j], King):
                        if self.game.board[i][j].in_check(self.board, i, j):
                            return [i,j].colour
                    else:
                        return self.current_player

        # def is_checkmate(self):
        #         return any([self.__check_for_possible_king_moves(), self.__check_for_possible_checkmate_blocks()])

        # private methods

        # def __check_for_possible_king_moves(self):
        #         king_coords = self.__find_current_colour_king()
        #         king_in_question = self.game.board[king_coords[0]][king_coords[1]]
        #         checkmate_evaluations = []
        #         if king_in_question.in_check(self.game.board, king_coords[0], king_coords[1]) == True:
        #             possible_king_moves_array = king_in_question.available_moves(self.game.board, king_coords[0], king_coords[1])
        #             for coords in possible_king_moves_array:
        #                 possible_move_target_square = self.game.board[coords[0]][coords[1]]
        #                 self.game.board[coords[0]][coords[1]] = king_in_question
        #                 self.game.board[king_coords[0]][king_coords[1]] = "-"
        #                 if king_in_question.in_check(self.game.board, coords[0], coords[1]):
        #                     checkmate_evaluations.append(True)
        #                 else:
        #                     checkmate_evaluations.append(False)
        #                 self.game.board[king_coords[0]][king_coords[1]] = king_in_question
        #                 self.game.board[coords[0]][coords[1]] = possible_move_target_square
        #             print(possible_king_moves_array)
        #             print(checkmate_evaluations)
        #             if False not in checkmate_evaluations:
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             return False
        #
        #
        # def __check_for_possible_checkmate_blocks(self):
        #         checkmate_evaluations = []
        #         king_coords = self.__find_current_colour_king()
        #         king_in_question = self.game.board[king_coords[0]][king_coords[1]]
        #         # print([king_in_question, king_in_question.colour])
        #         if king_in_question.in_check(self.game.board, king_coords[0], king_coords[1]):
        #         # all_available_moves_for_all_same_colour_pieces:
        #                 for i in range(0,8):
        #                         for j in range(0,8):
        #                             if isinstance(self.game.board[i][j], Piece) and not isinstance(self.game.board[i][j], King):
        #                                 if self.game.board[i][j].colour == king_in_question.colour:
        #                                     all_possible = self.game.board[i][j].available_moves(self.game.board, i, j)
        #                                     # print([all_possible, self.game.board[i][j], self.game.board[i][j].colour, i, j])
        #                                     for k in all_possible:
        #                                         original_piece = self.game.board[i][j]
        #                                         target_square = self.game.board[k[0]][k[1]]
        #                                         self.game.board[k[0]][k[1]] = self.game.board[i][j]
        #                                         self.game.board[i][j] = "-"
        #                                         if king_in_question.in_check(self.game.board, king_coords[0], king_coords[1]):
        #                                             checkmate_evaluations.append(True)
        #                                         else:
        #                                             checkmate_evaluations.append(False)
        #                                         self.game.board[i][j] = original_piece
        #                                         self.game.board[k[0]][k[1]] = target_square
        #                                     # print(checkmate_evaluations)
        #                 if False in checkmate_evaluations:
        #                     return False
        #                 else:
        #                     return True
        #         else:
        #             return False
