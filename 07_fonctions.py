#coding:utf-8

'''
fonctions déja vues 	:	print(), input()
							type(), int(), float(), str(), bool()

Définition 				: une boîte

						: Il possède un nom

nommage de la fonction

paramètres 				: 0, 1, ...
						: nombre de paramètres inconnu

Valeur de retour 		: return (il faut en mettre qu'un seul à la fois)						
'''

# print('Bonjour à tous ! :) ')

def dire_bonjour() :
	print('Bonjour à tous ! :) ')

dire_bonjour()


def dire(nom_personne, message_personne) :
	print('{} : {}'.format(nom_personne, message_personne))


dire('Alex', 'Bonjour à tous')

dire('Juni', 'Salut Al, Comment tu vas ?')


# paramètre par défaut
def dire(nom_personne = 'Vaness', message_personne = 'Salut !') :
	print('{} : {}'.format(nom_personne, message_personne))

# Préciser l'ordre des arguments

def dire(nom_personne = 'Vaness', age_personne = 18, message_personne = 'Salut !') :
	print('{} ({} ans) : {}'.format(nom_personne, age_personne,message_personne))

dire('Will', 'Salut')

dire( message_personne = 'Je passe ce soir ! ', nom_personne = 'Will',age_personne = 18)



# Nombre de paramètres inconnu

def show_inventory(*list_tems) :
	for item in list_tems :
		print(item)


show_inventory('épée')
show_inventory('épée', 'arc', 'potion de nana', 'cape de Dragon rouge')


def calculer_somme(nombre1, nombre2) :
	#resultat = nombre1 + nombre2
	#return resultat
	return nombre1 + nombre2

print(calculer_somme(5, 16))


def le_plus_grand(nombre1, nombre2) :
	if nombre1 > nombre2 :
		return nombre1
	elif nombre1 < nombre2 :
		return nombre2
	else :
		return 'EGALITE !'

print(le_plus_grand(4, 9))
print(le_plus_grand(23, 16))
print(le_plus_grand(9, 9))



