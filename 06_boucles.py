#coding:utf-8


"""
Boucles 		: while / for 
Mots-clés 		: break (casse la boucle)
				: continue (revient au début de la boucle)

"""
# Pour éviter les répétitions de code

#print("Je suis une phrase")
#print("Je suis une phrase")
#print("Je suis une phrase")
#print("Je suis une phrase")


## while

compteur = 0

while compteur < 5 :
	print("Je suis une phrase")
	compteur += 1

print("Je suis sorti de la boucle")

jeu_lance = True 

while jeu_lance :
	# Fais des instructions en rapport avec le jeu_lance
	choixMenu = input("> ")
	if choixMenu == 'again' :
		continue

	elif choixMenu == "quit" :
		jeu_lance = False
		# break

	elif choixMenu == 'hello' :
		print("Bonjour :) !")

	else :
		print("Commande introuvable")

print("À bientôt")


## for  (parcours de séquences)

phrase = "Bonjour tout le monde :) !"

for lettre in phrase :
	print(lettre) 



print("À bientôt")


