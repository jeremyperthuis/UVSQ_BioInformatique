sq1 = raw_input("inserer une sequence ADN :")
i=0

n=len(sq1)-1
x=0

while i<n :
	if sq1[i]==sq1[n] :
		x=x+1
	i=i+1
	
if x == (len(sq1)-1)/2 :
	print "cette sequence est un palindrome"

else :
	print"cette sequence n'est pas un palindrome"
