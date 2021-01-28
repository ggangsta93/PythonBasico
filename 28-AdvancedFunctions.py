#Manejo avanzado de funciones y decoradores
#Es un objeto que puede ser invocado y que modifica una funcion o clase

#En python los nombres de las funciones son referencias y una funcion
#puede tener mas de un nombre

def cuadrado(a):
    r=a*a
    return r

potencia2 = cuadrado    
print(potencia2(2))#4 
print(cuadrado(4))#16

#si tenemos dos o mas referencias, podemos eliminar una sin perder la otra        
del cuadrado
print(potencia2(5))#25

print("----------------------En python se puede definir una funcion adentro de otra------")

def cuadradoPar(a):
    def checarPar(x):
        return x%2==0
    
    if(checarPar(a)):
        print("Se puede hacer el cuadrado")
        return a*a
    else:
        print("No se puede hace el cuadrado")
        return 0

print(cuadradoPar(16))
print(cuadradoPar(15))

print("----------------------En python las funcion es un objeto y cualquier objeto puede ser pasado------")
print("----------------------como parametro, porlo que las funciones pueder  ser pasadas como parametro------")

def parImpar(a):
    if(a%2==0):
        print("No es impar")
    else:
        print("Es impar")

def imprimeMucho(a):
    valor = str(a)
    print((valor+" - ")*a)

def potencia(func, x):
    r = x**x
    func(r)
    print("La potencia es ",r)

potencia(parImpar,5)
potencia(imprimeMucho,4)

print("----------------------Las funciones tambien pueden regresar funciones------")

def f(x):
    def g(y):
        print("Estoy en g, este es x: ",x," este es y: ",y)
        return y+x

    print("estoy en f, este es x: ",x)
    return g

nf1 = f(1)
nf2 = f(3)

print(nf1(5))
print(nf2(7))

print("-"*10)

print("----------------------Creación de un decorador------")
#definimos la funcion decoradora

def miDecorador(func):
    #Definimos la funcion que envuelve
    def decorador(a):
        print('Soy un "validador" de parametros: paramtro ',a," ¡validado!")
        func(a)

    return decorador        

#Decoramos la funcion
@miDecorador
def miFuncion(x):
    print("Estoy en mi funcion con x: ",x)

#Invocamos la funcion
miFuncion(5)
