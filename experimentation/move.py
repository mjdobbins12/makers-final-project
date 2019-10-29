class Board:
	white_pieces = ['pw']
	black_pieces = ['pb']

	grid = [
		['*','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B'],
		['B','B','B','B','B','B','B','B']
        ]

	def show_board(self):
		return self.grid

	def move(self, start_r, start_c, finish_r, finish_c):
		if self.is_destination_free(finish_r, finish_c):
			self.grid[start_r][start_c] = 'B'
			self.grid[finish_r][finish_c] = '*'
		else:
			raise Exception("Invalid move")

	def is_destination_free(self, finish_r, finish_c):
		return self.grid[finish_r][finish_c] == 'B'

class Pawn:
	options = []

	def __init__(self, color):
		self.color = color

	def move(self, start_r, start_c, finish_r, finish_c):
		range(start_r, start_c)

	def range:
		options.extend([(start_r + 1), (start_c + 1)])

# board = Board()
# p8 = Pawn('white')
# board.grid[0][7] = p8
#
# print(board.show_board())
