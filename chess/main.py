from tkinter.tix import Tree
from termcolor import colored

from board import Board
from pieces import *
from consts import HEIGHT, WIDTH, COLOR_01, COLOR_02
from judge import Judge

def main():
	chess_game = ChessGame()
	chess_game.play()


class ChessGame:
	def __init__(self):
		self.board = Board()
		self.player1 = Player(COLOR_01, self.board)
		self.player2 = Player(COLOR_02, self.board)
		self.current_player = self.player1
		self.opposite_player = self.player2
		self.judge = Judge(self.board)

	def play(self):
		print("┌-------------------┐")
		print("│ Welcome to Chess! │")
		print("└-------------------┘")

		while True:
			self.board.print_board()
			self.current_player.move()

			if self.judge.is_check():
				if self.judge.is_check_mate():
					print("----- Check Mate! -----")
					print(f"Player {self.opposite_player.color} wins!")
					break
				else:
					print("------- Check! -------")

			if self.current_player == self.player1:
				self.current_player = self.player2
				self.opposite_player = self.player1
			else:
				self.current_player = self.player1
				self.opposite_player = self.player2
			

class Player:
	def __init__(self, color, board=None):
		self.color = color
		self.board = board

	def move(self):
		print("Player", self.color, "move")
		x1, y1, x2, y2 = map(int, input("x1, y1, x2, y2: ").split())

		self.board.board[y2][x2] = self.board.board[y1][x1]
		self.board.board[y1][x1] = None

		# if isValidMove(x1, y1, x2, y2):
		# 	self.board.board[y2][x2] = self.board.board[y1][x1]
		# 	self.board.board[y1][x1] = None
		# else:
		# 	print("Invalid move")

if __name__ == '__main__':
    main()
