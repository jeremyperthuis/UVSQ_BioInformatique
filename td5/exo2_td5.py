# TD5 EXO2
# Meme chose sans lutiliser la fonction find

nom = raw_input(" Saisir le chemin du fichier : ") +".txt"
f=open(nom,'r')

#### Concatenation des lignes du fichier ##### 

chaine=""
chainetmp=""
cpt=0
while 1 :
	chainetmp=f.readline()
	if chainetmp=='' :
		break	
	else :
		chaine += chainetmp[:len(chainetmp)]
		cpt+=1
f.close()
chaine = chaine.replace('\n','')
chaine = chaine.upper()



motif = raw_input(" Saisir un motif a rechercher : ")
if not motif in chaine  : 
	print "Pas de correspondance trouvee"
else :
	nom2 = raw_input("Saisissez le fichier pour sauver les donnees : ") + ".txt"
	f1=open(nom2,'w')
	res=0
	i=0
	while i < len(chaine)-1 :
		if chaine[i:i+len(motif)] == motif :
			res=i+1
			print res
			f1.write(str(res)+"\n")
			i +=len(motif)

		else:
			i+=1
	
	
	f1.close()		
