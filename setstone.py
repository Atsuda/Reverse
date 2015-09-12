# -*- coding: utf-8 -*-
class Setstone():
	#石を置くために必要な処理をまとめたクラス

	#クラス変数の定義
	#単位ベクトルをオプションとして、繰り返し処理に使用する。
	right_vecop = [0, 1]
	rightUp_vecop = [-1, 1]
	Up_vecop = [-1, 0]
	leftUp_vecop = [-1, -1]
	left_vecop = [0, -1]
	leftDown_vecop = [1, -1]
	down_vecop = [1, 0]
	rightDown_vecop = [1, 1]
	vector_option = {1: right_vecop, 2: rightUp_vecop, 3: Up_vecop, 4: leftUp_vecop \
		, 5: left_vecop, 6: leftDown_vecop, 7: down_vecop, 8: rightDown_vecop}
	def __init__(self):
		#指定した座標を中心とした8方向のベクトル
		self.right_vec = []
		self.rightUp_vec = []
		self.Up_vec = []
		self.leftUp_vec = []
		self.left_vec = []
		self.leftDown_vec = []
		self.down_vec = []
		self.rightDown_vec = []
		self.vector_list = {1: self.right_vec, 2: self.rightUp_vec, 3: self.Up_vec, 4: self.leftUp_vec, 5: self.left_vec,
		               6: self.leftDown_vec, 7: self.down_vec, 8: self.rightDown_vec}
		# next_stoneメソッドで取得するリストの入れ物
		self.next_stone_vector_list = []
		# can_reverse_stoneメソッドで取得するリストの入れ物。vector_optionと何個目の石まで処理するかのリストをネスト
		self.can_reverse_stone_optionAndCount = []

	def get_board(self,board):
		#baord変数を受け取る
		self.board = board

	def null_stone(self, row, column):
		# 石が置いてあるか判定
		if self.board[row][column] == 0:
			pass
		else:
			print 'er1'

	def get_vector(self, row, column):
		# 指定した座標からボード端までのベクトルを取得(指定した座標は除く)
		for num in range(1, 9):
			temprow = row
			tempcol = column
			while self.board[temprow][tempcol] != 2:
				self.vector_list[num].append(self.board[temprow][tempcol])
				temprow = temprow + Setstone.vector_option[num][0]
				tempcol = tempcol + Setstone.vector_option[num][1]
			self.vector_list[num].append(2)

	def next_stone(self, playernum):
		# 隣の石が相手の石か判定し、隣の石が相手の石であるベクトルのvector_optionのキーのリストを作成
		for num in range(1, 9):
			if self.vector_list[num][1] == playernum * (-1):
				self.next_stone_vector_list.append(num)
			else:
				pass
		if self.next_stone_vector_list == []:
			print 'er2'

	def can_reverse_stone(self, playernum):
		# 連続する相手の石の次が自分の石であるかの判定
		for num in self.next_stone_vector_list:
			for vecnum in range(1, len(self.vector_list[num])):
				if self.vector_list[num][vecnum] == playernum * (-1):
					pass
				elif self.vector_list[num][vecnum] == playernum:
					self.can_reverse_stone_optionAndCount.append([num, vecnum])
					break
				else:
					break
		if self.can_reverse_stone_optionAndCount == []:
			print 'er3'

	def reverse_stone(self, playernum, row, column):
		# 石の反転処理
		for num in range(len(self.can_reverse_stone_optionAndCount)):
			vecop = (self.can_reverse_stone_optionAndCount[num][0])
			reverseCount = self.can_reverse_stone_optionAndCount[num][1]
			temprow = row
			tempcol = column
			for num2 in range(reverseCount):
				del self.board[temprow][tempcol]
				self.board[temprow].insert(tempcol, playernum)
				temprow = temprow + Setstone.vector_option[vecop][0]
				tempcol = tempcol + Setstone.vector_option[vecop][1]

	def set_stone(self,playernum,board,row,column):
		Setstone.get_board(self,board)
		Setstone.null_stone(self, row,column)
		Setstone.get_vector(self,row,column)
		Setstone.next_stone(self,playernum)
		Setstone.can_reverse_stone(self, playernum)
		Setstone.reverse_stone(self, playernum, row, column)
