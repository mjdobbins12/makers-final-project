[![Build Status](https://travis-ci.com/DanGyi23/makers-final-project.svg?branch=master)](https://travis-ci.com/DanGyi23/makers-final-project)


# Grandmasters Slack-Based Chess Game

**Running the game in command line**
- RUN ALL commands in Setup.md file in the root directory of this REPO
- open python interpreter - e.g. `python3` on Mac from the src directory
- `import ui`
- `ui = ui.UI()`
- `ui.start()`


**Running the game in Slack**
- If you want to run in slack, then ensure you have slackclient installed (`python3 -m pip install slackclient`) and the env variable passed when starting the python interpreter in src directory (e.g. `SLACK_API_TOKEN="token" python3 slack_ui.py`)

- Open up your workspace and invite Chessy! `/invite @Chessy`

### Our process

- We focused on a feature lead design with a strict focus on TDD using Pytest. We made sure that we built each module was easily abstractable, and could be replaced easily (e.g. Rulesets, pieces etc.)
- We worked in 2 day sprints, and paired on the more technically difficult parts of the script. Working on modular design with clear separate responsibilities for each team member meant that there were barely any merge conflicts throughout  

- By the end of the second day we had arrived at our MVP:  

<br>
<img src="https://github.com/dangyi23/makers-final-project/blob/master/docs/MVP.gif" width=40%>

<br>
<img src="https://github.com/dangyi23/makers-final-project/blob/master/docs/Chessy_with_AI.gif" width=40%>


- Once we had a working MVP, we moved on to creating a module for each piece type, and making sure they each inherited from a master Piece class   

- This is where the headaches started. Programming Check/Checkmate/Stalemate conditions proved tricky. We prevailed!  

- Next, we moved on to implementing in Slack. We set up the slack UI to accept commands and print the state of the board in a slack channel

- Finally, we wanted to compete against an AI, and see how complex we could build a chess AI using a minimax algorithm. This required a few different versions and lots of reading/understanding Python iterative methods  

- We finally arrived, by the end of the second week, with a product that:
  - Has a Python backend that can run a command line UI but also interact with the Slack API to run in slack channels
  - Adheres to all of the rules of chess (legal/illegal moves, check/checkmate/stalemate etc.)
  - Multiple games can be played in parallel by any users that invite the Chessy Bot.
  - Has many different rulesets that can be injected into the game at various points (Bishops excommunicating, Rooks being sold off etc.)
  - Has an AI option, so that you can play vs DominationBot3000
  - This AI option can be modified to increase/decrease the depth (though increasing the depth has an exponential performance trade-off)
  - Renders a PNG image of the board after each legal turn is made, so that each player can see the state of the board before they make their turn.
  - Is great fun!

## Minimax Algorithm Iterations

**Kamikaze bot**

![](https://github.com/DanGyi23/makers-final-project/blob/master/docs/kamikaze_AI.gif)



**Bot only wants to move its Knights**

![](https://github.com/DanGyi23/makers-final-project/blob/master/docs/Knight_AI.gif)



**Bot works!**

![](https://github.com/DanGyi23/makers-final-project/blob/master/docs/Working_AI.gif)
