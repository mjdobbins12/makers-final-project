import os
import slack
from slack_control import SlackControl

class Slack:

    def __init__(self):
        self.slack_control = {}

    def post(self, client, text, channel):
        output = client.chat_postMessage(
            channel = channel,
            text = text,
            username = 'Chessy')
            # as_user = True)

    def start_listen(self):
        @slack.RTMClient.run_on(event='channel_joined')
        def join_channel(**payload):
            data = payload['data']
            self.post(payload['web_client'], self.__intro_chessy(), data['channel']['id'])
            self.slack_control[data['channel']['id']] = SlackControl(data['channel']['id'])
        @slack.RTMClient.run_on(event='group_joined')
        def join_private_channel(**payload):
            print('data')
            data = payload['data']
            self.post(payload['web_client'], self.__intro_chessy(), data['channel']['id'])
            self.slack_control[data['channel']['id']] = SlackControl(data['channel']['id'])
        @slack.RTMClient.run_on(event='message')
        def run_game(**payload):
            data = payload['data']
            web_client = payload['web_client']
            rtm_client = payload['rtm_client']
            print(data)
            print (data['channel'])
            try:
                self.slack_control[data['channel']].check_for_start(web_client, data)
                self.slack_control[data['channel']].check_for_moves(web_client, data)
                self.slack_control[data['channel']].check_for_stop(web_client, data)
                self.slack_control[data['channel']].check_for_mode(web_client, data)
                self.slack_control[data['channel']].check_for_mode_set(web_client, data)
                self.slack_control[data['channel']].check_for_join(web_client, data)
                self.slack_control[data['channel']].check_for_AI(web_client, data)
            except:
                print('Exception!')
                print(data)
        slack_token = os.environ["SLACK_API_TOKEN"]
        rtm_client = slack.RTMClient(token=slack_token)
        rtm_client.start()

    # private methods

    def __intro_chessy(self):
        output = 'Hi I am Chessy!\n'
        output += 'Let others play their games, the game of kings is still the ♔ of games!\n'
        output += 'Enter start to start the game!\n'
        return output

slack_instance = Slack()
slack_instance.start_listen()
