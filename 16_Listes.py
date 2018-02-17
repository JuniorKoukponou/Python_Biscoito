#coding:utf-8

'''
Création de liste  				: list(), [], ---> liste vide
				   				: [4, 5, 'moi', 98]
				   				: [0] * 10
				   				: range(20)

Accès à un élément d'une liste  : boucle for/while
								: liste[x]  = Affiche élément d'indice x 
								: liste[-x] = Affiche xème élément en partant de la fin
								: liste[:]  = Affiche tous les éléments
								: liste[x:] = Affiche les x derniers elements
								: liste[:x] = Affiche les x premiers elements 
								: liste[x:y:z] 

Modification de liste			: liste[x] = nouvelle_valeur
								: liste[x:x+k] = [nouvelle_valeur] * k

Recherche dans un liste			: if clause

Méthodes sur des liste 			: .append(<element>) ajouter un élément en fin de liste
								: .extend(<liste1>) ajouter une liste1 à une liste mère en fin de liste
								: .insert(<indce>, <nouvelle_valeur>) ajouter un élément à un endroit précis

								: .remove(<élément>) supprimer l'élément de la liste
								: del liste[indice]

								: .index(<element>) renvoie l'indice d'un élément (le premier rencontré)

								:.sort() tri une liste d'éléments de meme type

								: .reverse()
								: .count(<element>) nombre d'occurence de element

								: .clear() efface une liste

								: .split(<sep>)
								: <sep>.join()

								: enumerate()





'''

# inventaire = [] # list()
# inventaire = [0] * 10
inventaire = ['Arc', 'épée', 'bouclier', 'potion']


print(inventaire)

inventaire[:2] = ['bouclier d\'acier'] * 2

print(inventaire)
