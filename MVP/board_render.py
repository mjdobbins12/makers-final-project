from PIL import Image
from more_itertools import run_length
import chess
import chess.svg
import copy
import piece
import king
import queen
import pawn
import knight
import bishop

class BoardRender:

        def __init__(self,game):
                self.game = copy.deepcopy(game)
        
        def generate_fen(self):
                board = (self.game.board)
                for i in range(0,8):
                        for j in range(0,8):
                                if board[i][j] == "-":
                                        board[i][j] = "em"
                                elif isinstance(board[i][j], piece.Piece):
                                        if board[i][j].colour == "White":
                                                if board[i][j].name == "King":
                                                        board[i][j] = "wk"
                                                elif board[i][j].name == "Queen":
                                                        board[i][j] = "wq"
                                                elif board[i][j].name == "Rook":
                                                        board[i][j] = "wr"
                                                elif board[i][j].name == "Bishop":
                                                        board[i][j] = "wb"
                                                elif board[i][j].name == "Knight":
                                                        board[i][j] = "wn"
                                                elif board[i][j].name == "Pawn":
                                                        board[i][j] = "wp"
                                        elif board[i][j].colour == "Black":
                                                if board[i][j].name == "King":
                                                        board[i][j] = "bk"
                                                elif board[i][j].name == "Queen":
                                                        board[i][j] = "bq"
                                                elif board[i][j].name == "Rook":
                                                        board[i][j] = "br"
                                                elif board[i][j].name == "Bishop":
                                                        board[i][j] = "bb"
                                                elif board[i][j].name == "Knight":
                                                        board[i][j] = "bn"
                                                elif board[i][j].name == "Pawn":
                                                        board[i][j] = "bp"
                
                print(self.main(board))

                return self.main(board)

        def draw_board(self):
                board = chess.Board(self.generate_fen())
                img = chess.svg.board(board=board)
                file = open("index.html", "w")
                file.write(img)
                # print(file)




        def convert_cell(self, value):
                if value == 'em':
                        return None
                else:
                        color, piece = value
                        return piece.upper() if color == 'w' else piece.lower()


        def convert_rank(self, rank):
                return ''.join(
                        value * count if value else str(count)
                        for value, count in run_length.encode(map(self.convert_cell, rank))
                )


        def fen_from_board(self, board):
                return '/'.join(map(self.convert_rank, board)) + ' w KQkq - 0 1'


        def main(self, board):
                # board = [
                #         ['bk', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
                #         ['em', 'bn', 'em', 'wr', 'em', 'wp', 'em', 'em'],
                #         ['br', 'em', 'bp', 'em', 'em', 'bn', 'wn', 'em'],
                #         ['em', 'em', 'bp', 'bp', 'bp', 'em', 'wp', 'bp'],
                #         ['bp', 'bp', 'em', 'bp', 'wn', 'em', 'wp', 'em'],
                #         ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
                #         ['em', 'em', 'em', 'wk', 'em', 'em', 'em', 'em'],
                #         ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
                # ]
                return self.fen_from_board(board)