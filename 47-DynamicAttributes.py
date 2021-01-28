#Uso de Slots y atributos dinamicos
#Nuestra clase debe de descender de object

class Persona:
    "Esta es la clase persona"

    #Usar __slots__ para evitar los atributos dinamicos
    #__slots__=('Nombre','Edad')

    #No hay constructor explicitom pero usamos __init__
    
    def __init__(self, nombre, edad):
        print ("Estamos en __init__")
        self.Nombre = nombre
        self.Edad = edad
    
    #Definimos un metodo
    def muestra(self):
        print("Mi nombre es",self.Nombre)
        print("Mi edad es ",self.Edad)
        print("-------")
    
    #No hay destructor explicito, pero usamos __del__
    def __del__(self):
        print("Bye desde: ",self.Nombre)

#Creamos la instancia
persona1 = Persona("Aldo",18)

#Invocamos metodo
persona1.muestra()

#Creamos un atributo dinamico
persona1.dato = 60
print(persona1.dato)
