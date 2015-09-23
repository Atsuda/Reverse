# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,setstone
game1=board.Board()
playernum = 1
row=3
column = 4

game1.playboard
turn1 = setstone.Setstone()
turn1.set_stone(playernum,game1.playboard,row,column)
game1.playboard

print "finsh"