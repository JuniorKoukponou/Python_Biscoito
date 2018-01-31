##----------------------------------------------------
# La Programmation Orrientée Objet (POO) avec Python
##----------------------------------------------------

# Notion de paradigme

# Classe 						: plan de conception, genre (ex : Humain)
# Objet 						: c'est une instance de classe, quelque chose qui est du genre de cette Classe (ex : William est un Humain)


# Attribut 						: Variable de la classe, caractéristique d'une classe et n'est pas valide en dehors de celle-ci, (ex prenom, sexe, ...)
# Propriété 					: (un Attribut est une Propriété) moyen de manipuler les attributs (définition pour Python) (ex lecture seule, accès non autorisé en dehors de la classe, etc.)


# Méthode			    		: fonction d'une classe (ex : manger, parler, dormir, marcher, mourir)
# Méthode de classe 			: fonction d'une classe (explication à venir plus tard !!!!)
# Méthode (de classe) statique. : fonction d'une classe, mais indépendante de celle-ci, pratique dans les classes utilitaires. Pas besoin d'instancier une classe pour l'utiliser


# Héritage 						: classe Fille (Léopard, Chat) qui hérite d'une classe Mère (Animal). On dit que Fille est une sorte de Mère
#								: classe Chat hérite de la classe Animal (chat est une sorte de Animal)


# ----------- Interets du POO ------------ # 
#								: Mieux organiser son code, d'où la POO est un paradigme
#								: Réutilisation via l'instanciation
#								: Code plus facile à maintenir
#


nom = 'Vanessa'

texte = "Bienvenue {}".format(nom)
print(texte)

# texte est un objet de classe str
# format est une méthode de la classe str