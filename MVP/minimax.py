class Minimax:
        def __init__(self, board, p1_turn):
                self.board = board
                if p1_turn == True:
                        self.turn = "White"
                else:
                        self.turn = "Black"