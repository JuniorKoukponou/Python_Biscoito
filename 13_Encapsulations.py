#coding:utf-8

'''
Propriété  : manière de manipuler/controler des attributs 
			 principe d'encapsulation !
'''



class Humain :

	def __init__(self, nom, age) :
		print('Création d\'un Humain ....')

		self.nom = nom
		self._age = age

	# Propriété : permet de controler/manipuler les attributs (fort dans d'autres langages)
	#			  Tout ce qui est attribut ne peut être lu/modifier en dehors de la classe
	# Convention _Nom de l'attribut


	def _getage(self):
		#print('Récupération non autorisée')
		try : 
			return self._age
		except AttributeError :
			print('L\'age n\'existe pas !')

	def _setage(self, nouvel_age) :
		if nouvel_age < 0 :
			self._age = 0 
		else :
			self._age = nouvel_age

	def _delage(self) :
		del self._age



	# property(<getter>, <setter>, <deleter>, <helper>)
	age = property(_getage, _setage, _delage, 'Je suis l\'age d\'un humain')



# Programme principal

h1 = Humain('Alex', 27)

print(h1.age)

#h1.age = -7
del h1.age
print(h1.age)

#help(Humain.age)
