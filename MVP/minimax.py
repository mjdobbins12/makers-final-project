from piece import Piece
import copy
from random import random
from heuristics import Heuristics

class Minimax:
        def __init__(self, game):
                self.game = game
                
        
        def execute_turn(self):
                return []

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
                # print(evaluation_array)
                return evaluation_array
        
        def minimax(self):
                # 1) get avail moves
                # 2) get move values
                # 3) get MORE all_possible_move_valuess from all_possible_move_valuess
                # print(self.game.show_board("1", "2"))
                all_evals = []
                a = 0
                next_move_evaluation_array = self.all_possible_moves(self.game.board.board)
                next_move_evaluation_array = max(next_move_evaluation_array)
                all_evals.append(next_move_evaluation_array)
                # print(next_move_evaluation_array)
                #         # print(last_known_board)
                for i in next_move_evaluation_array:
                        pieces = self.game.get_original_pieces(self.game.board.board, next_move_evaluation_array[1][0], next_move_evaluation_array[1][1], next_move_evaluation_array[2][0], next_move_evaluation_array[2][1])
                        self.game.execute_turn(next_move_evaluation_array[1][0], next_move_evaluation_array[1][1], next_move_evaluation_array[2][0], next_move_evaluation_array[2][1])
                        # print(self.game.board.board)
                        for_revert_turn1 = next_move_evaluation_array
                        # all_moves = self.all_possible_moves(self.game.board.board)
                        # all_evals.append([all_moves]) # returns best move option
                        next_move_evaluation_array = self.all_possible_moves(self.game.board.board)
                        # print(next_move_evaluation_array)
                        next_move_evaluation_array = max(next_move_evaluation_array)
                        all_evals.append(next_move_evaluation_array)
                        # print([pieces, i, self.game.p1_turn])
                        for i in next_move_evaluation_array:
                                pieces = self.game.get_original_pieces(self.game.board.board, next_move_evaluation_array[1][0], next_move_evaluation_array[1][1], next_move_evaluation_array[2][0], next_move_evaluation_array[2][1])
                                # print([pieces, i])
                                self.game.execute_turn(next_move_evaluation_array[1][0], next_move_evaluation_array[1][1], next_move_evaluation_array[2][0], next_move_evaluation_array[2][1])
                                for_revert_turn2 = next_move_evaluation_array
                                # all_moves = self.all_possible_moves(self.game.board.board)
                                # all_evals.append([all_moves]) # returns best move option
                                next_move_evaluation_array = self.all_possible_moves(self.game.board.board)
                                next_move_evaluation_array = max(next_move_evaluation_array)
                                all_evals.append(next_move_evaluation_array)
                                self.game.revert_turn(for_revert_turn2[1][0], for_revert_turn2[1][1], for_revert_turn2[2][0], for_revert_turn2[2][1], pieces[0], pieces[1])
                                self.game.revert_turn(for_revert_turn1[1][0], for_revert_turn1[1][1], for_revert_turn1[2][0], for_revert_turn1[2][1], pieces[0], pieces[1])
                                return [next_move_evaluation_array[1], next_move_evaluation_array[2]]




        def available_moves(self, board):
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if isinstance(board[i][j], Piece):
                                        if self.game.p1_turn == True:
                                                if board[i][j].colour == "White":
                                                        # print([self.game.board.board[i][j].colour, self.game.board.board[i][j].name, i,j])
                                                        array.append([[i,j], board[i][j].available_moves(board, i, j)])
                                        elif self.game.p1_turn == False:
                                                if board[i][j].colour == "Black":
                                                        array.append([[i,j], board[i][j].available_moves(board, i, j)])
                # array = list(filter(lambda a: a != [], array)) # removes empty arrays from available moves array
                # print(array)
                return array

        def evaluate_position(self, board):
                return round(random() * 100)


        