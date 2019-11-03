import piece
import coordinate_conversion
import game
import slack_post
from io import StringIO
import sys
import os


class UI:
    def __init__(self):
        self.game = ''

    def start(self):
        names = self.get_names()
        self.game = game.Game(names[0], names[1])
        self.loop_turns()

    def get_names(self):
        names = []
        names.append(input("Enter player 1 name: "))
        names.append(input("Enter player 2 name: "))
        print(names[0] + ' vs. ' + names[1])
        return names

    def loop_turns(self):
          while True:
              self.__output_slack() # outputs to slack if ENV variable with token is found
              self.show_board(self.game.board, self.game.player_1.name, self.game.player_2.name)
              if self.game.is_checkmate():
                  if self.game.p1_turn:
                    print(f'Checkmate, {self.game.player_2.name} wins! ')
                    break
                  elif self.game.p1_turn == False:
                    print(f'Checkmate, {self.game.player_1.name} wins!')
                    break
              self.announce_whose_turn()
              print('Enter quit to stop the game')
              turn_from = input('Please enter square to move FROM: ')
              if turn_from == 'quit': break
              turn_to = input('Please enter square to move TO: ')
              if turn_to == 'quit': break
              move = coordinate_conversion.Convert().coordinates(turn_from, turn_to)
              if self.game.execute_turn(move[0],move[1],move[2],move[3]) == 'invalid move':
                  print('Invalid move - try again')


    def announce_whose_turn(self):
        if self.game.p1_turn == True:
            print(self.game.player_1.name + "'s turn!")
        else:
            print(self.game.player_2.name + "'s turn!")


    def show_board(self, board, p1_name, p2_name):
        print('')
        print(p2_name)
        print("| a | b | c | d | e | f | g | h |")
        print("_" * 33)
        ind = 8
        for row in board.board:
            x = "|"
            for el in row:
                if isinstance(el, piece.Piece):
                    x += f" {el.symbol} |"
                else:
                    x += f" {el} |"
            x += f" {ind}"
            ind -= 1
            print(x)
            print("-" * 33)
        print(p1_name)
        print('')
        self.__print_taken_pieces_ifany()


    # private methods

    def __print_taken_pieces_ifany(self):
        if len(self.game.player_2.taken_pieces) > 0:
            x = 'Taken:'
            for el in self.game.player_2.taken_pieces:
                x += f" {el.symbol}"
            print(x)
        if len(self.game.player_1.taken_pieces) > 0:
            x = 'Taken:'
            for el in self.game.player_1.taken_pieces:
                x += f" {el.symbol}"
            print(x)

    def __output_slack(self):
        if 'SLACK_API_TOKEN' in os.environ:
            old_stdout = sys.stdout
            result = StringIO()
            sys.stdout = result
            self.announce_whose_turn()
            self.show_board(self.game.board, self.game.player_1.name, self.game.player_2.name)
            result_string = result.getvalue()
            slack = slack_post.SlackOutput()
            slack.print(result_string)
            sys.stdout = old_stdout
