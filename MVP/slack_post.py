import os
import slack
import piece
import coordinate_conversion
import game
from io import StringIO
import sys

class SlackOutput:
    def __init__(self):
        self.client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
        self.bot_id = None
        self.game = None

    def post(self, client, text, channel = '#chess'):
        output = client.chat_postMessage(
        channel='#chess',
        text=text,
        as_user = True)
        if self.bot_id == None:
            self.bot_id = output['message']['bot_id']

    def start_listen(self):
        self.post(self.client, 'Hi I am Chessy! Enter start to start the game')
        @slack.RTMClient.run_on(event='message')
        def run_game(**payload):
            data = payload['data']
            web_client = payload['web_client']
            rtm_client = payload['rtm_client']
            if 'start' in data.get('text', []) and data.get('bot_id') == None:
                members = web_client.conversations_members(channel='CQ5DE12DV')['members']
                user = data['user']
                self.__launch_game(web_client, user, members)

                self.post(web_client, self.__output_board())
            if self.game != None and data.get('bot_id') == None and data.get('text', [])!= 'start' and data.get('text', [])!= 'stop':
                print(data)

                try:
                    self.__parse_and_execute_move(data.get('text', []))
                except:
                    self.post(web_client, 'Invalid move - try again')
                self.__check_for_checkmate()
                self.post(web_client, self.__output_board())

            if self.game != None and data.get('bot_id') == None and data.get('text', [])== 'stop':
                self.post(web_client, 'Ok, stopped the game. Enter start to start a new game!')

                #checking if the player is allowed to give the instruction
                #can run only one game concurrently

        slack_token = os.environ["SLACK_API_TOKEN"]
        rtm_client = slack.RTMClient(token=slack_token)
        rtm_client.start()



    # private methods

    def __output_board(self):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        self.__announce_whose_turn()
        self.__show_board(self.game.board, self.game.player_1.name, self.game.player_2.name)
        result_string = result.getvalue()
        sys.stdout = old_stdout
        return result_string

    def __show_board(self, board, p1_name, p2_name):
        print('')
        print(f"<@{p1_name}>")
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
        print(f"<@{p1_name}>")
        print('')
        self.__print_taken_pieces_ifany()

    def __announce_whose_turn(self):
        if self.game.p1_turn == True:
            print(f"<@{self.game.player_1.name}>" + "'s turn!")
        else:
            print(f"<@{self.game.player_2.name}>" + "'s turn!")

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

    def __launch_game(self, web_client, user, members):
        self.post(web_client, f" <@{user}> launched the game! Enter moves in this format: a2-a4")
        self.post(web_client, 'Enter stop to stop the game')

        self.post(web_client, f" <@{members[0]}> vs <@{members[1]}>")
        self.game = game.Game(members[0], members[1])

    def __parse_and_execute_move(self, text):
        turn_from = text.split('-')[0]
        turn_to = text.split('-')[1]
        move = coordinate_conversion.Convert().coordinates(turn_from, turn_to)
        if self.game.execute_turn(move[0],move[1],move[2],move[3]) == 'invalid move':
            self.post(web_client, 'Invalid move - try again')

    def __check_for_checkmate(self):
        if self.game.is_checkmate():
            if self.game.p1_turn:
              self.post(web_client, f"Checkmate, <@{self.game.player_2.name}> wins!")
            elif self.game.p1_turn == False:
              self.post(web_client, f"Checkmate, <@{self.game.player_2.name}> wins!")

test = SlackOutput()
test.start_listen()
