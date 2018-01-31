#coding:utf-8

class Lapin:
	def __init__(self, name, weight) :
		self.name = name
		self.weight = weight


	def __repr__(self) :
		return "Lapin {} de {} kg".format(self.name, self.weight)

	def __eq__(self, other):

		return self.weight == other.weight




lp = Lapin('coco', 25)
lp2 = Lapin('Titi', 7)

#print(lp)


if lp == lp2 :
	print('Ce sont les mêmes')

else :
	print('Ces lapins sont différents')