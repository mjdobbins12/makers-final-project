from piece import Piece
import copy
from random import random
from heuristics import Heuristics

class Minimax:
        def __init__(self, game):
                self.game = copy.deepcopy(game)

        def minimaxRoot(self, depth, board, isMaximizing):
                possibleMoves = self.available_moves(board)
                if(isMaximizing):
                        bestMove = -9999
                        bestMoveFinal = None
                        for x in possibleMoves:
                                move = x
                                original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                                if self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1]) == 'valid move':
                                        value = max(bestMove, self.minimax(depth - 1, board, not isMaximizing))
                                        self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                                else:
                                        value = bestMove
                                if( value > bestMove):
                                        bestMove = value
                                        bestMoveFinal = move
                        return bestMoveFinal
                else: 
                        bestMove = 9999
                        bestMoveFinal = None
                        for x in possibleMoves:
                                move = x
                                original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                                if self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1]) == 'valid move':
                                        value = min(bestMove, self.minimax(depth - 1, board, not isMaximizing))
                                        self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                                else:
                                        value = bestMove
                                if( value < bestMove):
                                        bestMove = value
                                        bestMoveFinal = move
                        return bestMoveFinal 

        def minimax(self, depth, board, is_maximizing):
                possibleMoves = self.available_moves(self.game.board)
                if(depth == 0):
                        heur = Heuristics(self.game)
                        return heur.evaluate(board)

                if(is_maximizing):
                        bestMove = -9999
                        for x in possibleMoves:
                                move = x
                                original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                                if self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1]) == 'valid move':
                                        bestMove = max(bestMove, self.minimax(depth - 1, board, not is_maximizing))
                                        self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                                else:
                                        bestMove = -9999
                        return bestMove
                else:
                        bestMove = 9999
                        for x in possibleMoves:
                                move = x
                                original_pieces = self.game.get_original_pieces(board, x[0][0], x[0][1], x[1][0], x[1][1])
                                if self.game.execute_turn(x[0][0], x[0][1], x[1][0], x[1][1]) == 'valid move':
                                        bestMove = min(bestMove, self.minimax(depth - 1, board, not is_maximizing))
                                        self.game.revert_turn(x[0][0], x[0][1], x[1][0], x[1][1], original_pieces[0], original_pieces[1])
                                else:
                                        bestMove = 9999
                        # print(bestMove)
                        return bestMove




        def available_moves(self, board):
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if isinstance(board[i][j], Piece):
                                        if self.game.p1_turn == True:
                                                if board[i][j].colour == "White":
                                                        for k in board[i][j].available_moves(board, i, j):
                                                            # if self.game.check_if_self_in_check(i, j, k[0], k[1]) != 'invalid move':
                                                                array.append([[i,j], k])
                                        elif self.game.p1_turn == False:
                                                if board[i][j].colour == "Black":
                                                        for k in board[i][j].available_moves(board, i, j):
                                                            # if self.game.check_if_self_in_check(i, j, k[0], k[1]) != 'invalid move':
                                                                array.append([[i,j], k])
                return array
