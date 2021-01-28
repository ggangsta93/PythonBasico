#Un generador es una funcion que regresa un objeto generator
#Un generator se puede ver como una funcion que produce una secuencia de
#resultados en lugar de un solo objeto. Estos son producidos al iterar
#yield es lo que convierte a una funcion en un iterador
#Se termina la ejecucion cuando se ha llegado a yield y el valor es regresado
#Cuando se usa next, se avanza al siguiente yield
#cualquier estados intermedio de las variables se  guarda entre invocaciones
#cosa que no sucede en las funciones

def dias_generador():
    yield("Lunes")
    yield("Martes")
    yield("Miercoles")
    yield("Jueves")
    yield("Viernes")

dias = dias_generador()
print("El tipo es_ ",type(dias))

#next recibe tipo generator, list_iterator
print("--> ",next(dias))#
print("--> ",next(dias))
print("--> ",next(dias))
print("--> ",next(dias))
print("--> ",next(dias))
#print("--> ",next(dias))#Lanza una exception tipo StopIteration

print("----------------------Creamos un generador para potencias de dos------")

#Se podria tener simplemente una funcion que genere las potencias y los guarde
#en unas lista, Para este caso se tiene una funcion que genera las potencias
#cada vez que se da next()

def potencia2():
    b=1
    while b>0:
        yield b
        b = b+b

binarios = potencia2()

print("El tipo es: ",type(binarios))#generator

for x in binarios:
    print(x)
    if x>100:#Si no se especifica el generator es infinito
        break

print("----------------------Creamos un generador para potencias de dos hasta cierto numero------")

def potencias2():
    b=1
    while b>0:
        yield b
        b=b+b
        if b>300:
            raise StopIteration#ESTO PRODUCE UN ERRROR POR REVISAR

binario = potencias2()
for x in binario:
    print(x)