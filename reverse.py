# -*- coding: utf-8 -*-
import board

playernum = 1
game1=board.Board()
row = 3
column =4
game1.null_stone(row, column)
game1.get_vector(row,column)
game1.print_board()
print(game1.right_vec)
game1.next_stone(playernum)
print(game1.next_stone_vector_option)
for num in game1.next_stone_vector_option:
	print game1.vector_list[num]
game1.can_reverse_stone(playernum)
print game1.can_reverse_stone_optionAndCount
game1.reverse_stone(playernum,row,column)
game1.print_board()