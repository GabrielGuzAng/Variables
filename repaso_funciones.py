

def my_func(nombre,apellido):
	print(f" \n\n me llamo {nombre} de apellido {apellido} \n")

my_func("gabo","guz")

def suma(a,b):
	res=a+b
	return "\n el resultado es ", res," \n fin\n"

tipo1,resultado,tipo2=suma(8,9)
#print(tipo1)
#print(resultado)
#print(tipo2)


import random

def suma_dados(): #retorno un vector
	for j in range(6):
		dados=[random.randint(1,6) for i in range(4)] ##genero un vector de 3 notas random
		dados.sort()
		max_dados=dados[1:]
		stats.append(sum(max_dados))
	return stats


def get_stats(): #retorno los stats del juego, el código es mas eficiente
	dados=[random.randint(1,6) for i in range(4)] ##genero un vector de 3 notas random
	dados.sort()
	max_dados=dados[1:]
	return sum(max_dados)

stats={
	"str": get_stats(),
	"des": get_stats(),
	"int": get_stats(),
	"wis": get_stats(),
	"con": get_stats(),
}

print(stats)
		

