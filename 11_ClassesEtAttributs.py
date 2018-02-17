#coding:utf-8

# Classe 		: plan de conception, genre (ex : Humain)
# Objet 		: instance de classe, quelque chose qui est du genre de cette Classe (ex : William est un Humain)
# Attribut 		: Variable de la classe, caractéristique d'une classe et n'est pas valide en dehors de celle-ci, (ex prenom, sexe, ...)


# On va créer notre première classe (Humain) 

class Humain :
	'''
	Classe des êtres humains

	'''

	def __init__(self, c_prenom, c_age) :

		'''
		Le constructeur

		self : cible l'objet lui même

		'''
		print('Création d\'un Humain ...')
		# print('Création d\'un Humain', self) # pass
		# self.prenom = 'Vaness'
		# self.age = 1

		self.prenom = c_prenom
		self.age = c_age


print("Lancement du programme ...")


# Vraiment deux objets

# h1 = Humain()

# Les attributs sont définies dans le constructeurs

h1 = Humain('Vaness', 32)

print('Le prenom de h1  -> {}'.format(h1.prenom))
print('L\'age de h1  -> {}'.format(h1.age))

h2 = Humain('Will', 34)
print('Le prenom de h2  -> {}'.format(h2.prenom))
print('L\'age de h2  -> {}'.format(h2.age))

# On peut changer la valeur d'un attribut d'une classe directement en faisant :
# Pas obligé de passer par des accesseurs comme en C++ par exemple

h2.prenom = 'Junior'
print('Le prenom de h2  -> {}'.format(h2.prenom))



## Attribut de classe
# Il appartient pas à un objet de la classe en particulier
# Il est le meme pour tous les objets la classe qu'on va créer

# On le cré dans la définition de la classe elle-meme

class Humain :
	'''
	Classe des êtres humains

	'''
	# C'est un peu comme une variable globale pour toute la classe
	humains_crees = 0

	def __init__(self, c_prenom, c_age) :

		print('Création d\'un Humain ...')
		

		self.prenom = c_prenom
		self.age = c_age
		Humain.humains_crees +=1 # Ici ce n'est pas self.humains_crees mais bien Humain.humains_crees


print("Lancement du programme ...")


h1 = Humain('Vaness', 32)
print('Humains existants : {} '.format(Humain.humains_crees))


h2 = Humain('Will', 33)
print('Humains existants : {} '.format(Humain.humains_crees))















