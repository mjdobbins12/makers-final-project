from piece import Piece

class Heuristics:

        def __init__(self,game):
                self.game = game

        PAWNS_GRID = ([
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 5, 10, 10,-20,-20, 10, 10,  5],
                [ 5, -5,-10,  0,  0,-10, -5,  5],
                [ 0,  0,  0, 20, 20,  0,  0,  0],
                [ 5,  5, 10, 25, 25, 10,  5,  5],
                [10, 10, 20, 30, 30, 20, 10, 10],
                [50, 50, 50, 50, 50, 50, 50, 50],
                [ 0,  0,  0,  0,  0,  0,  0,  0]
                ])

        KNIGHTS_GRID = ([
                [-50, -40, -30, -30, -30, -30, -40, -50],
                [-40, -20,   0,   5,   5,   0, -20, -40],
                [-30,   5,  10,  15,  15,  10,   5, -30],
                [-30,   0,  15,  20,  20,  15,   0, -30],
                [-30,   5,  15,  20,  20,  15,   0, -30],
                [-30,   0,  10,  15,  15,  10,   0, -30],
                [-40, -20,   0,   0,   0,   0, -20, -40],
                [-50, -40, -30, -30, -30, -30, -40, -50]
                ])

        BISHOPS_GRID = ([
                [-20, -10, -10, -10, -10, -10, -10, -20],
                [-10,   5,   0,   0,   0,   0,   5, -10],
                [-10,  10,  10,  10,  10,  10,  10, -10],
                [-10,   0,  10,  10,  10,  10,   0, -10],
                [-10,   5,   5,  10,  10,   5,   5, -10],
                [-10,   0,   5,  10,  10,   5,   0, -10],
                [-10,   0,   0,   0,   0,   0,   0, -10],
                [-20, -10, -10, -10, -10, -10, -10, -20]
                ])

        ROOKS_GRID = ([
                [ 0,  0,  0,  5,  5,  0,  0,  0],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [ 5, 10, 10, 10, 10, 10, 10,  5],
                [ 0,  0,  0,  0,  0,  0,  0,  0]
                ])

        QUEENS_GRID = ([
                [-20, -10, -10, -5, -5, -10, -10, -20],
                [-10,   0,   5,  0,  0,   0,   0, -10],
                [-10,   5,   5,  5,  5,   5,   0, -10],
                [  0,   0,   5,  5,  5,   5,   0,  -5],
                [ -5,   0,   5,  5,  5,   5,   0,  -5],
                [-10,   0,   5,  5,  5,   5,   0, -10],
                [-10,   0,   0,  0,  0,   0,   0, -10],
                [-20, -10, -10, -5, -5, -10, -10, -20]
                ])

        def evaluate(self, board):
                material = Heuristics.get_material_score(self.game.board)

                pawns = Heuristics.get_piece_position_score(self.game.board, "Pawn", Heuristics.PAWNS_GRID)
                knights = Heuristics.get_piece_position_score(self.game.board, "Knight", Heuristics.KNIGHTS_GRID)
                bishops = Heuristics.get_piece_position_score(self.game.board, "Bishop", Heuristics.BISHOPS_GRID)
                rooks = Heuristics.get_piece_position_score(self.game.board, "Rook", Heuristics.ROOKS_GRID)
                queens = Heuristics.get_piece_position_score(self.game.board, "Queen", Heuristics.QUEENS_GRID)

                return material + pawns + knights + bishops + rooks + queens

        @staticmethod
        def get_piece_position_score(board, piece_type, table):
                white = 0
                black = 0
                for x in range(0,8):
                        for y in range(0,8):
                                if isinstance(board[x][y], Piece):
                                        piece = board[x][y]
                                        if (piece.name == piece_type):
                                                if (piece.colour == "White"):
                                                        white += table[x][y]
                                                else:
                                                        black += table[7 - x][y]
                return white - black

        @staticmethod
        def get_material_score(board):
                white = 0
                black = 0
                for x in range(0,8):
                        for y in range(0,8):
                                if isinstance(board[x][y], Piece):
                                        piece = board[x][y]
                                        if (piece.colour == "White"):
                                                white += piece.value
                                        else:
                                                black += piece.value
                return white - black


                