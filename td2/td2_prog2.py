ch1 = raw_input("inserer une premiere chaine de caractere :")
n = input("choisir un nombre :")

if n<len(ch1) and n!=0 :
	print ch1[len(ch1)-n:]
elif n==0 :
	print "ne pas choisir 0 "

