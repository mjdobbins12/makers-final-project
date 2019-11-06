from piece import Piece

class Heuristics:

        def __init__(self,game):
                self.game = game

        WHITE_KINGS_GRID = ([
                [ 0,  0,  -80,  0,  0,  0,  -80,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,  -80,  0,  0,  0,  -80,  0]
                ])
        WHITE_KNIGHTS_GRID = ([
                [-50, -40, -30, -30, -30, -30, -40, -50],
                [-40, -20,   0,   5,   5,   0, -20, -40],
                [-30,   5,  10,  15,  15,  10,   5, -30],
                [-30,   0,  15,  20,  20,  15,   0, -30],
                [-30,   5,  15,  20,  20,  15,   0, -30],
                [-30,   0,  10,  15,  15,  10,   0, -30],
                [-40, -20,   0,   0,   0,   0, -20, -40],
                [-50, -40, -30, -30, -30, -30, -40, -50]
                ])

        WHITE_QUEENS_GRID = ([
                [-20, -10, -10, -5, -5, -10, -10, -20],
                [-10,   0,   5,  0,  0,   0,   0, -10],
                [-10,   5,   5,  5,  5,   5,   0, -10],
                [  0,   0,   5,  5,  5,   5,   0,  -5],
                [ -5,   0,   5,  5,  5,   5,   0,  -5],
                [-10,   0,   5,  5,  5,   5,   0, -10],
                [-10,   0,   0,  0,  0,   0,   0, -10],
                [-20, -10, -10, -5, -5, -10, -10, -20]
                ])

        WHITE_PAWNS_GRID = ([
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [50, 50, 50, 50, 50, 50, 50, 50],
                [10, 10, 20, 30, 30, 20, 10, 10],
                [ 5,  5, 10, 25, 25, 10,  5,  5],
                [ 0,  0,  0, 20, 20,  0,  0,  0],
                [ 5, -5,-10,  0,  0,-10, -5,  5],
                [ 5, 10, 10,-20,-20, 10, 10,  5],
                [ 0,  0,  0,  0,  0,  0,  0,  0]
                ])

        WHITE_BISHOPS_GRID = ([
                [-20, -10, -10, -10, -10, -10, -10, -20],
                [-10,   0,   0,   0,   0,   0,   0, -10],
                [-10,   0,   5,  10,  10,   5,   0, -10],
                [-10,   5,   5,  10,  10,   5,   5, -10],
                [-10,   0,  10,  10,  10,  10,   0, -10],
                [-10,   10,  10,  10,  10,  10,  10, -10],
                [-10,   5,   0,   0,   0,   0,   5, -10],
                [-20, -10, -10, -10, -10, -10, -10, -20]
                ])

        WHITE_ROOKS_GRID = ([
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ 5, 10, 10, 10, 10, 10, 10,  5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [ 0,  0,  0,  5,  5,  0,  0,  0]
                ])

        BLACK_KINGS_GRID = ([
                [ 0,  0,  80,  0,  0,  0,  80,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,    0,  0,  0,  0,    0,  0],
                [ 0,  0,  80,  0,  0,  0,  80,  0]
                ])
        
        BLACK_PAWNS_GRID = ([
                [ 0,  0,  0,  0,  0,  0,  0,  0],
                [ -5, -10, -10,20,20, -10, -10,  -5],
                [ -5, 5,10,  0,  0,10, 5,  -5],
                [ 0,  0,  0, -20, -20,  0,  0,  0],
                [ -5,  -5, -10, -25, -25, -10,  -5,  -5],
                [-10, -10, -20, -30, -30, -20, -10, -10],
                [-50, -50, -50, -50, -50, -50, -50, -50],
                [ 0,  0,  0,  0,  0,  0,  0,  0]
                ])

        BLACK_BISHOPS_GRID = ([
                [20, 10, 10, 10, 10, 10, 10, 20],
                [10,   -5,   0,   0,   0,   0,   -5, 10],
                [10,  -10,  -10,  -10,  -10,  -10,  -10, 10],
                [10,   0,  -10,  -10,  -10,  -10,   0, 10],
                [10,   -5,   -5,  -10,  -10,   -5,   -5, 10],
                [10,   0,   -5,  -10,  -10,   -5,   0, 10],
                [10,   0,   0,   0,   0,   0,   0, 10],
                [20, 10, 10, 10, 10, 10, 10, 20]
                ])

        BLACK_ROOKS_GRID = ([
                [ 0,  0,  0,  -5,  -5,  0,  0,  0],
                [5,  0,  0,  0,  0,  0,  0, 5],
                [5,  0,  0,  0,  0,  0,  0, 5],
                [5,  0,  0,  0,  0,  0,  0, 5],
                [5,  0,  0,  0,  0,  0,  0, 5],
                [5,  0,  0,  0,  0,  0,  0, 5],
                [ -5, -10, -10, -10, -10, -10, -10,  -5],
                [ 0,  0,  0,  0,  0,  0,  0,  0]
                ])

        BLACK_KNIGHTS_GRID = ([
                [50, 40, 30, 30, 30, 30, 40, 50],
                [40, 20,   0,   -5,   -5,   0, 20, 40],
                [30,   -5,  -10,  -15,  -15,  -10,   5, 30],
                [30,   0,  -15,  -20,  -20,  -15,   0, 30],
                [30,   -5,  -15,  -20,  -20,  -15,   0, 30],
                [30,   0,  -10,  -15,  -15,  -10,   0, 30],
                [40, 20,   0,   0,   0,   0, 20, 40],
                [50, 40, 30, 30, 30, 30, 40, 50]
                ])

        BLACK_QUEENS_GRID = ([
                [20, 10, 10, 5, 5, 10, 10, 20],
                [10,   0,   -5,  0,  0,   0,   0, 10],
                [10,   -5,   -5,  -5,  -5,   -5,   0, 10],
                [ 0,   0,   -5,  -5,  -5,   -5,   0,  5],
                [ 5,   0,   -5,  -5,  -5,   -5,   0,  5],
                [10,   0,   -5,  -5,  -5,   -5,   0, 10],
                [10,   0,   0,  0,  0,   0,   0, 10],
                [20, 10, 10, 5, 5, 10, 10, 20]
                ])

       

        

        def evaluate(self, board):
                material = Heuristics.get_material_score(self.game.board)
                if self.game.p1_turn:
                        pawns = Heuristics.get_piece_position_score(self.game.board, "Pawn", Heuristics.WHITE_PAWNS_GRID)
                        knights = Heuristics.get_piece_position_score(self.game.board, "Knight", Heuristics.WHITE_KNIGHTS_GRID)
                        bishops = Heuristics.get_piece_position_score(self.game.board, "Bishop", Heuristics.WHITE_BISHOPS_GRID)
                        rooks = Heuristics.get_piece_position_score(self.game.board, "Rook", Heuristics.WHITE_ROOKS_GRID)
                        queens = Heuristics.get_piece_position_score(self.game.board, "Queen", Heuristics.WHITE_QUEENS_GRID)
                        kings = Heuristics.get_piece_position_score(self.game.board, "King", Heuristics.WHITE_KINGS_GRID)
                else:
                        pawns = Heuristics.get_piece_position_score(self.game.board, "Pawn", Heuristics.BLACK_PAWNS_GRID)
                        knights = Heuristics.get_piece_position_score(self.game.board, "Knight", Heuristics.BLACK_KNIGHTS_GRID)
                        bishops = Heuristics.get_piece_position_score(self.game.board, "Bishop", Heuristics.BLACK_BISHOPS_GRID)
                        rooks = Heuristics.get_piece_position_score(self.game.board, "Rook", Heuristics.BLACK_ROOKS_GRID)
                        queens = Heuristics.get_piece_position_score(self.game.board, "Queen", Heuristics.BLACK_QUEENS_GRID)
                        kings = Heuristics.get_piece_position_score(self.game.board, "King", Heuristics.BLACK_KINGS_GRID)

                return material + pawns + knights + bishops + rooks + queens + kings

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
                                                        black += table[x][y]
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
                return white + black


                