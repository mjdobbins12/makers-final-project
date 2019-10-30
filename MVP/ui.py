import pawn

class UI:
    def __init__(self, game):
        self.game = game.Game(self.getnames()[0], self.getnames()[1])
        self.show_board(self.game.board, self.game.p1_name, self.game.p2_name)

    def get_names(self):
        names = []
        names.push(input("Enter player 1 name: "))
        names.push(input("Enter player 2 name: "))
        print(names[0] + ' vs. ' + names[1])
        return names
        # self.show_board(self.game.board, self.game.p1_name, self.game.p2_name)

    def show_board(self, board, p1_name, p2_name):
        print('')
        print(p2_name)
        print("| a | b | c | d | e | f | g | h |")
        print("_" * 33)
        ind = 8
        for row in self.game.board.board:
            x = "|"
            for el in row:
                if isinstance(el, pawn.Pawn):
                    x += f" {el.name} |"
                else:
                    x += f" {el} |"
            x += f" {ind}"
            ind -= 1
            print(x)
            print("-" * 33)
        print(p1_name)
        print('')
