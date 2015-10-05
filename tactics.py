# -*- coding: utf-8 -*-
import setstone
from board import count_stone1
from copy import deepcopy

class Tactics():
	#cpuプレイヤーの戦略
	predict_range =3 #何手先まで予測するかを決める
	def __init__(self):
		self.predict_list_1 = {} #predict_1関数の結果の入れ物。keyはpredict_list_id
		self.predict_list = {} #predict_1、predict_n関数の結果の入れ物。keyは、1→次の1手、2→その次の相手の1手、・・・になる。
		self.predict_list_id = 0
		self.child_max_n_list = {} #predict_child_max_nで使用。keyはpredict_list_id、valueはparentがkeyと一致する手の、count_stone1の最大値。
		self.minimax_list = {} #predict_child_maxで使用。keyはpredict_list_id、valueはparentがkeyと一致する手の、child_max_n_listの最大値。

	def predict_1(self,playernum,playboard):
		#1手予測する
		for row in range(1,9):
			for column in range(1,9):
				predict = setstone.Setstone()
				if predict.can_set_stone(playboard,playernum,row,column):
					predict.set_stone(playboard,playernum,row,column)
					self.predict_list_1[self.predict_list_id]={"parent_id":-1,"playernum":playernum,"playboard":predict.playboard,"row":row,"column":column,"stone1_count":count_stone1(predict.playboard,playernum)}
					self.predict_list_id=self.predict_list_id+1
		self.predict_list[1]=self.predict_list_1

	def predict_n(self,playernum,playboard,n=predict_range):
		#n手予測する(n>=2)
		Tactics.predict_1(self,playernum,playboard)
		for num in range(1,n):
			temp_predict_list = deepcopy(self.predict_list[num])
			temp_predict_result = {} #処理結果の一時的な入れ物
			playernum = playernum*(-1)
			for num2 in temp_predict_list.keys():
				for row in range(1,9):
					for column in range(1,9):
						predict = setstone.Setstone()
						if predict.can_set_stone(temp_predict_list[num2]["playboard"],playernum,row,column):
							predict.set_stone(temp_predict_list[num2]["playboard"],playernum,row,column)
							temp_predict_result[self.predict_list_id]={"parent_id":num2,"playernum":playernum,"playboard":predict.playboard,"row":row,"column":column,"stone1_count":count_stone1(predict.playboard,playernum)}
							self.predict_list_id=self.predict_list_id+1
			self.predict_list[num+1]=temp_predict_result

	def predict_child_max_n(self,n=predict_range):
		#minimax法を使うために、predict_listから、parent_idが同じであるリストが持つstone1_countを比較し、その最大値とparent_idを紐付ける。
		pl=self.predict_list[n] #3手目のリストを取得
		for num in pl.keys():
			parent_id = pl[num]["parent_id"]
			stone1_count = pl[num]["stone1_count"]
			if not self.child_max_n_list.has_key(parent_id):
				self.child_max_n_list[parent_id] = {"predict_list_id":num,"stone1_count":stone1_count}
			else:
				if self.child_max_n_list[parent_id]["stone1_count"]<stone1_count:
					self.child_max_n_list[parent_id] = {"predict_list_id":num,"stone1_count":stone1_count}
				else:
					pass

	def minimax_n(self,n=predict_range):
		Tactics.predict_child_max_n(self,Tactics.predict_range)
		#predict_nで出したpredict_listに対して、minimax法で最適な次の1手である、predict_list_idを取得
		for num in self.child_max_n_list.keys():
			self.minimax_list[num] = {"predict_list_id":self.child_max_n_list[num]["predict_list_id"],"stone1_count":self.child_max_n_list[num]["stone1_count"]*(-1)}
			#stone1_countに-1をかけたものを、child_max_listに入れる
		n=n-1

		while n >= 1:
			temp_minimax_list = {}
			pl=self.predict_list[n] #2手目のリストを取得
			for num in pl.keys():
				parent_id = pl[num]["parent_id"]
				stone1_count = self.minimax_list[num]["stone1_count"]
				if not temp_minimax_list.has_key(parent_id):
					temp_minimax_list[parent_id] = {"predict_list_id":num,"stone1_count":stone1_count}
				else:
					if temp_minimax_list[parent_id]["stone1_count"]<stone1_count:
						temp_minimax_list[parent_id] = {"predict_list_id":num,"stone1_count":stone1_count}
					else:
						pass
			self.minimax_list = {}
			for num in temp_minimax_list.keys():
				self.minimax_list[num] ={"predict_list_id":temp_minimax_list[num]["predict_list_id"],"stone1_count":temp_minimax_list[num]["stone1_count"]*(-1)}
			n=n-1
		temp_predict_list_id = self.minimax_list[-1]["predict_list_id"]
		global row
		global column
		row = self.predict_list[1][temp_predict_list_id]["row"]
		column = self.predict_list[1][temp_predict_list_id]["column"]
		print "row:%d"%(row)
		print "column:%d"%(column)
		return row,column

def run_minimax_set_stone(playernum,playboard):
	pre = Tactics()
	pre.predict_n(playernum,playboard)
	pre.minimax_n()
	temp_turn = setstone.Setstone()
	temp_turn.set_stone(playboard,playernum,row,column)
	return temp_turn.playboard
