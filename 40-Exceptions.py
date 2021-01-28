#Excepciones
#El codigo que tiene riesgo se coloca en el bloque try
#en lugar de try usamos except

#assert evalua una expresion, si la evaluacion es falsa se levanta una
#excepcion de tipo AssertionError

def pares(n):
    assert (n%2==0)#Si es false levanta la exception de tipo AssertionError
    print("Es par")

pares(4)
pares(16)
#pares(5)#Lanza la excepcion AssertionError

print("----------------------Except y Except AssertionError------")

try:
    print("vamos a intentar con un impar")
    pares(5)
except AssertionError: #con except solito: captura todas las excepciones que se puedan generar
    print ("fue un impar")
else:
    print("Era un par")

print("----------------------Finally------")
#finally se usa para poner codigo que se ejecuta independientemente de si la excepcion ocurre o no

try:
    print("vamos a intentar con un impar")
    pares(5)
except: #con except solito: captura todas las excepciones que se puedan generar
    print ("fue un impar")
else:
    print("Era un par")
finally:
    print("Gracias por usar el programa")


print("----------------------Argument------")
#argument da informacion sobre la exception

a="hola"

try:
    x = int(a)
    print(x)
except ValueError as inst:
    print("La instancia de la excepcion. ",type(inst))
    print("El argumento dice ",inst.args)

print("----------------------Multiples excepciones------")

class Fue1(RuntimeError):
    def __init__(self):
        print("Desde la clase")
    
class Fue2(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def checar(n):
    if n==1:
        raise Fue1
    if n==2:
        raise Fue2("Error")

    print("todo bien")

try:
    checar(2)
except Fue1 as Fue1:
    print("Excepcion para el 1")
    print("El argumento dice ",Fue1.args)
except Fue2 as Fue2:
    print("Exception para el 2")
    print("El argumento dice ",Fue2.args)


