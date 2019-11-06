from piece import Piece
import copy
from random import random
from heuristics import Heuristics

class Minimax:
        def __init__(self, game):
                self.game = copy.deepcopy(game)


        def all_possible_moves(self, board):
                evaluation_array = []
                all_available_moves = self.available_moves(board)
                for moveset in all_available_moves:
                        if len(moveset[1]) != 0:
                                for j in moveset[1]:
                                        pieces = self.game.get_original_pieces(board, moveset[0][0], moveset[0][1], j[0], j[1])
                                        self.game.execute_turn(moveset[0][0], moveset[0][1], j[0], j[1])
                                        score = Heuristics(self.game).evaluate(self.game)
                                        evaluation_array.append([score, moveset[0], [j[0],j[1]]])
                                        self.game.revert_turn(moveset[0][0], moveset[0][1], j[0], j[1], pieces[0], pieces[1])
                return evaluation_array

        # def minimax(self):
        #         level_1_evals = []
        #         a = 0
        #         next_move_evaluation_array = self.all_possible_moves(self.game.board)
        #         next_move_evaluation_array.sort()
        #         next_move_evaluation_array = next_move_evaluation_array[-10:]
        #         level_1_evals.append(next_move_evaluation_array)
        #         counter_i = 0
        #         counter_j = 0
        #         for i in next_move_evaluation_array:
        #                 pieces = self.game.get_original_pieces(self.game.board, i[1][0], i[1][1], i[2][0], i[2][1])
        #                 self.game.execute_turn(i[1][0], i[1][1], i[2][0], i[2][1])
        #                 array_level_one = next_move_evaluation_array
        #                 # print(self.game.board)
        #                 further_move_evaluation_array = self.all_possible_moves(self.game.board)
        #                 further_move_evaluation_array.sort()
        #                 # print(further_move_evaluation_array)
        #                 further_move_evaluation_array = further_move_evaluation_array[-10:]
        #                 # print(further_move_evaluation_array)
        #                 level_1_evals[0][counter_i].append(further_move_evaluation_array)
        #                 # print(level_1_evals[0][3])
        #                 counter_i += 1
        #                 # self.game.revert_turn(array_level_one[counter_i][1][0], array_level_one[counter_i][1][1], array_level_one[counter_i][2][0], array_level_one[counter_i][2][1], pieces[0], pieces[1])
        #                 # print(self.game.board)
        #                 for j in level_1_evals:
        #                         # print(self.game.p1_turn)
        #                         pieces = self.game.get_original_pieces(self.game.board, j[counter_j][1][0], j[counter_j][1][1], j[counter_j][2][0], j[counter_j][2][1])
        #                         self.game.execute_turn(j[counter_j][1][0], j[counter_j][1][1], j[counter_j][2][0], j[counter_j][2][1])
        #                         # print(self.game.p1_turn)
        #                         # print(j[0][counter_i + 2][counter_j - 3][1][0])
        #                         # print(j[0][4])
        #
        #                         self.game.execute_turn(j[0][counter_j + 3][0][1][0], j[0][counter_j + 3][0][1][1], j[0][counter_j + 3][0][2][0], j[0][counter_j + 3][0][2][1]) # need to fix
        #                         # print(self.game.board)
        #                         array_level_two = next_move_evaluation_array
        #                         even_further_move_evaluation_array = self.all_possible_moves(self.game.board)
        #                         even_further_move_evaluation_array.sort()
        #                         # print(even_further_move_evaluation_array)
        #                         even_further_move_evaluation_array = even_further_move_evaluation_array[-10:]
        #                         # print(j)
        #                         j[counter_j][counter_j + 3].append(even_further_move_evaluation_array)
        #                         # print(j[0][counter_j][counter_j - 3])
        #                         # print(j)
        #                         # J CONTAINS 3 levels of moves, nested arrays. [[score, [coords from], [coords to], [ALL POSSIBLE MOVES]] ]
        #                         # each of the ALL POSSIBLE MOVES has the form [score, [coords from], [coords to]]
        #                         counter_j += 1
        #                         self.game.revert_turn(array_level_two[counter_j][1][0], array_level_two[counter_j][1][1], array_level_two[counter_j][2][0], array_level_two[counter_j][2][1], pieces[0], pieces[1])
        #                         self.game.revert_turn(array_level_one[counter_i][1][0], array_level_one[counter_i][1][1], array_level_one[counter_i][2][0], array_level_one[counter_i][2][1], pieces[0], pieces[1])
        #         print(level_1_evals)
        #         return "YO"
        def minimax(self):
            next_move_evaluation_array = self.all_possible_moves(self.game.board)
            next_move_evaluation_array.sort()
            next_move_evaluation_array = next_move_evaluation_array[-10:]
            level_1_evals = next_move_evaluation_array
            counter = 0
            for i in level_1_evals:
                gameception = copy.deepcopy(self.game)
                gameception.execute_turn(i[1][0], i[1][1], i[2][0], i[2][1])
                further_move_evaluation_array = self.all_possible_moves(gameception.board)
                further_move_evaluation_array.sort()
                further_move_evaluation_array = further_move_evaluation_array[-10:]
                level_1_evals[counter].append(max(further_move_evaluation_array))
                counter += 0
            return (level_1_evals)

        def available_moves(self, board):
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if isinstance(board[i][j], Piece):
                                        if self.game.p1_turn == True:
                                                if board[i][j].colour == "White":
                                                        # print([self.game.board[i][j].colour, self.game.board[i][j].name, i,j])
                                                        array.append([[i,j], board[i][j].available_moves(board, i, j)])
                                        elif self.game.p1_turn == False:
                                                if board[i][j].colour == "Black":
                                                        array.append([[i,j], board[i][j].available_moves(board, i, j)])
                # array = list(filter(lambda a: a != [], array)) # removes empty arrays from available moves array
                # print(array)
                return array
