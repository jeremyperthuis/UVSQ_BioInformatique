# TD5 EXO3
# Donner le % de similarité entre 2 sequences de taille


chaine1 = raw_input(" Saisir une premiere sequence : ")
chaine2 = raw_input(" Saisir une seconde sequence : ")

if  not len(chaine1) == len(chaine2) :
	print "les deux sequences ne font pas la meme taille"

else :
	cpt=0
	i=0
	while i < len(chaine1)-1 :
		if chaine1[i] == chaine2[i] :
			i+=1

		if not chaine1[i] == chaine2[i]:
			cpt+=1
			i+=1
	

if cpt==0 :
	print "les sequences sont identiques"

else :
	res = round((cpt*100.0)/len(chaine1),2)
	print " les sequences sont a " +str(res) +"% identiques"	
