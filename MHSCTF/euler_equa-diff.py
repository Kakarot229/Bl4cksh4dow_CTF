
"""
import sys
limit=int(sys.stdin.readline())
entrees=[]
for i in range(limit):
	entrees.append(sys.stdin.readline().rstrip("\n"))
for entree in entrees:
	entree=entree.split()
	given_h=float(entree[0])
	given_x=float(entree[1])

	x,y=5.0,2.0

	while True:
		k=x**2 - 6*y**2
		y = y + given_h*k
		x=round(x+given_h,1)
		if x==given_x:
			y_to_print=round(y,1)
			print(y_to_print)
			break
"""	
"""
import numpy

    
def pas_euler(h,Yn):
    deriv = -6*(Yn[1]**2)+Yn[0]**2
    return Yn[1]+h*deriv
    
     
    
def euler(Yi,T,h):
    Y0 = Yi
    liste_y = [Y0[1]]
    liste_t = [Y0[0]]
    t=5.0
    while t<10:
        Y = pas_euler(h,Y0)
        print(Y)
        t += h
        liste_y.append(Y)
        liste_t.append(t)
        Y0=[t,Y]
    return (numpy.array(liste_t),numpy.array(liste_y))


T = 100.0
h = 0.9
Yi = [5.0,2.0]
(t,tab_y) = euler(Yi,T,h)
print("x:",t,"\ny:",tab_y)
"""

import sys
limit=int(sys.stdin.readline())
entrees=[]
for i in range(limit):
	entrees.append(sys.stdin.readline().rstrip("\n"))
for entree in entrees:
	entree=entree.split()
	given_h=float(entree[0])
	given_x=float(entree[1])
	
	Y0 = 2.0
	x=5.0
	while True:
		Y = Y0 + (x**2 - 6*(Y0**2))*given_h
		x = x+given_h
		Y0=Y
		if round(x,1)==given_x:
			print('%.1f'% (round(Y,1)))
			break

