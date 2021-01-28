#Memoization
#Se guarda los valores calculados previamente en una funcion
#para volver a utilizarlos si es necesario en lugar de volver a 
#calcularlos

def fibonacciIterativo(n):
    a=0
    b=1
    if n==0:
        return 0
    for i in range(n-1):
        anterior =a
        a=b
        b=anterior+b
    return b

def fibonacciRecursivo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2)

print("Iterativo ",fibonacciIterativo(35))
print("Recursivo ",fibonacciRecursivo(35))   

print("----------------------Con una memoization programada a mano------")

calculados = {0:0, 1:1}

def fibonacciMemoizado(n):
    if n in calculados:
        return calculados[n]
    else:
        calculados[n]=fibonacciMemoizado(n-1)+fibonacciMemoizado(n-2)
        return calculados[n]

print("Memoizados ",fibonacciMemoizado(35))


print("----------------------Con una memoization creada con un decorador------")

def memoizacion(f):
    calculados = {}

    def encuentra(a):
        if a not in calculados:
            calculados[a]=f(a)
        return calculados[a]

    return encuentra#esto es la funcion encuentra(a)
    
def fibonacciDecorador(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciDecorador(n-1)+fibonacciDecorador(n-2)

#Decoramos
fibdec = memoizacion(fibonacciDecorador)

print("Decorado ",fibdec(35))
