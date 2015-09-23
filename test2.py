# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,setstone
game1=board.Board()

turn1 = setstone.Setstone()
playernum = 1
yosoku_list = {}
yosoku_list_id = 0
for row in range(1,9):
	for column in range(1,9):
		yosoku = setstone.Setstone()
		if yosoku.can_set_stone(playernum,game1.playboard,row,column):
			yosoku_list[yosoku_list_id]=[playernum,row,column]
			yosoku_list_id=yosoku_list_id+1
"""
playernum = 1
row=3
column = 4

turn1.can_set_stone(playernum,game1.playboard,row,column)
"""
print yosoku_list
for a in range (10):
	print game1.playboard[a]
print 'a'
