#coding:utf-8
'''
Création de dictionnaire 		: dico = {} 									#vide
								: dico = {<cle> :<valeur>, <cle2> :<valeur2>} 	#pas d'ordre


Accès à une valeur 				: dico[<cle>]

Ajout et modification			: dico[<cle>] = <valeur>

Suppression						: .pop(<cle>)
								: del dico[<cle>]


Verifier si une clé existe		: if / (haskey : depreciated)

Parcourir un dictionnaire		: .keys(), .values(), .items()

Copie de dictionnaire			: .copy() 

Parametres nommées				: def maFonction(**parametres).                  #produit un dictionnaire


'''

dico = {}
dico = {1 : 145, 'prenom': 'Alex'}

#Si la clé est un entier, on accède à sa valeur sans le double cote

dico = {'chat' : 'c\'est un félin'}

dico['chien'] = 'c\'est un mammifère'

print(dico)

dico.pop('chien')
