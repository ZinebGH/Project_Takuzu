from tkinter import *
import random

def couleur():
	"""Met une couleur au hasard qui est nommée dans une liste """
	palette = ['black','purple','yellow','green','magenta','red','blue','orange','pink','cyan','white','brown','navy','beige','turquoise']
	c = random.randint(0,14)
	return palette[c]


def grille(n):
	"""Génére une grille en couleur de taille n grâce """
	cpt = 0
	coul = couleur()
	for cpt in range(n+1) :
		i=480*cpt/n + 10
		Canvas.create_rectangle(10,i,490,i,outline=coul,fill='grey')
		cooul = coul
		Canvas.create_rectangle(i,10,i,490,outline=cooul,fill='grey')
		cpt += 1

def grille_4x4():
	"""Contient une liste de forme lst[i][j] pour 4 listes de 4 éléments , qui
	sera utiliser pour appliquerchaque élément de la liste dans une seule
	case par rapport à son indice"""
	global lst #Reprend la valeur initiale de lst

	Canvas.bind('<Button-3>',clicG_4x4)#Le clic gauche est spécifier à la fonction clicG_4x4
	Canvas.bind('<Button-1>',clicD_4x4)
	Canvas.bind('<Button-2>',clicR_4x4)

	Canvas.delete(ALL)
	grille(4)
	if lst is None or len(lst) != 4:
		lst=[[0,1,'',1],
			 ['','',1,''],
			 ['',0,'',0],
			 [1,'','',1]]


	wid,hei=70,70 #Coordonnées des éléments de la liste  pour les afficher au centre de chaque case en fonction de la taille de la fenetre
	for i in range(len(lst)):
		for val in lst[i] :
			Canvas.create_text(wid,hei,text=str(val),fill='white',font='Arial 20 ')
			wid+=120
		wid,hei=70,120+hei


def clic_4x4(event,cycle):
	"""Sert à valider un clic qui peut modifier la valeur de lst[i][j] (en 1,0 ou vide)
	de la grille de taille 4 avec un clic sur la case qui le représente,
	les cases où l'on peut rajouter une valeur sont sélectionner pour que
	celle qui ont déjà une valeur ne peuvent pas être modifiable par le joueur
	et donc garder la grille initiale """
	global lst
#Case vide de la premiere ligne
	if 240<event.x<360 and 10<event.y<120 :
		lst[0][2] = 0  if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides de la deuxieme ligne
	if 10<event.x<120  and 120<event.y<240:
		lst[1][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 120<event.x<240 and 120<event.y<240 :
		lst[1][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<480 and 120<event.y<240:
		lst[1][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides de la troisieme ligne
	if 10<event.x<120 and 240<event.y<360:
		lst[2][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<360 and 240<event.y<360:
		lst[2][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides de la quatrieme ligne
	if 120<event.x<240 and 360<event.y<480:
		lst[3][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<360 and 360<event.y<480:
		lst[3][2]=0 if cycle == 0 else ('' if cycle == '' else 1)

	Canvas.delete(ALL)
	grille_4x4()

def clicD_4x4(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait clic droit qui affiche un 1 dans la case cliquée de la grille de taille 4"""
	clic_4x4(event,1)

def clicG_4x4(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait clic gauche qui affiche un 0 dans la case cliquée de la grille de taille 4"""
	clic_4x4(event,0)

def clicR_4x4(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait un clic sur la roulette de la souris qui affiche un ' ' dans
	 la case cliquée de la grille de taille 4"""
	clic_4x4(event,'')

def grille_6x6():
	"""Contient une liste de forme lst[i][j] pour 6 listes de 6 éléments , qui
	sera utiliser pour appliquer chaque élément de la liste dans une seule
	case par rapport à son indice"""
	#Même fonctionnement que la grille de taille 4
	global lst
	Canvas.bind('<Button-3>',clicG_6x6)
	Canvas.bind('<Button-1>',clicD_6x6)
	Canvas.bind('<Button-2>',clicR_6x6)

	Canvas.delete(ALL)
	grille(6)

	if lst is None or len(lst)!=6 :
		lst=[[0,1,' ',' ',1,' '],
			 [' ',' ',' ',1,' ',0],
			 [0,' ',0,' ',1,' '],
			 [' ',1,' ',0,' ',1],
			 [1,' ',' ',' ',' ',' '],
			 [' ',' ',1,' ',1,' ']]

	wid,hei=50,50
	for i in range(len(lst)):
		for val in lst[i] :
			Canvas.create_text(wid,hei,text=str(val),fill='white',font='Arial 20 ')
			wid+=80
		wid,hei=50,80+hei


def clic_6x6(event,cycle):
	"""Sert à valider un clic qui peut modifier la valeur de lst[i][j] (en 1,0 ou vide)
	de la grille de taille 6 avec un clic sur la case qui le représente,
	les cases où l'on peut rajouter une valeur sont sélectionner pour que
	celle qui ont déjà une valeur ne peuvent pas être modifiable par le joueur
	et donc garder la grille initiale """
	global lst
#Cases vides premiere ligne
	if 160<event.x<240 and 10<event.y<80 :
		lst[0][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<320 and 10<event.y<80:
		lst[0][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 400<event.x<480 and 10<event.y<80:
		lst[0][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides deuxieme ligne
	if 10<event.x<80  and 80<event.y<160:
		lst[1][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 80<event.x<160 and 80<event.y<160 :
		lst[1][1] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 160<event.x<240 and 80<event.y<160:
		lst[1][2] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 320<event.x<400 and 80<event.y<160:
		lst[1][4] = 0  if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides de la troisieme ligne
	if 80<event.x<160 and 160<event.y<240:
		lst[2][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<320 and 160<event.y<240:
		lst[2][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 400<event.x<480 and 160<event.y<240:
		lst[2][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides de la quatrieme ligne
	if 10<event.x<80 and 240<event.y<320:
		lst[3][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 160<event.x<240 and 240<event.y<320:
		lst[3][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 320<event.x<400 and 240<event.y<320:
		lst[3][4] = 0  if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides cinquieme ligne
	if 80<event.x<160 and 320<event.y<400:
		lst[4][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 160<event.x<240 and 320<event.y<400:
		lst[4][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<320 and 320<event.y<400:
		lst[4][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 320<event.x<400 and 320<event.y<400:
		lst[4][4] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 400<event.x<480 and 320<event.y<400:
		lst[4][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides sixième ligne 
	if 10<event.x<80 and 400<event.y<480:
		lst[5][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 80<event.x<160 and 400<event.y<480:
		lst[5][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<320 and 400<event.y<480:
		lst[5][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 400<event.x<480 and 400<event.y<480:
		lst[5][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)

	Canvas.delete(ALL)
	grille_6x6()

def clicG_6x6(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait clic gauche qui affiche un 0 dans la case cliquée de la grille de taille 6"""
	clic_6x6(event,0)

def clicD_6x6(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait clic droit qui affiche un 1 dans la case cliquée de la grille de taille 6"""
	clic_6x6(event,1)

def clicR_6x6(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait un clic sur la roulette de la souris qui affiche un ' ' dans
	la case cliquée de la grille de taille 6"""
	clic_6x6(event,'')

def grille_8x8():
	"""Contient une liste de forme lst[i][j] pour 8 listes de 8 éléments , qui
	sera utiliser pour appliquer chaque élément de la liste dans une seule
	case par rapport à son indice"""
	global lst
	Canvas.bind('<Button-3>',clicG_8x8)
	Canvas.bind('<Button-1>',clicD_8x8)
	Canvas.bind('<Button-2>',clicR_8x8)
	Canvas.delete(ALL)
	grille(8)

	if lst is None or len(lst)!=8 :
		lst=[[0,' ',' ',' ',0,' ',' ',1],
			 [' ',' ',0,' ',' ',' ',1,' '],
			 [1,' ',1,' ',0,' ',' ',' '],
			 [' ',0,' ',1,' ',0,' ',1],
			 [' ',' ',0,' ',0,' ',' ',0],
			 [0,' ',' ',0,' ',1,0,' '],
			 [' ',1,' ',' ',' ',1,' ',0],
			 [1,' ',' ',1,0,' ',' ',' ']]


	wid,hei=40,40
	for i in range(len(lst)):
		for val in lst[i] :
			Canvas.create_text(wid,hei,text=str(val),fill='white',font='Arial 20 ')
			wid+=60
		wid,hei=40,60+hei

def clic_8x8(event,cycle):
	"""Sert à valider un clic qui peut modifier la valeur de lst[i][j] (en 1,0 ou vide)
	de la grille de taille 8 avec un clic sur la case qui le représente,
	les cases où l'on peut rajouter une valeur sont sélectionner pour que
	celle qui ont déjà une valeur ne peuvent pas être modifiable par le joueur
	et donc garder la grille initiale """
	global lst
#Cases vides premiere ligne
	if 60<event.x<120 and 10<event.y<60 :
		lst[0][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 120<event.x<180 and 10<event.y<60:
		lst[0][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 180<event.x<240 and 10<event.y<60 :
		lst[0][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 300<event.x<360 and 10<event.y<60 :
		lst[0][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<420 and 10<event.y<60 :
		lst[0][6] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides deuxieme ligne
	if 10<event.x<60  and 60<event.y<120:
		lst[1][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 60<event.x<120 and 60<event.y<120 :
		lst[1][1] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 180<event.x<240 and 60<event.y<120:
		lst[1][3] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<300 and 60<event.y<120:
		lst[1][4] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 300<event.x<360  and 60<event.y<120:
		lst[1][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 420<event.x<480  and 60<event.y<120:
		lst[1][7] = 0 if cycle == 0 else ('' if cycle == '' else 1) 

#Cases vides troisieme ligne
	if 60<event.x<120 and 120<event.y<180:
		lst[2][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 180<event.x<240 and 120<event.y<180:
		lst[2][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 300<event.x<360 and 120<event.y<180:
		lst[2][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<420 and 120<event.y<180:
		lst[2][6] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif  420<event.x<480 and 120<event.y<180:
		lst[2][7] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Case vide quatrieme ligne
	if 10<event.x<60 and 180<event.y<240:
		lst[3][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 120<event.x<180 and 180<event.y<240:
		lst[3][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<300 and 180<event.y<240:
		lst[3][4] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<420 and 180<event.y<240:
		lst[3][6] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides cinquieme ligne
	if 10<event.x<60 and 240<event.y<300:
		lst[4][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 60<event.x<120 and 240<event.y<300:
		lst[4][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 180<event.x<240 and 240<event.y<300:
		lst[4][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 300<event.x<360 and 240<event.y<300:
		lst[4][5] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<420 and 240<event.y<300:
		lst[4][6] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides sixième ligne 
	if 60<event.x<120 and 300<event.y<360:
		lst[5][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 120<event.x<180 and 300<event.y<360:
		lst[5][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<300 and 300<event.y<360:
		lst[5][4] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 420<event.x<480 and 300<event.y<360:
		lst[5][7] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides septieme ligne
	if 10<event.x<60 and 360<event.y<420 :
		lst[6][0] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 120<event.x<180 and 360<event.y<420:
		lst[6][2] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 180<event.x<240 and 360<event.y<420:
		lst[6][3] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 240<event.x<300 and 360<event.y<420:
		lst[6][4] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<420 and 360<event.y<420:
		lst[6][6] = 0 if cycle == 0 else ('' if cycle == '' else 1)

#Cases vides huitieme ligne
	if 60<event.x<120  and 420<event.y<480:
		lst[7][1] = 0 if cycle == 0 else ('' if cycle == '' else 1)
	elif 120<event.x<180 and 420<event.y<480 :
		lst[7][2] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 300<event.x<360 and 420<event.y<480:
		lst[7][5] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 360<event.x<420 and 420<event.y<480:
		lst[7][6] = 0  if cycle == 0 else ('' if cycle == '' else 1)
	elif 420<event.x<480  and 420<event.y<480:
		lst[7][7] = 0 if cycle == 0 else ('' if cycle == '' else 1)

	Canvas.delete(ALL)
	grille_8x8()

def clicG_8x8(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait clic gauche qui affiche un 0 dans la case cliquée de la grille de taille 8"""
	clic_8x8(event,0)

def clicD_8x8(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait clic droit qui affiche un 1 dans la case cliquée de la grille de taille 8"""
	clic_8x8(event,1)

def clicR_8x8(event):
	"""Lance la fonction ci-dessus mais s'execute que lorsqu'on 
	fait un clic sur la roulette de la souris qui affiche un ' ' dans
	la case cliquée de la grille de taille 0"""
	clic_8x8(event,'')

def but_du_jeu():
	"""Sert a être exécuté losque le joueur clic sur le bouton < But du jeu > pour
	ouvrir une fenêtre qui va lui expliquer le but du Takuzu"""
	mafenetre4=Tk() #Crée une nouvelle fenêtre
	mafenetre4.title('But du jeu')
	mafenetre4['bg']='grey'

	frame00 = Frame(mafenetre4,borderwidth=2,relief=GROOVE) #Zone rectangulaire qui contient le texte
	frame00.pack(side=LEFT,padx=10,pady=10)
	
	Label(frame00,text='But du jeu :''\n'"Remplir la grille avec des 0 ou des 1 de sorte qu'il y ait autant de 0 "'\n'"que de 1 sur chaque ligne et chaque colonne, qu'il n'y ait jamais plus de "'\n'"deux mêmes chiffres côte à côte et plusieurs lignes et/ou colonnes complètes identiques",fg='purple',bg='grey',justify='left').pack()

	boutonQuitter= Button(mafenetre4, text='Quitter',fg='purple',bg='grey',command=mafenetre4.destroy)
	boutonQuitter.pack(side=LEFT,padx=5,pady=5)

	mafenetre4.mainloop() #Provoque le démarrage des événements associé à la fenêtre

def regle_du_jeu():
	"""Sert a être exécuté losque le joueur clic sur le bouton < Règle du jeu > pour
	ouvrir une fenêtre qui va lui expliquer quelles sont les règles du Takuzu"""
	mafenetre3=Tk()
	mafenetre3.title('Règle du jeu')
	mafenetre3['bg']='grey'

	frame0 = Frame(mafenetre3,borderwidth=2,relief=GROOVE)
	frame0.pack(side=LEFT,padx=10,pady=10)

	Label(frame0,text='Voici les règles du Takuzu : ''\n''1 - Chaque ligne et colonnes doit contenir autant de 0 que de 1,''\n''2 - Les lignes ou colonnes identiques sont interdites,''\n'"3 - Il ne doit pas y avoir plus de deux 0 ou 1 placés l'un à coté ou en dessous de l'autre.",fg='cyan',bg='grey',justify='left').pack()

	boutonQuitter= Button(mafenetre3, text='Quitter',fg='cyan',bg='grey',command=mafenetre3.destroy)
	boutonQuitter.pack(side=LEFT,padx=5,pady=5)

	mafenetre3.mainloop()

def comment_jouer():
	"""Sert a être exécuté losque le joueur clic sur le bouton < Comment jouer > pour
	ouvrir une fenêtre qui va lui expliquer comment jouer du Takuzu"""
	mafenetre6=Tk()
	mafenetre6.title('Règle du jeu')
	mafenetre6['bg']='grey'

	frame000 = Frame(mafenetre6,borderwidth=2,relief=GROOVE)
	frame000.pack(side=LEFT,padx=10,pady=10)

	Label(frame000,text='Voici les commandes pour pourvoir jouer: ''\n''- Cliquer sur le bouton "Niveaux" et ensuite choisir un des niveaux proposer selon votre envie,''\n'"- Pour afficher un '1' dans l'une des cases choisie, faites un clic gauche dans la case,"'\n'"- Pour mettre la valeur '0', il vous suffi de faire la même méthode précédente mais cette fois ci avec le clic droit,"'\n'"- Et pour ne plus rien afficher dans la case choisi faite un clic sur la roulette de votre souris."'\n'"Bon jeu !",fg='yellow',bg='grey',justify='left').pack()

	boutonQuitter= Button(mafenetre6, text='Quitter',fg='yellow',bg='grey',command=mafenetre6.destroy)
	boutonQuitter.pack(side=LEFT,padx=5,pady=5)

	mafenetre3.mainloop()

def niveaux():
	"""Dans cette fonction, on ouvre une nouvelle fenêtre qui affiche plusieurs 
	choix de niveaux Débutant,Intermédiaire,Expert. Pour choisir un de ces niveaux 
	proposés, on clic sur le bouton < Choisir > qui va nous afficher dans la 
	fenetre principale la grille de taille spécifique au niveau choisi"""

	mafenetre2=Tk()
	mafenetre2.title('Niveaux')
	mafenetre2['bg']='grey'

	Canvas.delete(ALL)
	Canvas.create_text(250,250,text='Choisir un niveaux',font='Arial 40',fill='red')
	frame1 = Frame(mafenetre2,borderwidth=2,relief=GROOVE,bg='green')
	frame1.pack(side=LEFT,padx=10,pady=10)

	frame2 = Frame(mafenetre2,borderwidth=2,relief=GROOVE,bg='orange')
	frame2.pack(side=LEFT,padx=10,pady=10)

	frame3 = Frame(mafenetre2,borderwidth=2,relief=GROOVE,bg='red')
	frame3.pack(side=LEFT,padx=10,pady=10)


	Label(frame1,text='Débutant',bg='green').pack(padx=10,pady=10)
	boutonChoisir1=Button(frame1,text='Choisir',fg='black',bg='green',command=grille_4x4)
	boutonChoisir1.pack(side=LEFT,padx=10,pady=10)

	Label(frame2,text='Intermédiaire',bg='orange').pack(padx=10,pady=10)
	boutonChoisir2=Button(frame2,text='Choisir',fg='black',bg='orange',command=grille_6x6)
	boutonChoisir2.pack(side=LEFT,padx=10,pady=10)

	Label(frame3,text='Expert',bg='red').pack(padx=10,pady=10)
	boutonChoisir3=Button(frame3,text='Choisir',fg='black',bg='red',command=grille_8x8)
	boutonChoisir3.pack(side=LEFT,padx=10,pady=10)



	mafenetre2.mainloop()

def case_rempli(lst):
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j] == '' and i!= j :
				return False
	return True

def ligneverif(lst) :
	"""Vérifie si il n'y a pas de ligne identiques en les comparant, 
	si ce n'est pas égal on compare la première ligne à la ligne suivante"""  
	for i in range(len(lst)):
		for j in range(len(lst)):
			if lst[i] == lst[j] and i != j :
				return False
	return True

def colonneverif(lst) : 
	"""Vérifie s'il n'y a pas de colonne identique dans la liste de la grille jouée"""
	for i in range(len(lst)):
		for c in range(len(lst[i])):
			for j in range(len(lst[i])):
				for z in range(len(lst[i])):
					if lst[i][c] == lst[i][j] == lst[i][z] and c!=j and j!=z and z!=c :
						return False
	return True

def ligne(lst,x):
	"""Vérifie si il y a trois fois la même valeur (valeur qui est en paramètre) 
	d'affilée dans chaque ligne de la grille jouée, renvoie False si il y a 3 élément identique
	à la suite sinon renvoi True"""
	for i in range(len(lst)):
			for j in range(2,len(lst[i])):
				if lst[i][j] == lst[i][j-1] == lst[i][j-2] :
					return False
	return True

def colonne(lst,x):
	"""Vérifie si il n'y a pas de 0 ou de 1 à la suite dans chaque colonne de la grille jouée"""
	for i in range(len(lst)):
		for j in range(2,len(lst[i])):
				if lst[i][j] == lst[i][j-1] == lst[i][j-2] :
					return False
	return True



def verifier():
	"""Fonction qui regroupe toutes les conditions que lorsqu'elles sont vraies pour que la grille présenté
	 par le joueur soit correcte, lorque celle-ci l'est, une fenêtre s'ouvre 
	 pour dire au joueur qu'il a résolu la grille, sinon on prévient le joueur que sa grille est incorrecte par un message s'affichant dans une fenêtre """
	if (ligne(lst,0) == True) and (case_rempli(lst) == True) and (ligneverif(lst) == True) and (colonneverif(lst) == True) and (colonne(lst,0) == True) and (ligne(lst,1 ) == True) and (colonne(lst,0) == True) :
		mafenetre7=Tk()
		mafenetre7.title('Gagné')
		mafenetre7['bg']='grey'
		frame0000 = Frame(mafenetre7,borderwidth=2,relief=GROOVE)
		frame0000.pack(side=LEFT,padx=10,pady=10)
		Label(frame0000,text="Félicitation, vous avez réussi !",fg='white',bg='grey',justify='left',font='Arial 30').pack()
	else :
		mafenetre8=Tk()
		mafenetre8.title('Incorrecte')
		mafenetre8['bg']='grey'
		frame0000 = Frame(mafenetre8,borderwidth=2,relief=GROOVE)
		frame0000.pack(side=LEFT,padx=10,pady=10)
		Label(frame0000,text="Attention ta grille est incorrecte !",fg='white',bg='grey',justify='left',font='Arial 30').pack()


lst = None

mafenetre=Tk() #fenêtre principale
mafenetre.title('TAKUZU')
mafenetre['bg']='grey'

largeur = 500
hauteur = 500
Canvas = Canvas(mafenetre, width = largeur, height = hauteur, bg='grey')
Canvas.create_text(250,250,text='TAKUZU',fill='red',font='Arial 80')
Canvas.pack(padx = 5, pady = 5) #Provoque l'affichage du composant définit au dessus

Labelbis=Label(mafenetre,text='Menu',fg='black',bg='grey')
Labelbis.pack()

boutonButduJeu = Button(mafenetre,text='But du jeu',fg='black',bg='grey',command=but_du_jeu)#Création du bouton
boutonButduJeu.pack(side=LEFT,padx=5,pady=5)

boutonRegleduJeu = Button(mafenetre,text='Règle du jeu',fg='black',bg='grey',command=regle_du_jeu)
boutonRegleduJeu.pack(side=LEFT,padx=5,pady=5)

boutonNiveau = Button(mafenetre,text='Niveaux',fg='black',bg='grey',command=niveaux)
boutonNiveau.pack(side=LEFT,padx=5,pady=5)

boutonCommentJouer= Button(mafenetre,text='Comment jouer ?',fg='black',bg='grey',command=comment_jouer)
boutonCommentJouer.pack(side=LEFT,padx=5,pady=5)

boutonVerifier = Button(mafenetre,text='Vérifier grille',fg='black',bg='grey',command=verifier)
boutonVerifier.pack(side=LEFT,padx=5,pady=5)

boutonQuitter= Button(mafenetre, text='Quitter',bg='grey',command=mafenetre.destroy)
boutonQuitter.pack(side=LEFT,padx=5,pady=5)




mafenetre.mainloop()


