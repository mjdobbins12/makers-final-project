from piece import Piece

class Minimax:
        def __init__(self, game):
                self.game = game
        
        def execute_turn(self):
                return []

        def move_value(self):
                return []

                moves = self.available_moves()
                for piece_moves in moves:
                        for move in piece_moves:
                                return "YO"



        def available_moves(self):
                array = []
                for i in range(0,8):
                        for j in range(0,8):
                                if isinstance(self.game.board.board[i][j], Piece):
                                        if self.game.p1_turn == True:
                                                if self.game.board.board[i][j].colour == "White":
                                                        print([self.game.board.board[i][j].colour, self.game.board.board[i][j].name, i,j])
                                                        array.append(self.game.board.board[i][j].available_moves(self.game.board.board, i, j))
                                        elif self.game.p1_turn == False:
                                                if self.game.board.board[i][j].colour == "Black":
                                                        print([self.game.board.board[i][j].colour, self.game.board.board[i][j].name, i,j])
                                                        array.append(self.game.board.board[i][j].available_moves(self.game.board.board, i, j))
                array = list(filter(lambda a: a != [], array)) # removes empty arrays from available moves array
                return array


        