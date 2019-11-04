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

    def test(self):
        response = self.client.chat_postMessage(
        channel='#chess',
        text="Hello world!",
        as_user = True)
        assert response["ok"]
        assert response["message"]["text"] == "Hello world!"

    def print(self, text):
        output = self.client.chat_postMessage(
        channel='#chess',
        text=text,
        as_user = True)
        if self.bot_id == None:
            self.bot_id = output['message']['bot_id']

    def start_listen(self):
        self.print('Hi I am Chessy! Enter start to start the game')
        @slack.RTMClient.run_on(event='message')
        def say_hello(**payload):
            data = payload['data']
            web_client = payload['web_client']
            rtm_client = payload['rtm_client']
            if 'start' in data.get('text', []) and data.get('bot_id') == None:
                print(data)
                print(self.bot_id)
                members = web_client.conversations_members(channel='CQ5DE12DV')['members']
                print(members)
                channel_id = data['channel']
                thread_ts = data['ts']
                user = data['user']
                web_client.chat_postMessage(
                    channel=channel_id,
                    text=f" <@{user}> launched the game! Enter moves in this format: a2-a4"
                    )
                web_client.chat_postMessage(
                    channel=channel_id,
                    text=f" <@{members[0]}> vs <@{members[1]}>"
                    )
                self.game = game.Game(f"<@{members[0]}>",f"<@{members[1]}>")
                output = self.__output_board()
                web_client.chat_postMessage(
                    channel=channel_id,
                    text=output
                    )
            elif self.game != None and data.get('bot_id') == None:
                channel_id = data['channel']
                thread_ts = data['ts']
                user = data['user']
                text = data.get('text', [])
                print (text)
                try:
                    turn_from = text.split('-')[0]
                    turn_to = text.split('-')[1]
                    move = coordinate_conversion.Convert().coordinates(turn_from, turn_to)
                    if self.game.execute_turn(move[0],move[1],move[2],move[3]) == 'invalid move':
                        web_client.chat_postMessage(
                            channel=channel_id,
                            text='Invalid move - try again'
                            )
                except:
                    web_client.chat_postMessage(
                        channel=channel_id,
                        text='Invalid move - try again'
                        )
                output = self.__output_board()
                web_client.chat_postMessage(
                    channel=channel_id,
                    text=output
                    #thread_ts=thread_ts
                    )
                #checkmate condition
                #stop the game
                #checking if the player is allowed to give the instruction
                #can run only one game concurrently

        slack_token = os.environ["SLACK_API_TOKEN"]
        rtm_client = slack.RTMClient(token=slack_token)
        rtm_client.start()

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

    def announce_whose_turn(self):
        if self.game.p1_turn == True:
            print(self.game.player_1.name + "'s turn!")
        else:
            print(self.game.player_2.name + "'s turn!")

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

    def __output_board(self):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        self.announce_whose_turn()
        self.show_board(self.game.board, self.game.player_1.name, self.game.player_2.name)
        result_string = result.getvalue()
        sys.stdout = old_stdout
        return result_string

test = SlackOutput()
test.start_listen()
