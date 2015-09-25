# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,setstone,tactics
from copy import deepcopy
game1=board.Board()

print "   0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
for n in range(10):
	print n,game1.playboard[n]
playernum = 1
row = int(raw_input("input row"))
column = int(raw_input("input column"))
turn = setstone.Setstone()
turn.set_stone(game1.playboard,playernum,row,column)
game1.playboard = deepcopy(turn.playboard)
print "   0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
for n in range(10):
	print n,game1.playboard[n]

playernum = -1
tactics.run_minimax_set_stone(playernum,game1.playboard)
game1.playboard = deepcopy(predict_result_playboard)
print "   0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
for n in range(10):
	print n,game1.playboard[n]