class Minimax:
        def __init__(self, game, p1_turn):
                self.board = game.board.board
                self.game = game
                if p1_turn == True:
                        self.turn = "White"
                else:
                        self.turn = "Black"
        
        def execute_turn(self):
                return []