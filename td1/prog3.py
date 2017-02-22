#prog3
adn=raw_input('Saisir une sequence ADN : ')
adn=adn.upper()
print adn
per1 = round(adn.count('A')*1.0/len(adn)*100,2)
per2 = round(adn.count('T')*1.0/len(adn)*100,2)
per3 = round(adn.count('G')*1.0/len(adn)*100,2)
per4 = round(adn.count('C')*1.0/len(adn)*100,2)

print 'pourcentage de A : ',per1
print 'pourcentage de T : ',per2
print 'pourcentage de G : ',per3
print 'pourcentage de C : ',per4

print 'pourcentage des non ATGC', 100-(per1+per2+per3+per4)
