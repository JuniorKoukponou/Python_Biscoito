#coding:utf-8

'''
importer un module 		: import <nom_module>
						: from <nom_module> import <nom_fonction>
						: from <nom_module> import *


création de module 		: 
						: dans un repertoire

Tests isolés en fin de module
'''

#Fonction lambda
#coucou = lambda:print('Bonjour')  # <=> def :
						   		   #		print('Bonjour')

#coucou()

ttc = lambda prixHT : prixHT + (prixHT * 20/100)

print(ttc(24))

calculer = lambda a, b : a + b

print(calculer(13, 27))

# Modularité Module == bibliothèque
import math 

# from math import sqrt # pas besoi

resultat = math.sqrt(100)

print(resultat)

import os

# os.system('clear')

import player_module

player_module.au_revoir()


player_module.parler('Al', 'Coucou toi !')


###
from player_module import parler
from player_module import au_revoir

au_revoir()
parler('Al', 'Coucou toi !')



###
import includes.player_module # as player

includes.player_module.au_revoir()

includes.player_module.parler('Al', 'Coucou toi !')

