
num=float(input("\n Ingrese número para adherir al promedio. O ingrese 0 para salir\n"))
cant=0
prom=0
while(num!=0):
	if((num>0) and (num<=10)):
		cant=cant+1
		prom=prom+num
	else:
		print("\n El número ingresado se encuentra fuera del rango aceptable\n")
	num=float(input("\n Ingrese número para adherir al promedio. O ingrese 0 para salir\n"))
	
prom_final=prom/cant
if(prom>=6):
	print("\n Pasa con %.2f y cant %i \n"%(prom_final,cant))
else:
	print("\n No pasa, tiene promedio de %.2f y cant \n"%(prom_final,cant))
print("\n version 2\n")
