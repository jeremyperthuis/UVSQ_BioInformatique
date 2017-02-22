# Determinisation de sequences palindromiques
# Ce programme verifie si les 2 brins forment une sequence palindromique
# exemple  :	GAATTC
#				CTTAAG

chaine1 = raw_input("inserer le 1er brin de la sequence ADN : ")
chaine2 = raw_input("inserer le 2eme brin de la sequence ADN : ")

if len(chaine1) != len(chaine2) : 
	print "ERREUR les deux brins sont de tailles differentes"

# on inverse la chaine 2
else : 
	i=0
	chainetmp=""
	j=len(chaine2)-1

	while j>=i :
		chainetmp += chaine2[j]
		j = j-1

	chaine2=chainetmp
		#on compare les 2 chaines
	if chaine1 in chaine2 :
		print "les 2 brins sont des palindromes"
	
	else : 
		print "les 2 brins ne sont pas des palindromes"
	

	

