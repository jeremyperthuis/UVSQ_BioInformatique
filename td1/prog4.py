#prog4 avec in 

chaine1=raw_input('saisir une chaine de caractere : ')
chaine2=raw_input('saisir une chaine de caractere : ')
chaine1.upper()
chaine2.upper()
if chaine2 in chaine1 :
	print 'OUI'

else : 
	 
	print 'NON'

#prog4 avec count

chaine1=raw_input('saisir une chaine de caractere : ')
chaine2=raw_input('saisir une chaine de caractere : ')
chaine1.upper()
chaine2.upper()
if chaine1.count(chaine2) :
	print 'OUI'

else : 
	 
	print 'NON'
