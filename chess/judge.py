from consts import HEIGHT, WIDTH
from board import Board
from pieces import *


class Judge:
	def __init__(self, board: Board):
		board = board

	def is_check(self):
		king_x, king_y = self.board.get_king_position(self.opposite_player.color)
		for w in range(WIDTH):
			for h in range(HEIGHT):
				if self.is_valid_move(w, h, king_x, king_y):
					return True

	def is_check_mate(self):
		king = self.board.get_king(self.opposite_player.color) # type: King
		king_x, king_y = self.board.get_king_position(self.opposite_player.color)

		# Rule 1 - is the king in check?
		if self.is_check():
			return False

		# TODO: Rule 2 - is the king in checkmate?
		# Rule 2 - can any of the pieces capture the piece that is checking the king?
		if self.judge.is_attacker_can_be_captured(x2, y2):
			print("----- Check! -----")
			return False

		# TODO: Rule 3
		# Rule 3 - can any of the pieces block the check?


		# TODO: Rule 4 
		# Rule 4 - can the king move to a safe square?
		valid_moves = king.get_valid_moves(king_x, king_y)
		for w in range(WIDTH):
			for h in range(HEIGHT):
				valid_moves = [move for move in valid_moves if not self.judge.is_valid_move(w, h, move[0], move[1])]
		if len(valid_moves) == 0:
			return True


	def is_valid_move(self, x1, y1, x2, y2):
		piece = self.board.board[y1][x1]
		if piece is None:
			return False

		if (x2, y2) in piece.get_valid_moves(x1, y1):
			return True
		
		return False

	def is_attacker_can_be_captured(self, x, y):
		for w in range(WIDTH):
			for h in range(HEIGHT):
				if self.judge.is_valid_move(w, h, x, y):
					return True
		return False
