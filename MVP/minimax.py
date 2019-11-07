from piece import Piece
import copy
from random import random
from heuristics import Heuristics

class Minimax:
        def __init__(self, game):
                self.game = copy.deepcopy(game)

        def minimaxRoot(self, depth, board,isMaximizing):
                possibleMoves = self.available_moves(board)
                bestMove = -9999
                secondBest = -9999
                thirdBest = -9999
                bestMoveFinal = None
                for x in possibleMoves:
                        move = x
                        original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                        self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1])
                        value = max(bestMove, self.minimax(depth - 1, board, not isMaximizing))
                        self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                        # print(value)
                        if( value > bestMove):
                                # print("Best score: " ,str(bestMove))
                                # print("Best move: ",str(bestMoveFinal))
                                # print("Second best: ", str(secondBest))
                                thirdBest = secondBest
                                secondBest = bestMove
                                bestMove = value
                                bestMoveFinal = move
                # print(bestMoveFinal)
                # print(bestMove)
                return bestMoveFinal

        def minimax(self, depth, board, is_maximizing):
                possibleMoves = self.available_moves(self.game.board)
                # print(possibleMoves)
                if(depth == 0):
                        heur = Heuristics(self.game)
                        return heur.evaluate(board)

                if(is_maximizing):
                        bestMove = -9999
                        for x in possibleMoves:
                                move = x
                                original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                                self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1])
                                bestMove = max(bestMove, self.  minimax(depth - 1, board, not is_maximizing))
                                self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                        return bestMove
                else:
                        bestMove = 9999
                        for x in possibleMoves:
                                move = x
                                original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                                self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1])
                                bestMove = min(bestMove, self.minimax(depth - 1, board, not is_maximizing))
                                self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                        return bestMove




        def available_moves(self, board):
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if isinstance(board[i][j], Piece):
                                        if self.game.p1_turn == True:
                                                if board[i][j].colour == "White":
                                                        for k in board[i][j].available_moves(board, i, j):
                                                            if self.game.check_if_self_in_check(i, j, k[0], k[1]) != 'invalid move':
                                                                array.append([[i,j], k])
                                        elif self.game.p1_turn == False:
                                                if board[i][j].colour == "Black":
                                                        for k in board[i][j].available_moves(board, i, j):
                                                            if self.game.check_if_self_in_check(i, j, k[0], k[1]) != 'invalid move':
                                                                array.append([[i,j], k])
                # array = list(filter(lambda a: a != [], array)) # removes empty arrays from available moves array
                # print(array)
                return array
