#	TD4_EXO1
# A partir d'un fichier
#  -> lire le fichier
#  -> concatener les sequences ADN et les afficher sous forme de codon
#  exemple : ACGTACGTA  ->  ACG TAC GTA


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

#### Affichage sous forme de codons #######
i=0
x=len(chaine)
seqtmp=""
while i<x :
	seqtmp += chaine[i:i+3]+ " "
	i=i+3

if len(chaine)%3 !=0 :
	seqtmp += chaine[i:i+3]+ " "
	
print seqtmp


	
