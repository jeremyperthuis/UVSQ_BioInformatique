# TD5 EXO1
# Afficher la premiere occurrence si elle existe (sa position)
# Afficher toute les positions
# Enregistrer dans un fichier 


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


i=0
motif = raw_input(" Saisir un motif a rechercher : ")
if chaine.find(motif) ==-1 : 
	print "Pas de correspondance trouvee"
else :
	nom2 = raw_input("Saisissez le fichier pour sauver les donnees : ") + ".txt"
	f1=open(nom2,'w')
	
	while i < len(chaine) :
		regno=chaine.find(motif,i) +1
		if regno :
			print regno
			f1.write(str(regno)+"\n")
			i=regno
		else :
			i= len(chaine)+1
			f1.close()

			
			
			
			
