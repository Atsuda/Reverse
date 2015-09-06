 # coding: UTF-8
class Rule():
    def set_stone(self,row,column):
        #石が置けるか判定
        if game.array[row][column] != 0:
            print "既に石がおいてあります"
