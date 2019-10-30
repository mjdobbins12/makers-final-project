import pawn

class UI:

    def show_board(self, board, p1_name, p2_name):
        print('')
        print(p2_name)
        print("| a | b | c | d | e | f | g | h |")
        print("_" * 33)
        ind = 8
        for row in board.board:
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
