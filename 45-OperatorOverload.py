#Sobrecarga de operadores
#+ __add__
#- __sub__
#* __mul__
#** __pow__
#/ __truediv__
#// __floordiv__
#% __mod__
#<< __lshift__
#>> __rshift__
#& __and__
#| __or__
#^ __xor__
#~ __invert__
#< __lt__
#<= __le__
#== __eq__
#!= __ne__
#> __gt__
#>= __ge__

import math

class Vector:
    def __init__(self, px=0, py=0):
        self.x=px
        self.y=py
    
    def __str__(self):
        return "(%f, %f)"%(self.x, self.y)
    
    #Sobrecarga del operador +
    def __add__(self, operando):
        mx = self.x+operando.x
        my = self.y+operando.y
        return Vector(mx, my)
    
    #Calculamos la magnitud
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    #Sobrecarga de ==
    def __eq__(self, operando):
        return self.magnitud()==operando.magnitud()
    
    #Sobrecarga de >
    def __gt__(self, operando):
        return self.magnitud()>operando.magnitud()

a=Vector(5,3)
b=Vector(-1,2)
d=Vector(5,3)

print(a)
print(b)

c = a+b
print(c)
print(a.magnitud())

if(a==b):
    print("a y b son iguales")
else:
    print("a y b son diferentes")

if(a==d):
    print("a y d son iguales")
else:
    print("a y d son diferentes")

if(a>b):
    print("a es mayor")
else:
    print("b es mayor")