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
			print(f"| {x.join(row)} |")
			print("-" * 33)

	def move(self, start_r, start_c, finish_r, finish_c):
		self.grid[start_r][start_c] = ' '
		self.grid[finish_r][finish_c] = 'p'
