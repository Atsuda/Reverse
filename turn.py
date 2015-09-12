# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import setstone
class Turn(setstone.Setstone):
	#このターンの処理
	def turn(self,playernum,board,row,column):
		setstone.Setstone.set_stone(self,playernum,board,row,column)