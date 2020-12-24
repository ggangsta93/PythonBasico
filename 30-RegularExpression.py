#Expresiones regulares
#Se usan para filtrar textos y verificar si un texto concuerda con la expresion
#importamos el modulo re

import re

a = re.search("casa","La casa del casamentero")
print(a)

if re.search("casa","El estudiante es un casanova en la escuela"):#La expresion regular es casa
    print("1. Sí. está")#<--
else:
    print("1. No. no está")


if re.search(" casa ","El estudiante es un casanova en la escuela"):
    print("2. Sí. está")
else:
    print("2. No. no está")#<--

print("----------------------uso de . significa cualquier caracter------")
if re.search("ca.","Saluda al mas cabal"):
    print("Hay palabra que inicia con ca")#<--
else:
    print("No hay palabra que inicia con ca")

print("----------------------uso de clases de caracteres, se usa [] para contener los caracteres------")
if re.search("N[ie]c","Hola Nico"):#Recordar que aqí si importan las mayusculas y minusculas
    print("Se encontró")#<--
else:
    print("No se encontró.")
