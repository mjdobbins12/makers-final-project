class Player:
        def __init__(self, name, colour):
                self.name = name
                self.colour = colour
                self.taken_pieces = []

        def store_piece(self, piece):
                self.taken_pieces.append(piece)
