#coding:utf-8

# Héritage

class Mammifere():
	caract1 = 'il allaite ses petits ; '

class Carnivore(Mammifere):
	caract2 = 'il se nourri de la chair de ses proies ; '

class Chien(Carnivore):
	caract3 = 'son cri s\'appelle aboiement ; '


mirza = Chien()

print(mirza.caract1, mirza.caract2, mirza.caract3)

# mirza hérite bien des caractéristiques de Mammifere, Carnivore et Chien (son prototype)
# Ici, on a utilisé des attributs de classe et non des attributs d'instances


# Règle de priorité :

# Lorsqu'on demande d'utiliser la valeur d'une variable, 'alpha', Python cherche d'abord dans l'espace local
# s'il trouve une valeur dans cet espace, c'est celle là qui sera utilisée et la recherche s'arrête.
# s'il ne trouve pas, Python examine l'espace de nom de la structure parente, puis de la structure grand-parente,
# et ainsi de suite jusqu'au niveau principal du programme.


# Héritage et polymorphisme

class Atome():
	""" Atomes simplifiés, choisis parmi les 10 premiers elements du TP """
	table = [None, ('hydrogène',0), ('hélium',2), ('litium',4), ('béryllium',5),
	('bore',6), ('carbone',6), ('azote',7), ('oxygène',8), ('fluor',10), ('néon',10)]

	def __init__(self, nat) :
		''' Le n° atomique détermine le nombre de protons d'électrons et de neutrons'''

		self.np = nat
		self.ne = nat
		self.nn = Atome.table[nat][1]

	def affiche(self):
		print()
		print('Nom de l\'élément : {}'.format(Atome.table[self.np][0]))
		print('{} protons, {} électrons, {} neutrons'.format(self.np, self.ne, self.nn))



class Ion(Atome):
	"""Les ions sont des atomes qui ont gagné ou perdu des électrons"""

	def __init__(self, nat, charge):
		''' le n° atomique et la charge électrique déterminent l\' ion '''
		Atome.__init__(self, nat)

		self.ne = self.ne - charge
		self.charge = charge



	def affiche(self) :
		Atome.affiche(self)
		print('Particule électrisé. Charge = {} '.format(self.charge))


a1 = Atome(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)

a1.affiche()
a2.affiche()
a3.affiche()


##### EXOS
	
class Cercle():	
	""" Construit des cercles de tailles variées"""
	def __init__(self, rayon):
		self.rayon = rayon

	def surface(self) :
		import math
		return math.pi * (self.rayon)**2 


class Cylindre(Cercle):
	"""Cylindre dérivé de la classe Cercle"""
	def __init__(self, rayon, hauteur):
		Cercle.__init__(self, rayon)
		self.hauteur = hauteur

	def volume(self):
		import math
		return math.pi * self.hauteur * (self.rayon)**2 
 
		
cyl = Cylindre(5, 7)
print(cyl.surface())

print(cyl.volume())


# 

class Cone(Cylindre):
	""" Dérivé de la classe Cylindre """
	def __init__(self, rayon, hauteur):
		Cylindre.__init__(self, rayon, hauteur)

	def volume(self):
		import math
		return (math.pi * self.hauteur * (self.rayon)**2) / 3
 
co = Cone(5, 7)
print(co.volume())


class JeuDeCartes():
	"""Similaire au comportement d'un vrai jeu de cartes"""
	def __init__(self):
		self.cartes = []

		self.couleurs = [('Coeur', 3), ('Carreau', 2), ('Trèfle', 1), ('Pique', 0)] 
		
		for val in range(2, 15) :
			for col in self.couleurs :
				tuple = (val, col[1])
				self.cartes.append(tuple)

		print(self.cartes)

	def nom_carte() :
		pass

	def battre()



jeu = JeuDeCartes()
jeu







