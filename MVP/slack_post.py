import os
import slack

class SlackOutput:

    def __init__(self):
        self.client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

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
