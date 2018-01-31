#coding:utf-8

'''
Opérateurs de comparaison 		: == (égal à)
								: != (différent de)
								: < (plus petit que)
								: > (plus grand que)
								: <= (inférieur ou égal à)
								: >= (supérieur ou égal à)

Conditions multiples 			: and (ET)
								: or (OU)
								: in / not in (DANS / PAS DANS) 



Mots clés des Conditions 		: if / elif / else 
'''

identifiant = 'Will'
mot_de_passe = 'password123'

print('Interface de connexion')

user_id = input('Entrez votre identifiant : ')
user_password = input('Entrez votre mot de passe : ')


if user_password == mot_de_passe :
	print('Vous êtes connectés, bienvenue', user_id)


print('je ne suis plus dans le 'if' ')


## AND
if user_id == identifiant and user_password == mot_de_passe :
	print('Vous êtes connectés, bienvenue', user_id)


print('je ne suis plus dans le 'if' ')


## OR
if user_id == identifiant or user_password == mot_de_passe :
	print('Vous êtes connectés, bienvenue', user_id)


print('je ne suis plus dans le 'if' ')


## IN 

lettre_hasard = 'b'

if lettre_hasard in 'aeiouy' :
	print('C\'est une voyelle')

## NOT IN
lettre_hasard = 'b'

if lettre_hasard not in 'aeiouy' :
	print('C\'est une consonne')



## if - else
if lettre_hasard in 'aeiouy' :
	print('C\'est une voyelle')

else :
	print('C\'est une consonne')



## if - elif - else

age = 24

if age == 18 :
	print('Tu viens d\'être majeur')
elif age == 50 :
	print("Tu viens d'avoir 50 ans")
elif age == 60 :
	print("Tu viens d'avoir 60 ans")
else :
	print("Tu as", age, "ans")


## 

jeu_charge = True 				# True = vrai (= 1)

if jeu_charge :
	print('Le jeu est en marche')
else :
	print('Le jeu est éteint')


## 

if not jeu_charge :
	print('Le jeu est éteint')
else :
	print('Le jeu est lancé')



## 

age = int(input("Quel âge as-tu ? "))


'''
age > 0 ET age <= 100 --> 0 < age <= 100

'''

if 0 < age <= 100 :
	print("L'âge est validé ")

else :
	print("L'âge est incorrect")


