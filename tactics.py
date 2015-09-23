# -*- coding: utf-8 -*-
import setstone

class Tactics():
	#cpuプレイヤーの戦略
	self.cpu_board=setstone.Setstone.get_board(self,board)

	def can_set_stone(self,playernum,cpu_board):
	#石の置ける座標の取得
		for row in range(1,9):
			for column in range(1,9):
