#operador lambda
#Crea funciones anonimas que se usan al momento que hacen falta
#Generalmente se usan con filter(), map(9, reduce()
#lambda arg1, arg2,...:expresion

valor = lambda a,b: a*a+2*a*b+b*b
print("El trinomio cuadrado perfecto es: ",valor(2,3))


print("----------------------uso de map()------")
def cuadrados(valor):
    return valor*valor

valores = [2,5,10]

resultados = list(map(cuadrados, valores))#map(lambda x: x*x, valores)
print(resultados)#[4, 25, 100]

print("----------------------uso de filter()------")
def impares(valor):#lambda x: (x%2!=0)
    return (valor%2)!=0

valores = [1,4,5,7,8,9,1012,15,17,18,28]

filtrados = filter(lambda x: (x%2!=0), valores)#Si es True los pasa a filtrados

print(list(filtrados))#[1, 5, 7, 9, 15, 17]


print("----------------------uso de reduce()------")

import functools
#Aplica una funcion de manera continua a una secuencia de valores
#y regresa yn unico valor
#[a1,a2,a3,a4,a5]
#b1 = fun(a1,a2)
#b2 = fun(b1,a3)
#b3 = fun(b2,a4)
#b4 = fun(b3,a5) --> Resultado final

valores = [1,2,3,4,5,6,7,8,9]

def suma(a,b):
    return a+b

r = functools.reduce(lambda  a,b: a+b, valores)

print("La suma es: ",r)



