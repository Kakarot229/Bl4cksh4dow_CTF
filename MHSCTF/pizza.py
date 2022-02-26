import sys # sys.stdin.readline permet de récupérer uniquement l'entree standard
lines=[]
for i in range(7):
	lines.append(sys.stdin.readline())# lines a la fin va contenir un l'ensemble des 7 entrees (lignes) de l'utilisateur


# Pour chaque entree par exemple (TATTM)
for elt in lines:	
	price=15.0
	if 'T' in elt:
    		price+=1.5
	if 'O' in elt:
    		price+=1.25
	if 'P' in elt:
    		price+=3.5
	if 'M' in elt:
    		price+=3.75
	if 'A' in elt:
    		price+=0.4
    		
	if price > 20.0 :
    		price=round(price-(price*0.05),2)
 
	liste=str(price).split(".")
	if len(liste[-1])==1:
    		print(str(price)+"0")# Ici on formate pour que ça mette 2.50 au lieu de 2.5  	
	else:
    		print(price)  

