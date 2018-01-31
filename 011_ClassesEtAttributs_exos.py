#coding:utf-8

# [objet = attributs + méthodes]

class Time() :
	''' Définition d'objets temporels '''

	def __init__(self, heure = 15, minute = 30 , seconde = 0) :
		self.heure = str(heure)
		self.minute = str(minute)
		self.seconde = str(seconde)


	def affiche_heure(self):
		print(':'.join([self.heure, self.minute, self.seconde]))


# programme principal
rdv = Time()
rdv.affiche_heure()

instant= Time(11, 34, 25)
instant.affiche_heure()


###
class Domino():
	'''
	'''
	def __init__(self, faceA = 0, faceB =0) :
		self.faceA = faceA
		self.faceB = faceB


	def affiche_points(self):
		print('face A : {},  face B : {} '.format(self.faceA, self.faceB))

	def valeur(self) :
		return self.faceA + self.faceB


d1 = Domino(2, 6)
d2 = Domino(4, 3)

d1.affiche_points()
d2.affiche_points()

print(d1.valeur())
print('total des points : {}'.format(d1.valeur() + d2.valeur()))

liste_dominos = []
for i in range(7) :
	liste_dominos.append(Domino(6, i))

print(liste_dominos[3])

dom3 = liste_dominos[3]
dom3.affiche_points()

###


class CompteBancaire():

	def __init__(self, nom = 'Dupont', sexe = 'M', solde = 1000) :

		self.nom = nom
		self.solde = solde
		self.sexe= sexe

	def depot(self, somme):
		self.solde += somme
		if self.sexe == 'M' :
			print('M. {} vient de déposer {}'.format(self.nom, somme))

		elif self.sexe == 'F' :
			print('Mme. {} vient de déposer {}'.format(self.nom, somme))

	def retrait(self, somme):
		self.solde -= somme
		print('{} vient de retirer {}'.format(self.nom, somme))

	def affiche(self):
		if self.sexe == 'M' :
			print('Le solde du compte bancaire de M. {} est de {} euros'.format(self.nom,
			self.solde))
		elif self.sexe == 'F' :
			print('Le solde du compte bancaire de Mme {} est de {} euros'.format(self.nom,
			self.solde))


cmp1 = CompteBancaire('Duchmol', 'F',800)
cmp1.affiche()

cmp1.depot(350)
cmp1.retrait(200)
cmp1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.retrait(1026)
compte2.affiche()



###

class Voiture() :
	def __init__(self, marque = 'Ford', couleur = 'rouge', pilote = 'personne', vitesse = 0):
		self.marque = marque
		self.couleur = couleur
		self.pilote = pilote
		self.vitesse = vitesse
	
	def choix_conducteur(self, nom):
		self.pilote = nom
		print('Votre nouveau pilote est {}'.format(nom))

	def accelerer(self, taux, duree):

		if self.pilote == 'personne' :
			self.vitesse  = 0
			print('Cette voiture n\'a pas de conducteur \nMerci de choisir un pilote avant de conduire la Voiture ...')
			
		else :
			self.vitesse = taux * duree

			if self.vitesse  > 0 : print('Allez, on accélère ...')

			else : print('Allez, on décélère ...')

	def affiche_tout(self) :
		print('{} {} piloté par {}, vitesse {} m/s'.format(self.marque, self.couleur,
			self.pilote, self.vitesse))


a1 = Voiture('Peugeot', 'bleue')

a2 = Voiture(couleur = 'verte')

a3 = Voiture('Mercedes')

a1.choix_conducteur('Roméo')

a2.choix_conducteur('Juliette')

a2.accelerer(1.8, 12)

a3.accelerer(1.9, 11)

a1.affiche_tout()

a2.affiche_tout()

a3.affiche_tout()


class Satellite() :
	
	def __init__(self, nom, masse, vitesse) :
		self.nom = nom
		self.masse = masse
		self.vitesse = vitesse


	def impulsion(self, force, duree) :

		# A améliorer pour les décélération
		self.vitesse  += (force * duree)/self.masse

		return self.vitesse

	def energie(self) :
		return (self.masse * self.vitesse**2)/2

	def affiche_vitesse(self) :
		print('Vitesse du satellite {} = {} m/s'.format(self.nom, self.vitesse))


s1 = Satellite('zoé', masse = 250, vitesse = 10)
s1.impulsion(500, 15)
s1.affiche_vitesse()
print(s1.energie())

s1.impulsion(500, 15)
s1.affiche_vitesse()
print(s1.energie())

s1.impulsion(500, 1)
s1.affiche_vitesse()
print(s1.energie())


###

class Espace():
	aa = 33 # espace de nom de la classe
	def affiche(self) :
		print(aa, Espace.aa, self.aa)

aa = 12 # espace de nom principal
essai = Espace()
essai.aa = 67 # espace de nom de l'instance
essai.affiche()

print(aa, Espace.aa, essai.aa)





















