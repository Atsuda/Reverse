# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,setstone,tactics
from copy import deepcopy
game1=board.Board()

for nim in range(5):
	print 'turn %d'%(nim)
	print "   0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
	for n in range(10):
		print n,game1.playboard[n]
	playernum = 1
	print "playernum:%d"%(playernum)
	turn = setstone.Setstone()
	if turn.can_set_stone_all_point(game1.playboard,playernum):
		turn.set_stone_for_manual(game1.playboard,playernum)
		game1.playboard = deepcopy(turn.playboard)
	print "   0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
	for n in range(10):
		print n,game1.playboard[n]

	playernum = -1
	cpu_turn = setstone.Setstone()
	if turn.can_set_stone_all_point(game1.playboard,playernum):
		game1.playboard = deepcopy(tactics.run_minimax_set_stone(playernum,game1.playboard))
