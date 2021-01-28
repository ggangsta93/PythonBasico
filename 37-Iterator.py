#iterador - nos permite recorrer una estructura de datos sin que nos
#interese conocer la forma como trabaja esa estructura, usamos forma

#Generador - es una funcion especial que nos permite implementar iteradores

#internamente el for trabaja con un iterador que va pidiendo el elemento
#siguiente hasta que recibe StopIteration

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

for i in dias:
    print(i)

print("----------------------Creando nuestro Iterator------")

#Se invoca iter en la estructura y nos regresa un objeto iterable
mi_iterador = iter(dias)

#Usamos el iteravle con next parqa obtener el elemento siguiente

print("--> ",next(mi_iterador))#Se lee el elemento actual y avanza el siguiente
print("--> ",next(mi_iterador))
print("--> ",next(mi_iterador))
print("--> ",next(mi_iterador))
print("--> ",next(mi_iterador))#Cuando no hay más elementos recibe el StopIteration
#print("--> ",next(mi_iterador))#Lanza una exception

print("----------------------Creando nuestro Iterator------")

mi_iterador2 = iter(dias)
print("El tipo es: ",type(mi_iterador2))#<class 'list_iterator'>

while mi_iterador2:
    try:
        d=next(mi_iterador2)
        print("=> ",d)
    except:
        print("No hay más elementos, forzamos la salida")
        break
