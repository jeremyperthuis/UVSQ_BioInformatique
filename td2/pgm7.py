sq1 = raw_input("inserer une sequence ADN :")
n=0

sq2 = ""

while n<= len(sq1) :
	if sq1[n] =='A' or sq1[n] =='T' or sq1[n] =='G' or sq1[n] =='C' :
		print sq1[n]
	else :
		print "IL y'a erreur sur le lettre",sq1[n],"a la position :",n+1
	n=n+1
