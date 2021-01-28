#Este archivo es el modulo

print("*"*20)
print("Has importado el modulo")
x=100
print("En el modulo x=",x)
print("*"*20)
r = 500

def suma (a,b):
    global r
    r =a+b
    print ("suma",r)

def imprime_x():
    print("x desde el modulo= ",x)

def imprime_r():
    print("r desde el modulo= ",r)