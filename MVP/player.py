class Player:
        def __init__(self, name, colour):
                self.name = name
                self.colour = colour
                self.taken_pieces = []
                self.current_score = 0

        def store_piece(self, piece):
                self.taken_pieces.append(piece)
                self.score += piece.score
