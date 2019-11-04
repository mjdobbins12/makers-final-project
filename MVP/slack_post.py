import os
import slack
import piece
import coordinate_conversion
import game

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
        # might not be needed
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
                    text=f" <@{user}> launched the game!"#,
                    #thread_ts=thread_ts
                    )
                web_client.chat_postMessage(
                    channel=channel_id,
                    text=f" <@{members[0]}> vs <@{members[1]}>"#,
                    #thread_ts=thread_ts
                    )
                self.game = game.Game(f"<@{members[0]}>",f"<@{members[1]}>")


        slack_token = os.environ["SLACK_API_TOKEN"]
        rtm_client = slack.RTMClient(token=slack_token)
        rtm_client.start()

test = SlackOutput()
test.start_listen()
