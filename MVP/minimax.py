from piece import Piece
import copy
from random import random

class Minimax:
        def __init__(self, game):
                self.game = game
                
        
        def execute_turn(self):
                return []

        def all_possible_moves(self):
                evaluation_array = []
                all_available_moves = self.available_moves()
                for moveset in all_available_moves:
                        if len(moveset[1]) != 0:
                                for j in moveset[1]:
                                        pieces = self.game.get_original_pieces(self.game.board.board, moveset[0][0], moveset[0][1], j[0], j[1])
                                        self.game.execute_turn(moveset[0][0], moveset[0][1], j[0], j[1])
                                        score = self.evaluate_position(self.game.board.board)     
                                        evaluation_array.append([score, moveset[0], [j[0],j[1]]])
                                        self.game.revert_turn(moveset[0][0], moveset[0][1], j[0], j[1], pieces[0], pieces[1])
                # print(evaluation_array)
                return evaluation_array
        
        def minimax(self, depth):
                # 1) get avail moves
                # 2) get move values
                # 3) get MORE all_possible_move_valuess from all_possible_move_valuess
                # print(self.game.show_board("1", "2"))
                all_evals = []
                a = 0
                while a < depth:
                        last_known_board = copy.deepcopy(self.game.board.board)
                        # print(last_known_board)
                        next_move_evaluation_array = self.all_possible_moves()
                        # print(next_move_evaluation_array)
                        for i in next_move_evaluation_array:
                                pieces = self.game.get_original_pieces(last_known_board, i[1][0], i[1][1], i[2][0], i[2][1])
                                # print([pieces, i])
                                self.game.execute_turn(i[1][0], i[1][1], i[2][0], i[2][1])
                                all_evals.append(self.all_possible_moves())
                                self.game.revert_turn(i[1][0], i[1][1], i[2][0], i[2][1], pieces[0], pieces[1])
                        a += 1
                print(len(all_evals) * len(all_evals[0]))
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


        