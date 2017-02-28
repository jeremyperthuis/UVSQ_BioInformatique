#	TD4_EXO3
# On ouvre un fichier : 1 sequence par ligne
# 	-> on affiche la plus grande sequence et son numero de ligne

nom = raw_input(" Saisir le chemin du fichier : ") +".txt"
f=open(nom,'r')

#### Concatenation des lignes du fichier ##### 

ligne =f.readline()
ligne = ligne.replace('\n','')
x=len(ligne)-1
cpt=1
while ligne != "" :
	if x < len(ligne) :
		x = len(ligne)
		z=ligne
		tcpt =cpt
	ligne = f.readline()
	ligne = ligne.replace('\n','')
	cpt +=1

print "la plus grande sequence : " +z
print "(ligne "+str(tcpt) +")"
