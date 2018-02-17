#coding:utf-8

class Point(object) :
	''' Définition d'un point géométrique '''
	pass




#Programme principal

p9 = Point()

print(p9)
print(p9.__doc__)

#

p9.x = 3.
p9.y = 4.
print(p9.x, p9.y)

print(p9.x**2 + p9.y**2)

def affiche_point(p) :
	print('coord. horizontale = {}, coord. verticale = {}'.format(p.x, p.y))


affiche_point(p9)


def distance(point1, point2):
	'''calculer la distance euclidienne entre deux points, point1 et point2'''
	import math

	print('La distance euclidienne entre {} et {} est : {} '.format(point1, point2,
		 math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)))


p10 = Point()
p10.x = 3.
p10.y = 5.

distance(p10, p9)


class Rectangle(object) :
	''' Définition d'une classe de rectangles :
			rectangles obliques exclus
			Un rectangle est défini à partir de la position du coin supérieur 
			gauche et la taille (longueur et largeur)

	'''
	pass

	# Methode TrouveCentre : prend en argument un rectangle et renvoie le point qui représente
	#le centre de ce rectangle


