# -*- coding: utf-8 -*-
import setstone
from board import count_stone1
from copy import deepcopy

class Tactics():
	#cpuプレイヤーの戦略
	predict_range =3 #何手先まで予測するかを決める
	def __init__(self):
		self.predict_list_1 = {} #predict_1関数の結果の入れ物。keyはpredict_list_id
		self.predict_list = \
		{1:\
		{0:\
		{"parent_id":-1}\
		,1:\
		{"parent_id":-1}\
		,2:\
		{"parent_id":-1}\
		}\
		,2:\
		{3:\
		{"parent_id":0}\
		,4:\
		{"parent_id":0}\
		,5:\
		{"parent_id":1}\
		,6:\
		 {"parent_id":1}\
		,7:\
		{"parent_id":2}\
		,8:\
		{"parent_id":2}\
		}\
		,3:\
		{9:\
		{"parent_id":3,"stone1_count":8}\
		,10:\
		{"parent_id":3,"stone1_count":6}\
		,11:\
		{"parent_id":4,"stone1_count":9}\
		,12:\
		{"parent_id":4,"stone1_count":46}\
		,13:\
		{"parent_id":5,"stone1_count":22}\
		,14:\
		{"parent_id":5,"stone1_count":4}\
		,15:\
		{"parent_id":6,"stone1_count":6}\
		,16:\
		{"parent_id":6,"stone1_count":5}\
		,17:\
		{"parent_id":7,"stone1_count":2}\
		,18:\
		{"parent_id":7,"stone1_count":3}\
		,19:\
		{"parent_id":8,"stone1_count":12}\
		,20:\
		{"parent_id":8,"stone1_count":1}\
		}\
		}
		self.predict_list_id = 0
		self.child_max_n_list = {} #predict_child_max_nで使用。keyはpredict_list_id、valueはparentがkeyと一致する手の、count_stone1の最大値。
		self.child_max_list = {} #predict_child_maxで使用。keyはpredict_list_id、valueはparentがkeyと一致する手の、child_max_n_listの最大値。
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
		#predict_nで出したpredict_listに対して、minimax法で最適な次の1手を決める
		for num in self.child_max_n_list.keys():
			self.child_max_list[num] = {"predict_list_id":self.child_max_n_list[num]["predict_list_id"],"stone1_count":self.child_max_n_list[num]["stone1_count"]*(-1)}
			#stone1_countに-1をかけたものを、child_max_listに入れる
		n=n-1
		print self.child_max_list

		while n >= 1:
			temp_child_max_list = {}
			pl=self.predict_list[n] #2手目のリストを取得
			for num in pl.keys():
				parent_id = pl[num]["parent_id"]
				stone1_count = self.child_max_list[num]["stone1_count"]
				if not temp_child_max_list.has_key(parent_id):
					temp_child_max_list[parent_id] = {"predict_list_id":num,"stone1_count":stone1_count}
				else:
					if temp_child_max_list[parent_id]["stone1_count"]<stone1_count:
						temp_child_max_list[parent_id] = {"predict_list_id":num,"stone1_count":stone1_count}
					else:
						pass
			self.child_max_list = {}
			for num in temp_child_max_list.keys():
				self.child_max_list[num] ={"predict_list_id":temp_child_max_list[num]["predict_list_id"],"stone1_count":temp_child_max_list[num]["stone1_count"]*(-1)}
			print(self.child_max_list)
			n=n-1
