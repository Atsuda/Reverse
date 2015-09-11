# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board

game1 = board.Board()
playernum = 1
row =4
column =3
game1.set_stone(playernum,row,column)
for a in range (10):
	print game1.board[a]