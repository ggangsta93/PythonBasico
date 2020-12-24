#Compresion de listas
#Implementa en las listas la notacion de los con juntos que usan los matematicos

valores = [1,2,3,4,5]

cuadrados=[(x*x) for x in valores]
print("CUADRADOS: ",cuadrados)


#TCP-------------------------------------------
#x=1, y=1
#x=1, y=2
#x=2, y=1
#x=2, y=2
trinomios = [(x*x+2*x*y+y*y) for x in  range(1,3) for y in range(1,3)]#
print("TCP: ",trinomios)

#PULGAS A CMS-----------------------------------
pulgadas = [1,3.5,-6,-2,5.1,-3.2]
cm =[(x*2.54) for x in pulgadas if x>0]
print("PULGAS: ",cm)

#NOTA: con corchetes "[]" obtendré una lista, con parentesis "()" obtendré un generador, y con llaves "{}" obtendré un conjunto o set

valores = [1,2,3,4,5,4,5]
gen1 = (x*x for x in valores)

print(gen1)
#convertimos a lista
print(list(gen1))