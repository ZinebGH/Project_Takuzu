from upemtk import *

#Grilles de taille nxn , vides
G4x4=[]
G6x6=[]
G8x8=[]


def LOADFILE(fileName):
	"""fonction qui charge un puzzle depuis un fichier .dat
	situé dans le même document """
	text_file = open(fileName, "r") #ouvrir(nom fichier, r=reading, ouvrir le fichier pour le lire)
	G = []
	line = ''
	while line!=['']:
		line = text_file.readline().replace('\n','').split(',')
		if line!=['']:
			G.append(line)
	return G

def affiche(lst):
	"""on utilise cette fonction dans LOADFILE_choix dans le but d'afficher 
	les différentes listes correspondant aux différents puzzles"""
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			print(lst[i][j][0], end="")
		print("")


def LOADFILE_choix(choix):
	"""selon le choix de l'utilisateur
	(2 pour la grille 4x4,3pour la grille 6x6,4 pour la grille 8x8)
	on charge la grille correspondante grâce à la fonction affiche(lst)"""
	global G4x4 #global permet de reprendre la valeur initiale
	global G6x6
	global G8x8
	if choix == 2 :
		G4x4=LOADFILE('4x4.dat')
		affiche(G4x4)
	elif choix == 3 :
		G6x6=LOADFILE('6x6.dat')
		affiche(G6x6)
	elif choix == 4 :
		G8x8=LOADFILE('8x8.dat')
		affiche(G8x8)
	print ('')

 

def MAJ(i,j,n,choix) :
	"""on définit les coordonnées des différents éléments des listes puis
	on affiche les puzzle sous forme de listes de liste grâce à la fonction 
	‘affiche’ , Par exemple si on choisit le niveau débutant (choix==2), 
	alors la variable n sera affichée aux coordonnées[i][j] 
	dans le puzzle de taille 4*4."""
	global G4x4
	global G6x6
	global G8x8
	if choix==2 and i>=0 and i<4 and j>=0 and j<4:
		if (G4x4[i][j][1]):
			G4x4[i][j]=(n, True)
		else:
			print("Manoeuvre interdite, veuillez recommencer")
			#il faut que la valeur ne soit pas bloquée par le tuple pour pouvoir la changer.
		affiche(G4x4)
	elif choix==3 and i>=0 and i<6 and j>=0 and j<6:
		G6x6[i][j]=n
		affiche(G6x6)
	elif choix==4 and i>=0 and i<8 and j>=0 and j<8:
		G8x8[i][j]=n
		affiche(G8x8)

 
def titre():
	"""affiche le titre 'TAKUZU'."""
	print('                                        Takuzu ')


def affiche_menu() :
	"""affiche le menu, les différents choix disponibles pour l'utilisateur"""
	print('')
	print('Table de choix : ')
	print('Choix 0 : Règle du jeu ')
	print('Choix 1 : But du jeu ')
	print('Choix 2 : Niveau Débutant ')
	print('Choix 3 : Niveau Intermédiare ')
	print('Choix 4 : Niveau Expert ')
	print('Choix q : Quitter ')

 

def choix_pris(choix) :
	"""Pour chaque choix effectué par l'utilisateur on met en marche qqchose de différent
	ex
	choix=0 on affiche les règles
	choix==1 le but du jeu
	choix==2 on charge le puzzle 4x4
	etc"""
	if choix == 0 :
		regle_du_jeu()
	elif choix == 1 :
		but_du_jeu()
	elif choix == 2 :
		G4x4=LOADFILE('4x4.dat')
	elif choix == 3 :
		G6x6=LOADFILE('6x6.dat')
	elif choix == 4 :
		G8x8=LOADFILE('8x8.dat')


def regle_du_jeu() :
	"""affiche les règles du jeu seulement à la demande de l'utilisateur"""
	print('')
	print('Voici les règles du Takuzu : ')
	print('1 - Chaque ligne et colonnes doit contenir autant de 0 que de 1,')
	print('2 - Les lignes ou colonnes identiques sont interdites,')
	print("3 - Il ne doit pas y avoir plus de deux 0 ou 1 placés l'un à  côté ou en dessous de l'autre.")

 

def but_du_jeu() :
	"""affiche le but du jeu seulement à la demande de l'utilisateur"""
	print('')
	print('But du jeu :')
	print("Remplir la grille avec des 0 ou des 1 de sorte qu'il y ait autant de 0 ")
	print("que de 1 sur chaque ligne et chaque colonne, qu'il n'y ait jamais plus de ")
	print("deux mêmes chiffres côte à côte et plusieurs lignes et/ou colonnes ")
	print("complètes identiques")

def verifier():
	"""permet de comparer le puzzle rempli par l'utilisateur 
	à la solution de ce dernier, tant qu'ils ne sont pas ls mêmes, 
	il continue sans indication dès que le puzzle de l'utilisateur 
	correspond à la solution, un message s'affiche"""
	G4x4R=LOADFILE('4x4R.dat')
	G6x6R=LOADFILE('6x6R.dat')
	G8x8R=LOADFILE('8x8R.dat')
	if compare_listes(G4x4R,G4x4):#on utilise la fonction compare_listes(lst1,lst2) pour comparer 2 listes 
		print("Vous avez réussi")
	elif compare_listes(G6x6R,G6x6) :
		print("Vous avez réussi")
	elif compare_listes(G8x8R,G8x8):
		print("Vous avez réussi")
		return False
	return True

def compare_listes(lst1,lst2):
	"""on verifie que les 2 listes ont la même longueur
	 puis si les 2 lisstes ne sont pas identiques """
	if (len(lst1) != len(lst2)):
		return False
	for i in range(len(lst1)):
		for j in range(len(lst1[i])):
			if lst1[i][j]!=lst2[i][j] :
				return False
	return True

def bloquer(g):
	"""En utilisant des tuples on bloque les 
	valeurs présentes dans l'énoncé du puzzle"""
	for i in range(len(g)):
		for j in range (len(g[i])) :
			 if g[i][j] == '-':
				 g[i][j]=('-',True)
			 else :
				 g[i][j]=(g[i][j],False)

def main() :
	titre()
	affiche_menu()
	choix = input('Quel choix désirez vous (0-4 / q) ? ' )

	while choix != 'q':
		choix=int(choix)
		if choix == 0:
			regle_du_jeu()
			affiche_menu()
			choix = input('Quel choix désirez vous (0-4 / q) ? ' )
		elif choix==1:
			but_du_jeu()
			affiche_menu()
			choix = input('Quel choix désirez vous (0-4 / q) ? ' )
		elif choix == 2 or choix == 3 or choix == 4 :
			LOADFILE_choix(choix)
			if choix==2 :
				bloquer(G4x4)
			elif choix==3 :
				bloquer(G6x6)
			elif choix==4:
				bloquer(G8x8)
			while choix!='q' :
				while verifier() :
					i = input('Choix de la ligne n° : ')
					if i=="q":
						choix="q"
					else:
						i=int(i)
					if choix!='q':
						j = input('Choix de la colonne n° : ')
						if j=='q':
							choix='q'
						else:
							j=int(j)
					if choix!='q':
						n = int(input('Y mettre 0 ou 1 ? : '))
						while n!=1 and n!=0 :
							n = int(input('Y mettre 0 ou 1 ? : '))
					if choix!='q':
						MAJ(i,j,n,choix)
	return 0


if __name__ == '__main__':
	main()
