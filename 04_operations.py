# -*- coding: utf-8 -*-
'''
Opérateurs 			        : + (addition)
							: - (soustraction)
							: * (multiplication)
							: / (division)
							: % (modulo). -> reste d'une division euclidienne


Priorité des opérateurs 	: parenthèse / modulo, multiplication, division/ soustraction, addition


variable = variable + x  <=> variable += x
variable = variable - x  <=> variable -= x
variable = variable * x  <=> variable *= x

'''

calcul = 5 / 2 

# calcul = int(calcul)
calcul = calcul

calcul2 = 5 % 2 
print('Résultat = ', calcul, 'reste', calcul2 )


niveauPersonnage = 1

print('Niveau du personnage : ', niveauPersonnage)

print('Combat réussi, tu gagnes deux niveaux')
niveauPersonnage = 2

print('Niveau du personnage : ', niveauPersonnage)



niveauPersonnage = input('Niveau de départ ? ')
niveauPersonnage = int(niveauPersonnage)

print('Niveau du personnage : ', niveauPersonnage)
print('Combat réussi, tu gagnes deux niveaux')
#niveauPersonnage = niveauPersonnage + 1
niveauPersonnage += 1

print('Niveau du personnage : ', niveauPersonnage)
