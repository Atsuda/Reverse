# -*- coding: utf-8 -*-
class Setstone():
	right_vec=[]
	rightUp_vec=[]
	Up_vec=[]
	leftUp_vec=[]
	left_vec=[]
	leftDown_vec=[]
	down_vec=[]
	rightDown_vec=[]
	vector_list = {1:right_vec,2:rightUp_vec,3:Up_vec,4:leftUp_vec,5:left_vec,6:leftDown_vec,7:down_vec,8:rightDown_vec}
	#単位ベクトルをオプションとする。
	right_vecop=[0,1]
	rightUp_vecop=[-1,1]
	Up_vecop=[-1,0]
	leftUp_vecop=[-1,-1]
	left_vecop=[0,-1]
	leftDown_vecop=[1,-1]
	down_vecop=[1,0]
	rightDown_vecop=[1,1]
	vector_option = {1:right_vecop,2:rightUp_vecop,3:Up_vecop,4:leftUp_vecop\
	,5:left_vecop,6:leftDown_vecop,7:down_vecop,8:rightDown_vecop}
	next_stone_vector_option = [] #next_stoneメソッドで取得するリストの入れ物
	def zero_stone(self,row,column):
		#石が置いてあるか判定
		if self.board[row][column] == 0:
			pass
		else:
			print 'err'
	"""	def get_vector(self,playernum,row,column):
		#指定した座標を開始点にしたベクトル取得
		right_vec=[0,1]
		rightUp_vec=[-1,1]
		Up_vec=[0,-1]
		leftUp_vec=[-1,-1]
		left_vec=[-1,0]
		leftDown_vec=[-1,1]
		down_vec=[0,1]
		rightDown_vec=[1,1]
		vecOption = {1:right_vec,2:rightUp_vec,3:Up_vec,4:leftUp_vec,5:left_vec,6:leftDown_vec,7:down_vec,8:rightDown_vec}
		for num in range(1,8):"""
	def get_vector(self,row,column):
		#指定した座標からボード端までのベクトルを取得(指定した座標は除く)
		#TODO plyernum修正
		for num in range(1,9):
			temprow=row
			tempcol=column
			while self.board[temprow][tempcol]!=2:
				Setstone.vector_list[num].append(self.board[temprow][tempcol])
				temprow = temprow+Setstone.vector_option[num][0]
				tempcol = tempcol+Setstone.vector_option[num][1]
			print num
			Setstone.vector_list[num].append(2)
			print (Setstone.vector_list[num])
	def next_stone(self,playernum):
		#隣の石が相手の石か判定し、隣の石が相手の石であるベクトルのvector_optionのキーのリストを作成
		for num in range(1,9):
			if Setstone.vector_list[num][1]==playernum*(-1):
				print "ok"
				Setstone.next_stone_vector_option.append(num)
			else:
				print "ng"
	def can_reverse_stone(self,playernum):
		#連続する相手の石の次が自分の石であるかの判定
		for num in Setstone.next_stone_vector_option:
			for vecnum in range(1,len(Setstone.vector_list[num])):
				if Setstone.vector_list[num][vecnum]==playernum*(-1):
					pass
				elif Setstone.vector_list[num][vecnum]==playernum:
					print num,vecnum
					break
				else:
					break