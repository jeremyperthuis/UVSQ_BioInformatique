# TD5 EXO4
# Donner une marge de similarité 

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
###################################################



motif = raw_input(" Saisir un motif a rechercher : ")
marge = input("Saisir un pourcentage minimal de similarite : ")
while marge<=50 :
	print "erreur le pourcentage minimal est de 50 %"
	marge = input("Saisir un pourcentage minimal de similarite : ")

res=0
i=0

while i < len(chaine)-1 :
	j=0
	while j < len(motif)-1 :
		if chaine[j] == motif[j] :
			j+=1

		if not chaine[j] == motif[j]:
			cpt+=1
			j+=1
			
	res = round((cpt*100.0)/len(motif),2)
			
	if chaine[i:i+len(motif)] == motif : # si les 2 chaine sont egales
		res=i+1
		print res
		i +=len(motif)

	if chaine[i:i+len(motif)] != motif: #si les 2 chaines ne sont pas egales
		if res>=marge :					# mais si la similarite est superieur a la marge minimale
			res=i+1
			print res
			i +=len(motif)
		
		else :	
			i+=1

