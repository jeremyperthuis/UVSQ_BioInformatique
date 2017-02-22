# Ouvre un fichier puis lis ligne par ligne
# 	et les concatene en une seule chaine de caractere

f=open("test.txt",'r')

chaine=""
chainetmp=""

while 1 :
	
	chainetmp=f.readline()
	
	if chainetmp=='' :		# si c'est une ligne vide c'est la fin du fichier
		break
		
	else :
		chaine += chainetmp[:len(chainetmp)]

chaine = chaine.replace('\n','') # remplace les retours a la ligne par un caractere nul
print chaine


	
