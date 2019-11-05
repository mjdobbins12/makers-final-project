from piece import Piece

class SlackBoardDisplay:

    def output_board(self, game):
        output = self.__announce_whose_turn(game)
        output +='\n\n\n'
        output += f"<@{game.player_2.name}>\n"
        output += "| A | B | C | D | E | F | G | H |\n"
        output += '________________________\n'
        ind = 8
        for row in game.board:
            x = "|"
            for el in row:
                if isinstance(el, Piece):
                    x += f" {el.symbol} |"
                else:
                    x += f" {el}  |"
            x += f" {ind}"
            ind -= 1
            output += f"{x}\n"
            output += '------------------------------\n'
        output += f"<@{game.player_1.name}>\n"
        output += '\n'
        output += self.__list_taken_pieces_ifany(game)
        return output

    def __announce_whose_turn(self, game):
        if game.p1_turn == True:
            return f"<@{game.player_1.name}>" + "'s turn!"
        else:
            return f"<@{game.player_2.name}>" + "'s turn!"

    def __list_taken_pieces_ifany(self, game):
        output = '\n'
        if len(game.player_2.taken_pieces) > 0:
            output += 'Taken:'
            for el in game.player_2.taken_pieces:
                output += f" {el.symbol}"
            output += '\n'
        if len(game.player_1.taken_pieces) > 0:
            output += 'Taken:'
            for el in game.player_1.taken_pieces:
                output += f" {el.symbol}"
            output += '\n'
        return output
