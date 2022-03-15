import sys

#This script needs two args : 
#   -first one for the CA state,range : [1-4]  
#   -second one for the cusumer grade, range : [1-4]

args=sys.argv

if(len(args)==3):
    f=open("/home/user/Documents/Scenarii_Projet_MiniEntreprise/config/conf.txt","w")
    newfile="'state_ca:"+str(args[1])+"\nstate_avis:"+str(args[2])
    f.write(newfile)
    f.close()
else:
    print("Pour exécuter ce script veuillez fournir deux arguments, le premier pour l'état du chiffre d'affaire, le deuxième pour l'état des avis")