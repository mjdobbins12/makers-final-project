import piece

class UIBoardDisplay:

    def show_board(self, game, board, p1_name, p2_name):
          print('')
          print(p2_name)
          print("| a | b | c | d | e | f | g | h |")
          print("_" * 33)
          ind = 8
          for row in board:
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
          self.__print_taken_pieces_ifany(game)

      # private methods

    def __print_taken_pieces_ifany(self, game):
        if len(game.player_2.taken_pieces) > 0:
            x = 'Taken:'
            for el in game.player_2.taken_pieces:
                x += f" {el.symbol}"
            print(x)
        if len(game.player_1.taken_pieces) > 0:
            x = 'Taken:'
            for el in game.player_1.taken_pieces:
                x += f" {el.symbol}"
            print(x)
