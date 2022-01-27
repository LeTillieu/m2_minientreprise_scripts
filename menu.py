import os

def getStarted():
	os.system("clear")

	print("Bienvenue sur le gestionnaire du jeu serieux 'Cyber Dem'")
	print("Quelle activité voulez-vous lancer ?")


	for root, dirs, filenames in os.walk("./activite"):
	
		filenames=list(filter(lambda x: x.split('.')[1]=='json',filenames))
		
		for id,files in enumerate(filenames) :
			print(id," : ",files)
		break
		
	choice=int(input("Votre choix (entier seulement) : "))

	confirm=input(f"Etes-vous sûr de vouloir lancer l'activité {files[choice]} ? (O/N) ")
	
	if confirm=="O" or confirm =="o":
	
		os.system(f"python /activite/parse.py {files[choice]} ")
		
	else:
		getStarted()
		
getStarted()
