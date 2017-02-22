# Ouvrir un fichier contenant une sequence par ligne
# Calculer le longueur moyenne des sequences et le nombre de sequences
# Sauvegarder dans un fichier


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
chaine = chaine.replace('\n','')
##############################################

avr = "la longueur moyenne d'une sequence : " + str(round(len(chaine)/cpt*1.0,2)) + " caracteres"
nbseq = "le fichier contient "+ str(cpt) +" sequences."
print avr
print nbseq

print " Sauver la sequence convertie ?  y/n"
resp1 = raw_input()
if resp1 == 'y' : 
	nom2 = raw_input(" Saisissez le fichier pour sauver les donnees : ") + ".txt"
	f1=open(nom2,'w')
	f1.write(avr)
	f1.write("\n")
	f1.write(nbseq)
	print " Donnees sauvegardees !\n"
elif resp1 =='n':
	print "Donnees non sauvegardees !\n"

