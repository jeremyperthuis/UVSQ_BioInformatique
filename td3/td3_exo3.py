# Demande le nom d'un fichier
# Ouvrir ce fichier pour afficher le % de A de toute la sequence
# Sauvegarder ce resultat plus la longueur de la sequence dans un fichier
#	specifie par l'utilisateur avec l'extension .txt automatique

nom = raw_input("Saisir le chemin du fichier : ") +".txt"
f=open(nom,'r')

chaine=""
chainetmp=""

while 1 :
	
	chainetmp=f.readline()
	
	if chainetmp=='' :
		break
		
	else :
		chaine += chainetmp[:len(chainetmp)]
f.close()
chaine = chaine.replace('\n','')

per1 = round(chaine.count('A')*1.0/len(chaine)*100,2)
chaine2 =  'pourcentage de A : ' + str(per1)
print chaine2

nom2 = raw_input("Saisissez le fichier pour sauver les donnees : ") + ".txt"
f1=open(nom2,'w')
f1.write(chaine2)
print "donnees sauvegardees !"






