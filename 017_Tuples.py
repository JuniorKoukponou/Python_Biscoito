#coding:utf-8

'''
(!) Tuple conteneur immuable

Création de tuple : mon_tuple = ()      	#vide
					mon_tuple = 17,     	#Une seule valeur
					mon_tuple = (17,)   	#Idem qu'au dessus
					mon_tuple = (4, 6)  	#Plusieurs valeurs


Acces aux valeurs : mon_tuple[x]			#valeur d'indice x


Intéret des tuples : Affectation multiple, dans ce cas on peut modifier les valeurs
					 Retour multiple de fonction

					


'''

liste = [1, 2, 3, 4, 5, 6]

for chose in enumerate(liste) :
	print(chose)

# Créer un tuple

mon_tuple = ()
print(type(mon_tuple))

mon_tuple = (45)
print(type(mon_tuple))

mon_tuple = (45, )
print(type(mon_tuple))

mon_tuple = 45, 
print(type(mon_tuple))

def get_position_player() :
	posX = 173
	posY = 59

	return (posX, posY)



#Programme principal
coordX, coordY = 0, 0

print('Position du joueur : ({} /{})'.format(coordX, coordY))


coordX, coordY = get_position_player()

#On peut modifier les valeurs de ce tuple
coordX, coordY = 145, 122

print('Position du joueur : ({} /{})'.format(coordX, coordY))