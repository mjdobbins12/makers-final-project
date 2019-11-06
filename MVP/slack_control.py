import os
import slack
import coordinate_conversion
import game
import minimax
from slack_board_display import SlackBoardDisplay

class SlackControl:

    def __init__(self, channel):
        self.game = None
        self.names_of_players = []
        self.game_mode = None
        self.slack_board_display = SlackBoardDisplay()
        self.channel = channel

    def check_for_start(self, web_client, data):
        if data.get('text', []) == 'start' and data.get('bot_id') == None and self.game == None:
            self.names_of_players = [data['user']]
            print(self.channel)
            self.post(web_client, f" <@{data['user']}> wants to play! Enter join to start the game!")

    def check_for_join(self, web_client, data):
        if data.get('text', []) == 'join' and data.get('bot_id') == None and len(self.names_of_players) == 1:
            self.names_of_players.append(data['user'])
            if self.game_mode not in [None, 'in_choosing']:
                self.__launch_game(web_client, self.names_of_players[0], self.names_of_players, ruleset = self.game_mode)
            else:
                self.__launch_game(web_client, self.names_of_players[0], self.names_of_players)

    def check_for_AI(self, web_client, data):
        if data.get('text', []) == 'AI please!' and data.get('bot_id') == None and len(self.names_of_players) == 1:
            print(data)
            self.names_of_players.append('AI')
            self.__launch_game(web_client, self.names_of_players[0], self.names_of_players, ruleset = self.game_mode)

    def check_for_mode(self, web_client, data):
        if data.get('text', []) == "let's make this more interesting!" and len(self.names_of_players) == 1 and data.get('user',[]) in self.names_of_players:
            self.game_mode = 'in_choosing'
            self.__announce_game_modes(web_client, data['user'])

    def check_for_mode_set(self, web_client, data):
        if data.get('text', []) == "Can I play daddy?" and len(self.names_of_players) == 1 and data.get('user',[]) in self.names_of_players:
            self.game_mode = 'many_queens'
            self.post(web_client, 'Yes you can!')
        if data.get('text', []) == "Piece of cake" and len(self.names_of_players) == 1 and data.get('user',[]) in self.names_of_players:
            self.game_mode = 'random_pieces'
            self.post(web_client, 'Pieces will be random, but not the cake (0)!')
        if data.get('text', []) == "Damn I'm good" and len(self.names_of_players) == 1 and data.get('user',[]) in self.names_of_players:
            self.game_mode = 'ex_bishops'
            self.post(web_client, 'Pieces will be random, but not the cake (0)!')
        # could refactor into method that takes the mode name and what to pass on to game_mode and a response

    def check_for_moves(self, web_client, data):
        if self.game != None and data.get('text', []) not in ['start', 'stop', 'join'] and data.get('user',[]) in self.names_of_players:
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
        # this could use some refactor - but needs to retain the AI move trigger after processing the player move

    def check_for_stop(self, web_client, data):
        if self.game != None and data.get('text', [])== 'stop' and data['user'] in self.names_of_players:
            self.post(web_client, 'Ok, stopped the game. Enter start to start a new game!')
            self.game = None
            self.names_of_players = []
            self.game_mode = None
            # maybe these 3 can all be set to None?

    def post(self, client, text):
        output = client.chat_postMessage(
            channel = self.channel,
            text = text,
            username = 'Chessy')
            # as_user = True)

    # private methods

    def __launch_game(self, web_client, user_launched_game, names, ruleset = 'standard'):
        self.game = game.Game(names[0], names[1], ruleset)
        self.__announce_start(web_client, user_launched_game, names)
        self.post(web_client, self.slack_board_display.output_board(self.game))

    def __parse_and_execute_move(self, web_client, text):
        turn_from = text.split('-')[0].lower()
        turn_to = text.split('-')[1].lower()
        move = coordinate_conversion.Convert().coordinates(turn_from, turn_to)
        response = self.game.execute_turn(move[0],move[1],move[2],move[3])
        if response == 'invalid move':
            self.post(web_client, 'Invalid move - try again')
        if response == 'excommunication':
            self.post(web_client, 'Oh no! bishops were excommunicated!')
        if response == 'rooksale':
            self.post(web_client, 'Oh no! rooks were sold off! They can't move for 5 turns, while the transaction completes.')
        if response == 'rooksign':
            self.post(web_client, 'Sale complete! All Rooks can move again.')
        if response == 'knight_honour':
            self.post(web_client, 'Knights receive the hightest honour! They can now move in any direction, for 2 turns.')
        if response == 'knight_normal':
            self.post(web_client, 'The fun has worn off! Knights can no longer move in any direction')
        # canb add more resonses here

    def __AI_move(self):
        AI_move = minimax.Minimax(self.game).minimaxRoot(2, self.game.board, True)
        print(AI_move)
        self.game.execute_turn(AI_move[0][0],AI_move[0][1],AI_move[1][0],AI_move[1][1])

    def __check_for_checkmate(self):
        if self.game.is_checkmate():
            if self.game.p1_turn:
              self.post(web_client, f"Checkmate, <@{self.game.player_2.name}> wins!")
            elif self.game.p1_turn == False:
              self.post(web_client, f"Checkmate, <@{self.game.player_1.name}> wins!")
            self.game = None

    def __correct_players_turn(self, data):
        if self.game.p1_turn:
            if data['user'] == self.game.player_1.name:
                return True
        else:
            if data['user'] == self.game.player_2.name:
                return True
        return False

    def __announce_start(self, web_client, user_launched_game, names):
        self.post(web_client, f" <@{user_launched_game}> launched the game! Enter moves in this format: a2-a4")
        self.post(web_client, 'Enter stop to stop the game')
        self.post(web_client, f" <@{names[0]}> vs <@{names[1]}>")

    def __announce_game_modes(self, web_client, user):
        self.post(web_client, f" Ok <@{user}>! Make your choice:")
        self.post(web_client, ' - Can I play daddy?')
        self.post(web_client, ' - Piece of cake')
        self.post(web_client, " - Damn I'm good")
