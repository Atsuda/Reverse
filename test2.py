# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,turn
game1=board.Board()

turn1 = turn.Turn()
playernum = 1
column = 3
row = 4
turn1.turn(playernum,game1.board,row,column)
for a in range (10):
	print game1.board[a]
print 'a'

turn2=turn.Turn()
playernum =-1
column = 5
row = 3
turn2.turn(playernum,game1.board,row,column)

for a in range (10):
	print game1.board[a]
print 'a'