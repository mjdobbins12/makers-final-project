**Running the game (WIP)**
- open python interpreter - e.g. python3 on Mac from the MVP directory
- import ui
- ui = ui.UI()
- ui.start()
- if you want to use slack, then ensure you have slackclient installed (pip install slackclient) and the env variable passed when starting the python intepreter (e.g. SLACK_API_TOKEN="token" python3 slack_ui.py)

### Our process

By the end of the second day we had arrived at our MVP:

<br>
<img src="https://github.com/dangyi23/makers-final-project/blob/master/docs/MVP.gif" width=40%>

MVP user stories:
```
As a user,
So that I can play a game,
I want to be able to see a chess board.

As a user,
So that I can advance towards the enemy
I want to make a move with a pawn and see the board update.

As a user,
So that I can play within the rules,
I want to be notified if I try and make an illegal move with a pawn.

As a user,
So that I can crush my opponent,
I want to take another pawn, and see it removed from the chess board.
```
