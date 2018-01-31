#coding:utf-8

'''

Nommer une variable 	: doit commencer par une lettre ou un underscore
						: ne pas contenir de caractères spéciaux
						: ne pas contenir d'espaces
						: utiliser des underscores (_)

typage dynamique   		: pas besoin d'indiquer le type de la variable
						: pas besoin de int agePersonne = 14
Types standards			: entier numériques (int)
						: nombre flottant (float)
						: chaîne de caractères (str)
						: booléen (bool)
						: Autres (listes, dictionnaires, tuples, objets, etc...)

Fonction vues 			: print()				-> afficher à l'écran
						: input()				-> lire au clavier
						: type()				-> retourne le type d'une donnée, variable, etc.
						: int(), str(), bool()  -> 'caster' une donnée ie la convertir
						: str.format()			-> formater une chaine de caractères


'''

""" 
agepersonne
age_personne
agePersonne
agePersonne
_agePersonne
"""

agePersonne = 14 
agePersonne2 = '14' 

prixHT = 120.58
continuer_partie = True

nombre_hexadecimal = 0xFAD5B8
nombre_octave = 0705


print(agePersonne == agePersonne2)
print(type(agePersonne))
print(type(agePersonne2))

print(type(nombre_hexadecimal))
print(nombre_hexadecimal)

print('agePersonne')
print(agePersonne)

print('Age de la personne : ', agePersonne, '.')


texte = "L'age de la personne est {}, et le prix est {}€."
print(texte.format(agePersonne, prixHT))



nomJoueur = input("Choisissez un nom de joueur : ")

print('Bienvenue, ', nomJoueur)



prixHT = input('Entrez un prix HT : ')

prixTTC = prixHT + prixHT * 20/100

print("prix TTC = ", prixTTC)


## 
False == 'False'
125 == '125'