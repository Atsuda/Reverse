# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board

game1 = board.Board()
playernum = -1
selectedRow =5
selectedColumn =3
row = selectedRow
column = selectedColumn
game1.get_vector(row,column)
game1.next_stone(playernum)
game1.set_stone(playernum,row,column)
for a in range (10):
	print game1.board[a]
'''
playernum = 1
selectedRow =6
selectedColumn =6
row = selectedRow
column = selectedColumn
game1.get_vector(row,column)
game1.next_stone(playernum)
game1.set_stone(playernum,row,column)
for a in range (10):
	print game1.board[a]'''

game2 = board.Board()
pass