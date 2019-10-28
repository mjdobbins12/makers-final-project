class Board:
				grid = [
								['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','*','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B']
              ]

				def show_board(self):
								return self.grid

				def move(self, start_r, start_c, finish_r, finish_c):
								self.grid[start_r][start_c] = 'B'
								self.grid[finish_r][finish_c] = '*'
