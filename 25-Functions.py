#Definicion de funciones

def mostrar(numero):
    "Esto es un Docstring; Esta funcion imprime el número."
    print(numero)

def multi(a, b=5):
    """
    Esta es una funcion con parametros opcionales,
    y sirve para multiplicar 2 numeros
    """
    r=a*b
    return r

def muestraValores(a=5, c=9, b=2):
    print("A es ",a)
    print("B es ",b)
    print("C es ",c)

def sumatoria(a, *mas):
    sum = a
    if len(mas)>0:
        for n in mas:
            sum = sum + n
    print ("La sumatoria es: ",sum)

print("####################Aquí el codigo principal##############")
mostrar(1)
mostrar(3)
mostrar(5)

print("----------------------Aquí vemos el uso de Docstring------")
print(mostrar.__doc__)

print("----------------------Aquí usamos las funciones con parametros y keyword------")
print("El resultado es: ",multi(3,7))#21
print("El resultado es: ",multi(4))#20

muestraValores()
muestraValores(c=50, a=1)


print("----------------------Aquí usamos numero de parametros arbitrarios------")
sumatoria(5)#5
sumatoria(5,3,1)#9
sumatoria(1,2,3,4,5)#15

