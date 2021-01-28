#En este programa hacemos uso del modulo

#importamos el modulo
#Directorio actual, 1. "Primero lo busca en el directorio actual"
#variable PYTHONPATH 2.
#Path de default        3."Toca consultarlo en la documentacion"

import Modul29 #as rnd <--esto es un alias
#import Modul29 import suma,imprime

m=3
n=5

Modul29.suma(m,n) 

print("El valor de la variable del modulo es :",Modul29.x)


print("----------------------Variable local y luego la del modulo------")
#NOTA:Python prefiere lo local a lo exterior
x=50
print(x)#50
Modul29.imprime_x()#x desde el modulo = 100
Modul29.imprime_r()
print("----------------------Aquí usamos dir()------")
contenidosmodulo = dir(Modul29)
print(contenidosmodulo)#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'imprime', 'suma', 'x']

print("----------------------Aquí usamos reload()------")
#Hacemos que se ejecute nuevamente el codigo del modulo
#y se cargue nuevamente el modulo

Modul29.imprime_r()#8

import importlib #for >= python3.4
importlib.reload(Modul29)

Modul29.imprime_r()#500

print("----------------------Aquí importamos un paquete------")

from mensajes import adios, como, hola

hola.hola()
como.como()
adios.adios()




