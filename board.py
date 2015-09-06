# -*- coding: utf-8 -*-
import setstone

class Board(setstone.Setstone):
	def __init__(self):
		self.board = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2] \
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2] \
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2] \
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2] \
			, [2, 0, 0, 0, -1, 1, 0, 0, 0, 2] \
			, [2, 0, 0, 0, 1, -1, 0, 0, 0, 2] \
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2] \
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2] \
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2] \
			, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

	# TODO boardの表示
	def print_board(self):
		for num in range(0,10):
			print self.board[num]