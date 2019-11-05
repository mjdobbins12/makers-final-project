import os
import slack
import coordinate_conversion
import game
from io import StringIO
import sys
import minimax
from slack_board_display import SlackBoardDisplay


class SlackControl:

    def __init__(self):
        self.game = None
        self.names_of_players = []
        self.game_mode = None
        self.slack_board_display = SlackBoardDisplay()
        # initiate game from here??

    def __check_for_moves(self, web_client, data):
        if self.game != None and data.get('text', []) not in ['start', 'stop', 'join'] and data['user'] in self.names_of_players:
            print(data)
            if self.__correct_players_turn(data):
                try:
                    self.__parse_and_execute_move(web_client, data.get('text', []))
                except:
                    self.post(web_client, 'Invalid move - try again')
                self.__check_for_checkmate()
                self.post(web_client, self.slack_board_display.output_board(self.game))
            if self.game.player_2.name == 'AI' and self.game.p1_turn == False:
                self.__AI_move()
                self.__check_for_checkmate()
                self.post(web_client, self.slack_board_display.output_board(self.game))
            # needs game, slack_board_display (can be instantiated), names of players

    def __AI_move(self):
        AI_move = minimax.Minimax(self.game).minimax()
        print(AI_move)
        self.game.execute_turn(AI_move[0][0],AI_move[0][1],AI_move[1][0],AI_move[1][1])
        # private method to check for moves

    def __check_for_stop(self, web_client, data):
        if self.game != None and data.get('text', [])== 'stop' and data['user'] in self.names_of_players:
            print(data)
            self.post(web_client, 'Ok, stopped the game. Enter start to start a new game!')
            self.game = None
            self.names_of_players = []
            self.game_mode = None

            # needs game, slack_board_display (can be instantiated), names of players


    def __launch_game(self, web_client, user_launched_game, names, ruleset = 'standard'):
        self.game = game.Game(names[0], names[1], ruleset)
        self.post(web_client, f" <@{user_launched_game}> launched the game! Enter moves in this format: a2-a4")
        self.post(web_client, 'Enter stop to stop the game')
        self.post(web_client, f" <@{names[0]}> vs <@{names[1]}>")
        self.post(web_client, self.slack_board_display.output_board(self.game))

    def __parse_and_execute_move(self, web_client, text):
        turn_from = text.split('-')[0].lower()
        turn_to = text.split('-')[1].lower()
        move = coordinate_conversion.Convert().coordinates(turn_from, turn_to)
        if self.game.execute_turn(move[0],move[1],move[2],move[3]) == 'invalid move':
            self.post(web_client, 'Invalid move - try again')

    def __check_for_checkmate(self):
        if self.game.is_checkmate():
            if self.game.p1_turn:
              self.post(web_client, f"Checkmate, <@{self.game.player_2.name}> wins!")
            elif self.game.p1_turn == False:
              self.post(web_client, f"Checkmate, <@{self.game.player_1.name}> wins!")
            self.game = None
        # belongs to move, needs game

    def __correct_players_turn(self, data):
        if self.game.p1_turn:
            if data['user'] == self.game.player_1.name:
                return True
        else:
            if data['user'] == self.game.player_2.name:
                return True
        return False
        # belongs to move, needs game

    def __intro_chessy(self):
        output = 'Hi I am Chessy!\n'
        output += 'Let others play their games, the game of kings is still the ♔ of games!\n'
        output += 'Enter start to start the game!\n'
        return output
