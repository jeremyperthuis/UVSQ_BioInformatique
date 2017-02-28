#	TD4_EXO2
# A partir d'un fichier
#  -> lire le fichier
#  -> concatener les sequences ADN et les afficher sous forme de codon
#  -> inserer un cadre de lecture  +1 +2 +3 pour une sequence ou -1 -2 -3 pour la complementaire
# exemple : AGTCATGCGAT
#			+1 AGT CAT GCG AT
#			+2 A GTC ATG CGA T
#			+3 AG TCA TGC GAT
# cplm :  inverse dans l'autre sens


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
print chaine
#### Affichage sous forme de codons #######
print "choix cadre :\n	+1\n	+2\n	+3\n	-1\n	-2\n	-3"
cdr = raw_input(" Saisir le cadre : ") +".txt"

	

x=len(chaine)
seqtmp=""
if "1" in cdr :
	nbr=0
if "2" in cdr :
	nbr=1
if "3" in cdr : 
	nbr=2

if "+" in cdr :
	
	i=0
	firstchar=chaine[0:nbr]	+" "
	chaine=chaine[nbr:]

	while i<x :
			seqtmp += chaine[i:i+3]+ " "
			i=i+3

	if len(chaine)%3 !=0 :
		seqtmp += chaine[i:i+3]+ " "
	seqtmp =firstchar+seqtmp	
	print seqtmp


if "-" in cdr : 
#### On calcul l'inverse #####
	i=0
	chainetmp=""
	j=len(chaine)-1

	while j>=i :
		chainetmp += chaine[j]
		j = j-1

	chaineINV=chainetmp 
		
	chaineINV=chaineINV.replace('A','t')
	chaineINV=chaineINV.replace('T','a')
	chaineINV=chaineINV.replace('G','c')
	chaineINV=chaineINV.replace('C','g')
	chaineINV=chaineINV.upper()
	chaine = chaineINV
	print chaine
	
	
	lastchar=chaine[i-nbr:]
	chaine=chaine[:i-nbr]
	i=len(chaine)
	while i>0 :
		if i-3<0 :
			seqtmp = chaine[:i] + " " +seqtmp
		
		seqtmp = chaine[i-3:i] + " " +seqtmp
		i=i-3

	seqtmp =seqtmp + lastchar	
	print seqtmp
	

