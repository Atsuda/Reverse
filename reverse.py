__author__ = 'a_tsuda'
import board

playernum = 1
game1=board.Board()
game1.get_vector(4,3)
game1.print_board()
print(game1.right_vec)
game1.next_stone(playernum)
print(game1.next_stone_vector_option)
for num in game1.next_stone_vector_option:
	print game1.vector_list[num]
game1.can_reverse_stone(playernum)

