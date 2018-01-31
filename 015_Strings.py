#coding:utf-8

'''
Une méthode de chaîne travaille sur une copie, et pas sur la chaîne elle-même.


str.upper(), str.lower(), str.capitalize(), str.title(), str.center(<largeur>, [<caractere_remplissage>])
str.strip(), str.split()


- Verification/Recherche dans une chaîne de caractères
str.find(<chaine>, <debut>, <fin>)
str.index(<chaine>, <debut>, <fin>)
str.replace(<ancienne>, <nouvelle>, <occurrence>)


- Vérifications sur les nombre
str.isalpha(), str.isdigit(), str.isnumeric(), str.isalphanum(), 

- Test sur les chaîne de caractères
str.islower(), str.isupper()

str.isidentifier(), str.iskeyword()

'''
# Classes str : string (chaîne de caractères)
help(str)


ma_chaine = 'MonSuperProgramme'
print(ma_chaine)

ma_chaine = ma_chaine.center(50, '*')


ma_chaine.find('Super')

# .index ne renvoie pas -1 quand il ne trouve pas la chaine recherchée... Il lève une erreur
try :
	ma_chaine.index('Super')

except ValueError :
	print('Je n\'ai pas trouvé cette chaine')



ma_chaine = 'abababababba'
print(ma_chaine)

ma_chaine = ma_chaine.replace('a', 'z', 2)