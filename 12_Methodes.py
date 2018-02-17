
#coding:utf-8

'''
Méthode	(d'instance)		  : fonction sur une instance (objet)
Méthode de classe 			  : fonction sur une classe 
Méthode (de classe) statique. : fonction indépendante mais 'liée' à une classe
'''

class Humain :
	''' Classe qui définit les humain '''

	lieu_habitation = 'Terre'

	def __init__(self, nom, age) :
		self.nom = nom
		self.age = age

	def parler(self, message) :
		print('{} a dit : {}'.format(self.nom, message))


	# Pour une méthode de classe
	# cls au lieu self
	# cls  --> methode de classe
	# self --> methode standard

	def changer_planete(cls, nouvelle_planete) :
		Humain.lieu_habitation = nouvelle_planete


	ch_planete = classmethod(changer_planete)

	
	# Pour les methodes statiques, elles sont catégorisées dans une classe mais en sont indépendantes


	def definition() :
		print('l\'Humain est le plus haut etre vivant de la chaine alimentaire')


	definition = staticmethod(definition)





# Programme principal
h1 = Humain('Alex', 27)

# h1.parler('Bonjour à tous !  :-) ')

# h1.parler('Comment allez-vous ?')

print('Planète actuelle : {} '.format(Humain.lieu_habitation))


Humain.ch_planete('Mars')

print('Planète actuelle : {} '.format(Humain.lieu_habitation))

