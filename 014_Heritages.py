#coding:utf-8

# Héritage 	: classe Fille qui hérite d'une classe Mère.
#.            On dit que Fille est une sorte de Mère


#Classe Mère
class Vehicule :

	def __init__(self, nom_vehicule, quantite_carburant) :
		self.nom = nom_vehicule
		self.essence = quantite_carburant


	def montrer_vehicule(self):
		return self.nom

	def se_deplacer(self) :
		print('Le véhicule {} se déplace ...'.format(self.nom))



#classe Fille
class Voiture(Vehicule) :
	def __init__(self, nom_vehicule, essence, puissance) :
		Vehicule.__init__(self, nom_vehicule, essence)
		self.puissance = puissance

	# On peut redefinir une méthode de la classe Mère
	def se_deplacer(self) :
		print('Je roule ...')

#Une classe Petite-Fille
class VoitureSport(Voiture) :
	pass



class Avion(Vehicule) :
	def __init__(self, nom, essence, marchandise) :
		Vehicule.__init__(self, nom, essence)
		self.marchandise = marchandise

	def se_deplacer(self) :
		print('Je vole ...')

# On peut faire un héritage multiple (sous Python) tous langages de programmation ne propose pas ca
# Exemple :

#Classe Mere 1
class Etudiant :
	pass

#Classe Mere 2
class Enseignant :
	pass

#Classe Fille
class Doctorant(Enseignant, Etudiant) :
	pass



# Programme principal
#v1 = Vehicule('F22 Raptor', 2500)

voiture1 = Voiture('Toyota supra', 90, 420) 
voiture1.se_deplacer()
print(voiture1.puissance, 'CH')

avion1 = Avion('F22 Raptor', 2400, 'Missiles')
avion1.se_deplacer()


#------------ QUELQUES FONCTIONS UTILES

'''
isinstance(<objet>, <classe>)   : Verifie qu'un objet est de la classe renseihnée

issubclass(<classe_fille>, <classe_mere>) Vérifie qu'une classe est fille d'une autre
'''
class Animal:
	def __init__(self, nom):
		self.nom = nom

	def manger(self):
		print(self.nom, 'mange ...')


class Reptile(Animal):

	def __init__(self, nom, regime_alimentaire):
		Animal.__init__(self, nom)
		self.regime = regime_alimentaire

	def manger(self):
		print('Le reptile mage ...')

# Code principal
lezard = Reptile('Lézard', 'grenouilles')

if isinstance(lezard, Animal) :
	print('Lézard est un Animal')

if issubclass(Reptile, Animal) :
	print('Reptile hérite de Animal')
#



