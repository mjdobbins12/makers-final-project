from piece import Piece

class Draw:
    def __init__(self, game):
        self.game = game
        if game.p1_turn == True:
            self.current_player = game.player_1.colour
        else:
            self.current_player = game.player_2.colour

    def is_draw(self):
        return any([
            self.__is_stalemate()
            ])

    def __is_stalemate(self):
        legal_moves = []
        for i in range(0,8):
            for j in range(0,8):
                if isinstance(self.game.board.board[i][j], Piece) and self.game.board.board[i][j].colour == self.current_player:
                    legal_moves.append(self.game.board.board[i][j].available_moves(self.game.board.board, i, j))
        print(legal_moves)
        print(self.current_player)
        if len(legal_moves) == 0:
            return True
        else:
            return False
