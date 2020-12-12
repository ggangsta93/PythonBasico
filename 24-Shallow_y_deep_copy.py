#SHALLOW Y DEEP COPY

print("-----------------------------------")
#esto no es una copia, sólo se referencia a la misma instancia que a
a=5
b=a
nombres1 = ["Javier","Arias"]
nombres2 = nombres1
#ambos a la misma instancia
print("nombres1:",nombres1)#nombres1 ['Javier', 'Arias']
print("nombres2:",nombres2)#nombres2 ['Javier', 'Arias']
nombres2[0]="Pedro"
print("nombres1:",nombres1)#nombres1 ['Pedro', 'Arias']


print("----------------------Copia con slice de un objeto que NO es compuesto------")
#parece que no tenemos el problema anterior
vocales = ["a","e","i","o","u"]
vocales2 = vocales[:]

print("vocales:",vocales)
print("vocales2:",vocales2)
vocales2[1]="Z"
print("vocales:",vocales)
print("vocales2:",vocales2)

print("----------------------Copia con slice de un objeto que es compuesto------")

letras=["a","e","i",["w","x","y"]]
letras2=letras[:]

print("letras:",letras)#letras: ['a', 'e', 'i', ['w', 'x', 'y']]
print("letras2:",letras2)#letras2: ['a', 'e', 'i', ['w', 'x', 'y']]
letras2[3][0]="O"
print("letras:",letras)#letras: ['a', 'e', 'i', ['O', 'x', 'y']]
print("letras2:",letras2)#letras2: ['a', 'e', 'i', ['O', 'x', 'y']]
letras2[3]="P"
print("letras:",letras)#letras: ['a', 'e', 'i', ['O', 'x', 'y']]
print("letras2:",letras2)#letras2: ['a', 'e', 'i', 'P']

print("----------------------Para solucionar hacemos una COPIA PROFUNDA------")
from copy import deepcopy

letras=["a","e","i",["w","x","y"]]
letras2=deepcopy(letras)

print("letras:",letras)#letras: ['a', 'e', 'i', ['w', 'x', 'y']]
print("letras2:",letras2)#letras2: ['a', 'e', 'i', ['w', 'x', 'y']]
letras2[3][0]="O"
print("letras:",letras)#letras: ['a', 'e', 'i', ['w', 'x', 'y']]
print("letras2:",letras2)#letras2: ['a', 'e', 'i', ['O', 'x', 'y']]
letras2[3]="P"
print("letras:",letras)#letras: ['a', 'e', 'i', ['w', 'x', 'y']]
print("letras2:",letras2)#letras2: ['a', 'e', 'i', 'P']




