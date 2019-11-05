import os
import slack
import piece
import coordinate_conversion
import game
from io import StringIO
import sys

class Slack:

    def __init__(self):
        self.client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
        self.game = None
        self.names_of_players = []
        self.game_mode = '####difficult_level####'

    def post(self, client, text, channel = '#chess'):
        output = client.chat_postMessage(
            channel = channel,
            text = text,
            as_user = True)

    def start_listen(self):
        self.post(self.client, 'Hi I am Chessy!')
        self.post(self.client, 'Let others play their games, the game of kings is still the king of games!')
        self.post(self.client, 'Enter start to start the game')
        @slack.RTMClient.run_on(event='message')
        def run_game(**payload):
            data = payload['data']
            web_client = payload['web_client']
            rtm_client = payload['rtm_client']
            self.__check_for_start(web_client, data)
            self.__check_for_join(web_client, data)
            self.__check_for_moves(web_client, data)
            self.__check_for_stop(web_client, data)
            # self.__check_for_mode(webclient, data)

                #can run only one game concurrently
                #think about how to run in another channel vs. #chess only

        slack_token = os.environ["SLACK_API_TOKEN"]
        rtm_client = slack.RTMClient(token=slack_token)
        rtm_client.start()

    # private methods

    def __check_for_start(self, web_client, data):
        if data.get('text', []) == 'start' and data.get('bot_id') == None and self.game == None:
            print(data)
            self.names_of_players = [data['user']]
            self.post(web_client, f" <@{data['user']}> wants to play! Enter join to start the game!")

    def __check_for_join(self, web_client, data):
        if data.get('text', []) == 'join' and data.get('bot_id') == None and len(self.names_of_players) == 1:
            print(data)
            self.names_of_players.append(data['user'])
            self.__launch_game(web_client, self.names_of_players[0], self.names_of_players)

    def __check_for_mode(self, web_client, data):
        if data.get('text', []) == '####difficult_level####' and len(self.names_of_players) == 1 and data['user'] in self.names_of_players:
            print(data)
            self.game_mode = 'test'
            self.post(web_client, f" <@{data['user']}> set mode ####difficult_level####")

    def __check_for_moves(self, web_client, data):
        if self.game != None and data.get('text', []) not in ['start', 'stop', 'join'] and data['user'] in self.names_of_players:
            print(data)
            if self.__correct_players_turn(data):
                try:
                    self.__parse_and_execute_move(data.get('text', []))
                except:
                    self.post(web_client, 'Invalid move - try again')
                self.__check_for_checkmate()
                self.post(web_client, self.__output_board())

    def __check_for_stop(self, web_client, data):
        if self.game != None and data.get('text', [])== 'stop' and data['user'] in self.names_of_players:
            print(data)
            self.post(web_client, 'Ok, stopped the game. Enter start to start a new game!')
            self.game = None
            self.names_of_players = []

    def __output_board(self):
        result_string = self.__announce_whose_turn()
        result_string +='\n\n\n'
        result_string += f"<@{self.game.player_2.name}>\n"
        result_string += "| a | b | c | d | e | f | g | h |      \n"
        result_string += '________________________\n'
        ind = 8
        for row in self.game.board:
            x = "|"
            for el in row:
                if isinstance(el, piece.Piece):
                    x += f" {el.symbol} |"
                else:
                    x += f" {el}  |"
            x += f" {ind}"
            ind -= 1
            result_string += f"{x}\n"
            result_string += '------------------------------\n'
        result_string += f"<@{self.game.player_1.name}>\n"
        result_string += '\n'
        result_string += self.__list_taken_pieces_ifany()
        return result_string

    def __announce_whose_turn(self):
        if self.game.p1_turn == True:
            return f"<@{self.game.player_1.name}>" + "'s turn!"
        else:
            return f"<@{self.game.player_2.name}>" + "'s turn!"

    def __list_taken_pieces_ifany(self):
        output = '\n'
        if len(self.game.player_2.taken_pieces) > 0:
            output += 'Taken:'
            for el in self.game.player_2.taken_pieces:
                output += f" {el.symbol}"
            output += '\n'
        if len(self.game.player_1.taken_pieces) > 0:
            output += 'Taken:'
            for el in self.game.player_1.taken_pieces:
                output += f" {el.symbol}"
            output += '\n'
        return output

    def __launch_game(self, web_client, user_launched_game, names):
        self.game = game.Game(names[0], names[1])
        self.post(web_client, f" <@{user_launched_game}> launched the game! Enter moves in this format: a2-a4")
        self.post(web_client, 'Enter stop to stop the game')
        self.post(web_client, f" <@{names[0]}> vs <@{names[1]}>")
        self.post(web_client, self.__output_board())

    def __parse_and_execute_move(self, text):
        turn_from = text.split('-')[0]
        turn_to = text.split('-')[1]
        move = coordinate_conversion.Convert().coordinates(turn_from, turn_to)
        self.game.execute_turn(move[0],move[1],move[2],move[3])

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

slack_instance = Slack()
slack_instance.start_listen()
