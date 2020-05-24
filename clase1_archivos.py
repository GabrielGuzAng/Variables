
datos="hola a todos 5"
#file=open("datos.txt","w")
#file.write(datos)
#file.close()

with open("datos.txt","w") as file:
	file.write(datos)

with open("datos.txt","r") as file:
	text=file.read()

print(text)