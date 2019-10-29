class Board:
	grid = [
		["R","N","B","Q","K","B","N","R"],
        ['p','p','p','p','p','p','p','p'],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ['p','p','p','p','p','p','p','p'],
        ["R","N","B","Q","K","B","N","R"]
        ]

	def show_board(self):
		print("_" * 33)
		for row in self.grid:
			x = " | "
			print(f"\n| {x.join(row)} |")
			print("-" * 33)

	def move(self, start_r, start_c, finish_r, finish_c):
		if self.is_destination_free(finish_r, finish_c):
			self.grid[start_r][start_c] = ' '
			self.grid[finish_r][finish_c] = 'R'
		else:
			raise Exception("Invalid move")

	def is_destination_free(self, finish_r, finish_c):
		return self.grid[finish_r][finish_c] == ' '

class Pawn:
	options = []

	def __init__(self, color):
		self.color = color

	def move(self, start_r, start_c, finish_r, finish_c):
		range(start_r, start_c)

	def range(start_r, start_c):
		self.options.extend([(start_r + 1, start_c + 1)])
