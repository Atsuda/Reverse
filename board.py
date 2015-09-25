# -*- coding: utf-8 -*-
class Board():
	def __init__(self):
		self.playboard = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]
			, [2, 0, 0, 0, 0, 0,1, 0, 0, 2]
			, [2, 0, 0, 0, -1, 1, 0, 0, 0, 2]
			, [2, 0, 0, 0, 1, -1, 0, 0, 0, 2]
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]
			, [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]
			, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

	# TODO boardの表示。文字コードがよく分からない。1,-1を○とか●にしたい。
	def print_board(self):
		for num in range(0,10):
			for num2 in range(0,10):
				print self.playboard[num][num2]

def count_stone1(playboard,playernum):
	#playboard内の1を数える。minimax法使用のため、playernumが-1なら、-1をかける。
	stone1_count = 0
	for a in playboard:
		b = a.count(1)
		stone1_count=stone1_count+b
	if playernum ==1:
		pass
	else:
		stone1_count = stone1_count*(-1)
	return stone1_count
