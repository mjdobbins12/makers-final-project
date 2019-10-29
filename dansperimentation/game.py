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
            turn_from_x = input('Please enter column to move FROM: ')
            if turn_from_x == 'quit': break
            turn_from_y = input('Please enter row to move FROM: ')
            if turn_from_y == 'quit': break
            turn_to_x = input('Please enter column to move TO: ')
            if turn_to_x == 'quit': break
            turn_to_y = input('Please enter row to move TO: ')
            if turn_to_y == 'quit': break
            self.execute_turn(turn_from_x, turn_from_y, turn_to_x, turn_to_y)

    def announce_whose_turn(self):
        if self.p1_turn == True:
            print(self.p1_name + "'s turn!")
        else:
            print(self.p2_name + "'s turn!")

    def execute_turn(self, turn_from_x, turn_from_y, turn_to_x, turn_to_y):
        self.board.move(int(turn_from_y), int(turn_from_x), int(turn_to_y), int(turn_to_x))
        self.board.show_board(self.p1_name, self.p2_name)
        self.p1_turn = not self.p1_turn
