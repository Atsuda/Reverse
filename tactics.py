# -*- coding: utf-8 -*-
import setstone

class Tactics():
	#cpuプレイヤーの戦略
	self.cpu_board=setstone.Setstone.get_board(self,board)

	def predict(self,playernum,cpu_board):
	#1手予測する
		for row in range(1,9):
			for column in range(1,9):
