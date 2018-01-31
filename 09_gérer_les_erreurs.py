#coding:utf-8

"""
Gérer les exceptions 		: try/except (+ else, finally)

Types d'exceptions 			: ValueError
							: NameError
							: TypeError
							: ZeroDivisionError
							: AssertionError
							: OSError

"""

# Gestion des erreurs pour un sécurisé le code 
## Jusqu'ici on faisait ...

ageUtilisateur = raw_input("Quel âge as-tu ? ")

ageUtilisateur = int(ageUtilisateur)

print("Tu as {} ans ".format(ageUtilisateur))


## On va gérer les cas d'erreur possible pour avoir un code plus propre


ageUtilisateur = raw_input("Quel âge as-tu ? ")

try :
	ageUtilisateur = int(ageUtilisateur)
	print("Tu as {} ans ".format(ageUtilisateur))
except : 
	print("L'âge indiqué est incorrect ! ")



## Un peu plus proprement

try :
	ageUtilisateur = int(ageUtilisateur)
except : 
	print("L'âge indiqué est incorrect ! ")
else : 	
	print("Tu as {} ans ".format(ageUtilisateur))



## synthase complète 

try :
	ageUtilisateur = int(ageUtilisateur)
except : 
	print("L'âge indiqué est incorrect ! ")
else : 	
	print("Tu as {} ans ".format(ageUtilisateur))
finally :
	print("Fin du programme ...")




#### Plusieurs types d'exceptions
nombre1 = 150
nombre2 = raw_input("Choisir le nombre pour diviser : ")
nombre2 = int(nombre2)

print("Résultat = {} ".format(nombre1 / nombre2))


nombre1 = 150
nombre2 = raw_input("Choisir le nombre pour diviser : ")

try :
	nombre2 = int(nombre2)										# possibilité de ValueError
	print("Résultat = {} ".format(nombre1 / nombre2))  			# possibilité de ZeroDivisionError
except ZeroDivisionError :
	print("Vous ne pouvez pas diviser par zéro.")
except ValueError :
	print("Vous devez entrer un nombre")
except : 
	print("Valeur incorrecte.")
else :
	print("Bravo, tu as noté un nombre valide !")
finally :
	print("Fin du programme ...")


#### Levée d'exception par nous même

try :
	age = int(raw_input("Quel âge as-tu ?"))

	if age < 25 :
		raise InventoryError("coucou :) !")
except InventoryError :
	print("J'ai attrapé ton exception inutile ;-) ")


#### Assertions
try :
	age = int(raw_input("Quel âge as-tu ?"))
	assert age < 25 

except AssertionError :
	print("J'ai attrapé l'exception ")


