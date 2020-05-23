

def change_var(b):
	b=b+5
	print(b)
	return b

a=20
print(a)
change_var(a)  #no modifico mi variable original
print(a)

print("\n\n")
################################################################################


def change_var1(b):
	b.append(5)
	print(b)


a=[20]
print(a)
change_var1(a)  #modifico mi variable original
print(a)

################################################################################


def change_var2(b,l=[]):
	l.append(b)
	return l

lst=change_var2(2)
lst1=change_var2(7)
lst2=change_var2(3)

print("\n\n",lst2) # se modifica la lista de mi función, no crea 2 listas distintas

##########################################################################



def argumentos(*dock):
	print(dock)

def kwargumentos(**kwdock):
	print(kwdock)

argumentos("hola",2,"chau") ## Le pasé una tupla de argumentos a imprimir
kwargumentos(name="gabo",surname="ga",edad=3) ## en este caso es un diccionario

#############################################################################


def suma(a,b):
	return a+b
def mul(a,b):
	return a*b
def res(a,b):
	return a-b
def div(a,b):
	return a/b

op={
	"suma": suma, #creo un diccionario de funciones
	"mul":mul,
	"res":res,
	"div":div,
}	

print(op["suma"](15,3)) #llamo a la funcion del diccionario, como argumento, en un print con sus argumentos