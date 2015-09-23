# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,setstone
game1=board.Board()
playernum = 1
row=3
column = 4

game1.playboard
turn1 = setstone.Setstone()
turn1.get_board(game1.playboard)
turn1.playboard.append(1)

print 'A'