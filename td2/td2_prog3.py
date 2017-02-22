ch1 = raw_input("inserer une chaine de caractere :")
print "voulez vous lire les n premiers ou les n derniers caracteres"
ch2 = raw_input("premiers carac: taper p / derniers carac: taper d")

n = input("choisir un nombre de lettre a afficher :")

if ch2[:1]!='p' or ch2[:1]!='d':
	print "nous avons pas compris votre choix"

elif ch2[:1]=='d':
	if n<len(ch1) and n!=0 :
	print ch1[len(ch1)-n:]
elif n==0 :
	print "ne pas choisir 0 "

elif ch2[:1]=='p' :
	if n<len(ch1) and n!=0 :
	print ch1[:n]
elif n==0 :
	print "ne pas choisir 0 "
	
