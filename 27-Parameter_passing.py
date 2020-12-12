"""
PASO DE PARAMETROS
-Paso por copia con objeto inmutable
-Paso por referencia y copia con objeto mutable
-paso por referencia pero con copia superficial
"""

print("----------------------Paso por copia con objeto inmutable------")
def mostrar(a):
    print(" ID objeto ",id(a)," valor objeto ",a)
    a=100
    print(" ID objeto ",id(a)," valor objeto ",a)
    a=a+15
    print(" ID objeto ",id(a)," valor objeto ",a)

numero = 5
print("Antes ",numero," <--- ID:",id(numero))

mostrar(5)
print("Desde fuera ",numero," <--- ID:",id(numero))

print("----------------------Paso por copia con objeto mutable------")

def mostrarLista(lista):#en esta logica, está funcionando como copia y No por referencia
    print(" ID objeto ",id(lista)," valor objeto ",lista)
    lista= ["Hola","a todos"]
    #¿cómo le hago para asignar ese valor, pero con referencia? y sin usar index
    #lista.clear()
    #lista +=["Hola","a todos"]
    print(" ID objeto ",id(lista)," valor objeto ",lista)

def mostrarLista2(lista):#en esta logica, SÍ funciona por referencia
    print(" ID objeto ",id(lista)," valor objeto ",lista)
    lista += ["Hola","a todos"]
    lista[3][0]="hamburguesa"
    print(" ID objeto ",id(lista)," valor objeto ",lista)


print("===Actua como copia")
palabras = ["pizza","auto","programación",["python","go","typescript"]]
print("Antes ",palabras," <--- ID:",id(palabras))
mostrarLista(palabras)
print("Desde fuera ",palabras," <--- ID:",id(palabras))

print("===Actua como referencia")
palabras = ["pizza","auto","programación",["python","go","typescript"]]
print("Antes ",palabras," <--- ID:",id(palabras))
mostrarLista2(palabras)
print("Desde fuera ",palabras," <--- ID:",id(palabras))

from copy import deepcopy

print('===Ahora actua como referencia pero con copia superficial "Shallow"')
palabras = ["pizza","auto","programación",["python","go","typescript"]]
print("Antes ",palabras," <--- ID:",id(palabras))
mostrarLista2(palabras[:])#Se puede utilzar el deepcopy para quitar lo superficial Ej: deepcopy(palabras)
print("Desde fuera ",palabras," <--- ID:",id(palabras))