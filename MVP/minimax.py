from piece import Piece
import copy
from random import random

class Minimax:
        def __init__(self, game):
                self.game = game
                
        
        def execute_turn(self):
                return []

        def move_value(self):
                evaluation_array = []
                all_available_moves = self.available_moves()
                original_board = copy.deepcopy(self.game.board.board)
                for moveset in all_available_moves:
                        if len(moveset[1]) != 0:
                                for j in moveset[1]:
                                        self.game.execute_turn(moveset[0][0], moveset[0][1], j[0], j[1])
                                        score = self.evaluate_position(self.game.board.board)     
                                        evaluation_array.append([score, moveset[0], [j[0],j[1]]])
                                self.game.board.board = original_board
                # print(evaluation_array)
                return evaluation_array

        def minimax(self, depth):
                # 1) get avail moves
                # 2) get move values
                # 3) get MORE move_values from move_values
                all_evals = []
                a = 0
                while a < depth:
                        last_known_board = copy.deepcopy(self.game.board.board)
                        next_move_evaluation_array = self.move_value()
                        for i in next_move_evaluation_array:
                                self.game.execute_turn(i[1][0], i[1][1], i[2][0], i[2][1])
                                all_evals.append(self.move_value())
                                # self.game.board.board = last_known_board
                        a += 1
                all_evals = sorted()
                print(all_evals)
                return all_evals






        def available_moves(self):
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if isinstance(self.game.board.board[i][j], Piece):
                                        if self.game.p1_turn == True:
                                                if self.game.board.board[i][j].colour == "White":
                                                        # print([self.game.board.board[i][j].colour, self.game.board.board[i][j].name, i,j])
                                                        array.append([[i,j], self.game.board.board[i][j].available_moves(self.game.board.board, i, j)])
                                        elif self.game.p1_turn == False:
                                                if self.game.board.board[i][j].colour == "Black":
                                                        array.append([[i,j], self.game.board.board[i][j].available_moves(self.game.board.board, i, j)])
                # array = list(filter(lambda a: a != [], array)) # removes empty arrays from available moves array
                return array

        def evaluate_position(self, board):
                return round(random() * 100)


        