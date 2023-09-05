class Board():
	
	def __init__(self):
		self.grid = []
		for number in range(3):
			row = []
			for col in range(3):
				row.append('')
			self.grid.append(row)
	
	def get_winner(self):
		"""Returns winner of game. Returns '' if no one has one."""
		
		#Checks if there are three of the same letter in a row
		for row in self.grid:
			if row[0] == row[1] and row[1] == row[2]:
				if row[0] != '':
					self.winning_row = [(row,0),(row,2)]
					return row[0]
		
		#Checks if there are three of the same letter in a column
		for col in range(3):
			if self.grid[0][col] == self.grid[1][col] and self.grid[1][col] == self.grid[2][col]:
					if self.grid[0][col] != '':
						self.winning_row = [(0,col), (2,col)]
						return self.grid[0][col]
		
		#Checks if there are three of the same letter in a diagonal
		if self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]:
			if self.grid[0][0] != '':
				self.winning_row = [(0,0),(2,2)]
				return self.grid[1][1]
		if self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]:
			if self.grid[0][2] != '':
				self.winning_row = [(0,2),(2,0)]
				return self.grid[0][2]
		
		#Checks if there is a draw
		for row in self.grid:
			for col in row:
				if col == '':
					return None
		return 'draw'
			
		


