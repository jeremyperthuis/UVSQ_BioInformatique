sq1 = raw_input("inserer une sequence ADN :")
sq2 = ""
n=0
while n<len(sq1) :
	if sq1[n]=='a':
		sq2=sq2+ "t"
	elif sq1[n]=='t' :
		sq2=sq2+ "a"
	elif sq1[n]=='g':
		sq2=sq2+ "c"
	elif sq1[n]=='c' :
		sq2=sq2+ "g"
	elif sq1[n:n]=='t':
		sq2=sq2+ "a"
	n=n+1
	
sq3 = ""
n = len(sq2)-1
i=0

while n>=0 :
	tmp=sq2[n]
	sq3=sq3+tmp		#incrementation sq3+tmp
	n=n-1
print "l'inverse complementaire de la sequence ADN est :"+sq3
	
