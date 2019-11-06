import coordinate_conversion
import game
import minimax
import standard_rules
from ui_board_display import UIBoardDisplay

class UI:
    def __init__(self):
        self.game = ''
        self.ruleset = standard_rules.StandardRules()
        self.board_display = UIBoardDisplay()

    def start(self):
        names = self.get_names()
        self.game = game.Game(names[0], names[1])
        self.loop_turns()

    def get_names(self):
        names = []
        names.append(input("Enter player 1 name: "))
        names.append(input("Enter player 2 name. Use AI to play against the computer: "))
        print(names[0] + ' vs. ' + names[1])
        return names

    def loop_turns(self):
        while True:
            self.board_display.show_board(self.game, self.game.board, self.game.player_1.name, self.game.player_2.name)
            if self.checkmate_or_draw(): break
            self.announce_whose_turn()
            if self.game.player_2.name == 'AI' and self.game.p1_turn == False:
                AI_move = minimax.Minimax(self.game).minimax()
                self.game.execute_turn(AI_move[0][0],AI_move[0][1],AI_move[1][0],AI_move[1][1])
            else:
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

    def checkmate_or_draw(self):
        if self.game.is_checkmate():
            if self.game.p1_turn:
                print(f'Checkmate, {self.game.player_2.name} wins! ')
            elif self.game.p1_turn == False:
                print(f'Checkmate, {self.game.player_1.name} wins!')
            return True
        if self.game.is_draw():
            print('Game drawn')
            return True
