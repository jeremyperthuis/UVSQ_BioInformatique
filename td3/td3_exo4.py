# Saisir un nom de fichier contenant une sequence
# Proposer plusieurs choix possibles : 
# 		1 -> Transcrire la sequence ADN en ARN
#		2 -> Transcrire la sequence ADN vers son inverse complementaire
#		3 -> Arret du programme sinon le programme boucle
# Sauvegarder dans un fichier les resultats

nom = raw_input(" Saisir le chemin du fichier : ") +".txt"
f=open(nom,'r')

while 1 : 
#### Concatenation des lignes du fichier ##### 

	chaine=""
	chainetmp=""

	while 1 :
		chainetmp=f.readline()
		if chainetmp=='' :
			break	
		else :
			chaine += chainetmp[:len(chainetmp)]
	chaine = chaine.replace('\n','')
	
##############################################
	

	print"   **MENU**"
	print "1 : Transcrire la sequence ADN en ARN"
	print "2 : Transcrire la sequence ADN vers son inverse complementaire"
	print "3 : Arret du programme"

	choix = input("Saisissez un choix : ")



	if choix > 3 : 
		print "ERREUR CHOIX"

	if choix == 1 : 
		chaineARN = chaine.replace('T','U')
		print chaineARN
		print " La sequence a ete convertie avec succes !"
		print " Sauver la sequence convertie ?  y/n"
		resp1 = raw_input()
		if resp1 == 'y' : 
			nom2 = raw_input(" Saisissez le fichier pour sauver les donnees : ") + ".txt"
			f1=open(nom2,'w')
			f1.write(chaineARN)
			print " Donnees sauvegardees !\n"
		elif resp1 =='n':
			print "Donnees non sauvegardees !\n"

	if choix == 2 :

	#Inversion de la sequence#
	
		i=0
		chainetmp=""
		j=len(chaine)-1

		while j>=i :
			chainetmp += chaine[j]
			j = j-1

		chaineINV=chainetmp 
	##########################
		chaineINV=chaineINV.replace('A','t')
		chaineINV=chaineINV.replace('T','a')
		chaineINV=chaineINV.replace('G','c')
		chaineINV=chaineINV.replace('C','g')
		chaineINV=chaineINV.upper()
		print chaineINV
		print " La sequence a ete convertie avec succes !"
		print " Sauver la sequence convertie ?  y/n"
		resp2 = raw_input()
		if resp2 == 'y' : 
			nom3 = raw_input(" Saisissez le fichier pour sauver les donnees : ") + ".txt"
			f2=open(nom3,'w')
			f2.write(chaineINV)
			print " Donnees sauvegardees !\n"
		elif resp2 =='n':
			print "Donnees non sauvegardees !\n"

	if choix == 3 : 
		print "FIN DU PROGRAMME"
		f.close()
		break
