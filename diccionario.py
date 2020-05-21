
import random
mi_dic={"nombre":"Gabo", "edad":26, "dni":18865342}

#print("\n\n",mi_dic["nombre"],"\n\n")

#print("\n\n",mi_dic.get("nombre"),"\n\n")

mi_dic["dni"]=777




mi_dic["surname"]="perez"


	#print("\n\n",key, value)
print("\n\n",mi_dic)

noms=["carla","marta","jonas"]

alumnos={}
for nombre in noms:
	notas=[random.randint(1,10) for i in range(3)]
	#alumnos.append(notas) caso lista
	alumnos[nombre]=notas	
print("\n\n\n", alumnos)

promedios={}
for nombre in noms:
	notas=alumnos[nombre]
	suma=0
	for nota in notas:
		suma=suma+nota
	suma=suma/3
	promedios[nombre]=suma	
print("\n\n\n", promedios)