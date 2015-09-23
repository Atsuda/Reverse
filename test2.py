# -*- coding: utf-8 -*-
__author__ = 'a_tsuda'
import board,setstone
game1=board.Board()

playernum = 1
yosoku_list = {}
yosoku_list_id = 0

for row in range(1,9):
	for column in range(1,9):
		yosoku = setstone.Setstone()
		if yosoku.can_set_stone(game1.playboard,playernum,row,column):
			yosoku.set_stone(game1.playboard,playernum,row,column)
			yosoku_list[yosoku_list_id]={"parent_id":-1,"playernum":playernum,"playboard":yosoku.playboard,"row":row,"column":column}
			yosoku_list_id=yosoku_list_id+1

print 'yosoku_list = '
print yosoku_list
meta_yosokulist = {1:yosoku_list}
temp_yosokulist = {}

y=yosoku_list[0]
print 'y = '
print y["playboard"]
print y["playboard"][1][1] == 0

for num in yosoku_list.keys():
	for row in range(1,9):
		for column in range(1,9):
			yosoku = setstone.Setstone()
			y=yosoku_list[num]
			if yosoku.can_set_stone(y["playboard"],y["playernum"]*(-1),row,column):
				temp_yosokulist[yosoku_list_id]=1000
				yosoku_list_id=yosoku_list_id+1

meta_yosokulist[2] = temp_yosokulist
print meta_yosokulist

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
