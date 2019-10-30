import chessboard

class Game:

    def __init__(self):
        self.board = chessboard.ChessBoard()
        self.p1_name = 'undefined'
        self.p2_name = 'undefined'
        self.p1_turn = True

    def start(self):
        self.get_names()
        self.run_turns()

    def get_names(self):
        self.p1_name = input("Enter player 1 name: ")
        self.p2_name = input("Enter player 2 name: ")
        print(self.p1_name + ' vs. ' + self.p2_name)
        self.board.show_board(self.p1_name, self.p2_name)

    def run_turns(self):
          while True:
              self.announce_whose_turn()
              print('Enter quit to stop the game')
              turn_from = input('Please enter square to move FROM: ')
              if turn_from == 'quit': break
              turn_to = input('Please enter square to move TO: ')
              if turn_to == 'quit': break
              self.convert_coordinates(turn_from, turn_to)

    def convert_coordinates(self, turn_from, turn_to):
        columns = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }
        turn_from_y = 7 - (int(turn_from[1]) - 1)
        turn_from_x = columns[turn_from[0]]
        turn_to_y = 7 - (int(turn_to[1]) - 1)
        turn_to_x = columns[turn_to[0]]
        self.execute_turn(turn_from_x, turn_from_y, turn_to_x, turn_to_y)

    def announce_whose_turn(self):
        if self.p1_turn == True:
            print(self.p1_name + "'s turn!")
        else:
            print(self.p2_name + "'s turn!")

    def execute_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        try:
            self.board.move(int(turn_from_x), int(turn_from_y), int(turn_to_x), int(turn_to_y))
            self.p1_turn = not self.p1_turn
        except ValueError:
            print('Invalid move - try again')
        self.board.show_board(self.p1_name, self.p2_name)
