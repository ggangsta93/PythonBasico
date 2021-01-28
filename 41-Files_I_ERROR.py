#lectura de archivos

#r - solo lectura
#rb - solo lectura en formato binario
#r+ - lectura y escritura, apuntador al inicio del archivo
#rb+ - igual que el anterior pero en binario
#w - solo escritura
#wb - solo escritura en binario
#w+ - escritura y lectura, sobre escribe el archivo si existe
#wb+ - igual que el anterior pero en binario}
#a - abre para append (adicion), el apuntador al final del archivo
#ab - igual pero en binario
#a+ - abre para append o lectura, el apuntador al final del archivo
#ab+ - igual pero en binario

print("----------------------Abrimos el archivo para lectura------")

archivo = open("miTexto.txt","r")#obtengo un referencia a ese archivo

#Recorremos el archivo linea por linea
for linea in archivo:
    print(linea.rstrip())#saca una copia y luego se imprime

print("Nombre: ",archivo.name)
print("Cerrado? : ",archivo.closed)
print("Modo de apertura: ",archivo.mode)

#Cerramos el archivo
archivo.close()

print("----------------------Abrimos el archivo para escritura------")

archivo = open("otroTexto.txt","w")#con w se sobreescrbe el archivo, con a lo agrega al final del archivo
n=0

#Escribimos 5 letras
while n<5:
    texto = input("Dame un texto")
    archivo.write(texto+"\n")
    n=n+1

#Cerramos el archivo
archivo.close()

print("----------------------Abrimos el archivo a una lista------")

lista = open("miTexto.txt","r").readlines()
print(lista)

print("-----------------------------------------------------------")

archivo = open("miTexto.txt","r")

#Vemos la posicion
pos =archivo.tell()
print("posicion ",pos)

#Colocamos en una posicion
#0-Inicio
#1-posicion actual
#2-final del archivo

archivo.seek(5,0)#ESTO PRODUCE UN ERROR CUANDO LE PONGO 1,"LANZA UN EXCEPCION"
cadena=archivo.read(8)
print(cadena)
pos=archivo.tell()
print("Posicion ",pos)#para saber en que posicion quedó
archivo.close()


print("----------------------Serialización------")
#Tres protocolos, 0-ascii, 1-compacto, 2-clases optimizadas
#importamos el modulo
import pickle
#Creamos el objeto a serializar
lista1=[5,"Hola"]
lista2=[7.8,"Python",True]

#Abrimos para escritura
archivo=open("misDatos.dato","w")

#Serializamos
pickle.dump(lista1,archivo)#ESTO PRODUCE UN ERROR: EL ARGUMENTO DEBER SER STR Y NO BYTES
pickle.dump(lista2,archivo)

#Cerramos 
archivo.close()

#Deserializamos
archivo = open("misDatos.dato","r")
lst1=pickle.load(archivo)
lst2=pickle.load(archivo)

print(lst1)
print(lst2)

archivo.close()