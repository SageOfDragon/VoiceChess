from pieces import *

class Board:
	def __init__(self):
		self.board = []
		for i in range(HEIGHT):
			self.board.append([])
			for j in range(WIDTH):
				self.board[i].append(None)

		self.add_piece(Rook(0, 0, COLOR_01))
		self.add_piece(Knight(1, 0, COLOR_01))
		self.add_piece(Bishop(2, 0, COLOR_01))
		self.add_piece(Queen(3, 0, COLOR_01))
		self.add_piece(King(4, 0, COLOR_01))
		self.add_piece(Bishop(5, 0, COLOR_01))
		self.add_piece(Knight(6, 0, COLOR_01))
		self.add_piece(Rook(7, 0, COLOR_01))
		for i in range(8):
			self.add_piece(Pawn(i, 1, COLOR_01))

		self.add_piece(Rook(0, 7, COLOR_02))
		self.add_piece(Knight(1, 7, COLOR_02))
		self.add_piece(Bishop(2, 7, COLOR_02))
		self.add_piece(Queen(3, 7, COLOR_02))
		self.add_piece(King(4, 7, COLOR_02))
		self.add_piece(Bishop(5, 7, COLOR_02))
		self.add_piece(Knight(6, 7, COLOR_02))
		self.add_piece(Rook(7, 7, COLOR_02))
		for i in range(8):
			self.add_piece(Pawn(i, 6, COLOR_02))

	def print_board(self):
		print("   -----------------")
		for i in range(HEIGHT):
			print(i, "|", end=" ")
			for j in range(WIDTH):
				if self.board[i][j] is None:
					print(" ", end=" ")
				else:
					p = self.board[i][j] # type: Piece
					print(colored(p.name, p.color), end=" ")
			print("|")
		print("   -----------------")
		print("    0 1 2 3 4 5 6 7")

	def add_piece(self, piece: Piece):
		self.board[piece.y][piece.x] = piece

	def get_king_position(self, color):
		for i in range(HEIGHT):
			for j in range(WIDTH):
				p = self.board[i][j]
				if p is not None and type(p).__name__ is "King" and p.color == color:
					return j, i
		return None
