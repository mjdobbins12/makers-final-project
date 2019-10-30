import chessboard

class Game:

    def __init__(self, p1_name, p2_name):
        self.board = chessboard.ChessBoard()
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_turn = True
        self.log = []

    def execute_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        try:
            self.board.move(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.log_turn(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.p1_turn = not self.p1_turn
            return 'valid move'
        except:
            return 'invalid move'

    def log_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        color = 'White' if self.p1_turn else 'Black'
        self.log.append([color, turn_from_x, turn_from_y, turn_to_x, turn_to_y])
