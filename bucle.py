

import random

alumnos = []

for i in range(30):
	notas=[random.randint(1,10) for i in range(3)] ##genero un vector de 3 notas random
	alumnos.append(notas) ## agrego el vector a alumnos

print("\n\n",alumnos,"\n\n")

promedios=[]

for i in range(30):
	notas=alumnos[i]
	suma=0
	for nota in notas:
		suma=suma+nota
	promedios.append(suma/3)
print ("\n\n",promedios)