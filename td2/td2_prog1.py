#td2 prog1
chaine1 = raw_input("inserer une premiere chaine de caractere : ")
n = input("choisir un nombre : ")

if n<len(chaine1) and n!=0 :
	print chaine1[:n]
elif n==0 :
	print "ne pas choisir 0 "


