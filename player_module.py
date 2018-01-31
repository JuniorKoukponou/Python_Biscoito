#coding:utf-8

"""
Module pour le joueur
"""

def parler(personnage, message) :
	print('{} : {}'.format(personnage, message))



def au_revoir():
	print('Bye bye ...')



# pour tester que le module tout seul fonctionne bien (des tests isolés)
if __name__ == "__name__" :
	parler('Al', 'Doudou')
	au_revoir()