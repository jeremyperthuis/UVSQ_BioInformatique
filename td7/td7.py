# TD7 
# On demande a l'utilisateur 2 fichiers contenant chacun 1 codon
# Les codons sont affcihé sous forme d'une matrice de correspondance dans un fichier externe
# On demande a l'utilisateur un nombrede groupement pour eliminer le bruit parasite de correspondance
# 	afin de mettre en valeur les diagonales
# Penser a modifier le chemin des fichier si l arborescence differe.

nom ="/home/perthuis/Programmation/Python/td7/" + raw_input(" Saisir le nom du fichier : ") +".txt"
f=open(nom,'r')

nom2 ="/home/perthuis/Programmation/Python/td7/" + raw_input(" Saisir le nom du fichier : ") +".txt"
p=open(nom2,'r')



chaine1=f.readline()
chaine2=p.readline()

nom3 = "/home/perthuis/Programmation/Python/td7/" + raw_input(" Saisissez un nom ou sauvegarder : ") + ".txt"
f1=open(nom3,'w')

groupement = input("saisir un groupement : ")
f1.write("groupement de "+ str(groupement)+"\n")

i=0
j=0
tmp1=" "
tmp2="  "+chaine1+"\n"
f1.write(tmp2)
print "chaine1"+str(len(chaine1))
print "chaine2"+str(len(chaine2))
while i < len(chaine2)-groupement :
	j=0
	while j < len(chaine1)-groupement :
		
		if chaine1[j:j+groupement] == chaine2[i:i+groupement] :
			tmp1= tmp1 + "X"
		
		else :
			tmp1 = tmp1 + " "
		j+=1
		
	tmp2=""		
	tmp2= chaine2[i]+tmp1+"\n"
	f1.write(tmp2)
	tmp1=" "
	
	i+=1;



	
