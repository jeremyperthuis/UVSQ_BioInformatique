ch1 = raw_input("inserer une chaine de caractere :")
l = input("combien de quelles lettres voulez vous extraire ?:")
n = input("choisir un nombre de lettre a lire :")

tmp = len(ch1)-l+1
if n<=tmp :
	 if n!=0 :
		print ch1[l-1:l+n-1]
	 elif n==0 :
		print "choisir un nombre different de 0"

else :
	print ("fausse position de depart")
