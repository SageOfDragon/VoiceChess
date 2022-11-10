from consts import WIDTH, HEIGHT, COLOR_01, COLOR_02

class Piece ():
	def __init__ (self, x, y, color, name):
		self.x = x
		self.y = y
		self.color = color
		self.name = name


class Rook (Piece):
	def __init__ (self, x, y, color):
		super().__init__ (x, y, color, "R")

	def get_valid_moves (self, x, y):
		moves = []
		for w in range (WIDTH):
			if w != x:
				moves.append ((w, y))
		for h in range (HEIGHT):
			if h != y:
				moves.append ((x, h))
		return moves


class Knight (Piece):
	def __init__ (self, x, y, color):
		super().__init__ (x, y, color, "N")

	def get_valid_moves (self, x, y):
		moves = []
		for w in range (WIDTH):
			for h in range (HEIGHT):
				if abs (x - w) == 1 and abs (y - j) == 2:
					moves.append ((w, h))
				if abs (x - w) == 2 and abs (y - j) == 1:
					moves.append ((w, h))
		return moves


class Bishop (Piece):
	def __init__ (self, x, y, color):
		super().__init__ (x, y, color, "B")

	def get_valid_moves (self, x, y):
		moves = []
		for w in range (WIDTH):
			for h in range (HEIGHT):
				if abs (x - w) == abs (y - h):
					if w != x or h != y:
						moves.append ((w, h))
		return moves


class Queen (Piece):
	def __init__ (self, x, y, color):
		super ().__init__ (x, y, color, "Q")

	def get_valid_moves (self, x, y):
		moves = []
		for w in range (WIDTH):
			for h in range (HEIGHT):
				if abs (x - w) == abs (y - h):
					if w != x and h != y:
						moves.append ((w, h))
				if w == x  and h != y:
					moves.append ((w, y))
				if h != y:
					moves.append ((x, h))
		return moves


class King (Piece):
	def __init__ (self, x, y, color):
		super().__init__ (x, y, color, "K")

	def get_valid_moves (self, x, y):
		moves = []
		for w in range (WIDTH):
			for h in range (HEIGHT):
				if abs (x - w) <= 1 and abs (y - h) <= 1:
					if w != x or h != y:
						moves.append ((w, h))
		return moves
	


class Pawn (Piece):
	def __init__ (self, x, y, color):
		super().__init__ (x, y, color, "P")

	def get_valid_moves (self, x, y):
		moves = []
		if self.color == COLOR_01:
			if y < HEIGHT - 1:
				moves.append ((x, y + 1))
			if y == 1:
				moves.append ((x, y + 2))
		else:
			if y > 0:
				moves.append ((x, y - 1))
			if y == HEIGHT - 2:
				moves.append ((x, y - 2))
		return moves
	
	def get_valid_attacks (self, x, y):
		moves = []
		if self.color == COLOR_01:
			if y < HEIGHT - 1:
				if x > 0:
					moves.append ((x - 1, y + 1))
				if x < WIDTH - 1:
					moves.append ((x + 1, y + 1))
		else:
			if y > 0:
				if x > 0:
					moves.append ((x - 1, y - 1))
				if x < WIDTH - 1:
					moves.append ((x + 1, y - 1))
		return moves

	def get_en_passant (self, x, y):
		moves = []
		if self.color == COLOR_01:
			if y == 3:
				if x > 0:
					moves.append ((x - 1, y + 1))
				if x < WIDTH - 1:
					moves.append ((x + 1, y + 1))
		else:
			if y == HEIGHT - 4:
				if x > 0:
					moves.append ((x - 1, y - 1))
				if x < WIDTH - 1:
					moves.append ((x + 1, y - 1))
		return moves


