import os

def getStarted():
	os.system("clear")

	print("Bienvenue sur le gestionnaire du jeu serieux 'Cyber Dem'")
	print("Quelle activité voulez-vous lancer ?")

	chosen_dir=[]

	for root, dirs, filenames in os.walk("."):
		print(dirs)
		for id,dir in enumerate(dirs[::-1]) :
			chosen_dir.append(dir)
			print(id," : ",dir)
		break
	choice=int(input("Votre choix (entier seulement) : "))


	confirm=input(f"Etes-vous sûr de vouloir lancer l'activité {chosen_dir[choice]} ? (O/N) ")
	if confirm=="O" or confirm =="o":
		os.system(f"./{chosen_dir[choice]}/main.sh")
	else:
		getStarted()
getStarted()
