#Metodo estatico
#Metodo de clase
#Funciones de interfaz
#Propiedades

class Persona:
    "Esta es la clase persona"

    #Variable de clase
    cantidad=0

    #Atributo publico
    valor = 0

    #Atributo privador
    __dato=20

    #No hay constructor explicito pero usamos __init__
    
    def __init__(self, nombre, edad):
        print ("Estamos en __init__")
        self.Nombre = nombre
        self.Edad = edad
    
    #Definimos un metodo
    def muestra(self):
        print("Mi nombre es",self.Nombre)
        print("Mi edad es ",self.Edad)
        print("El valos guardado es",self.valor)
        print("El dato es ",self.__dato)
        print("La cantidad es ",Persona.cantidad)#Variable de clase
        print("-------")
    
    def ponCantidad(self, cant):
        Persona.cantidad = cant

    def muestraSaludo(self):
        print("Hola, soy ",self.Nombre)
    
    #No hay destructor explicito, pero usamos __del__
    def __del__(self):
        print("Bye desde: ",self.Nombre)

    #Creamos un metodo estatico, este no lleva el self
    @staticmethod
    def mensaje(msg):
        print ("Tienes este mensaje: ",msg)
    
    #Creamos un metodo de clase
    #Se usan en el patron fabrica
    """
    Usamos el decorador classmethod para indicar que es de este tipo
    En lugar de usar self usamos cls como parametro
    Esto indica que no apunta a la instancia sino a la clase
    no puede modificar el estado del objeto pero puede modificar 
    el estado de la clase que se aplica a todas las instancias
    Tiene la misma implmenetacion en todas las instancias
    """
    @classmethod
    def autor(cls):#No existe equivalente en algunos otros lenguajes de programacion
        print("La clase ",cls.__name__)
        print("fue creada por Javier")
    
    #Creamos funciones de interfaz para __dato
    def get_dato(self):
        return self.__dato
    
    def set_dato(self, pDato):
        print("En propiedad")
        self.__dato = pDato
    
    #Creamos propiedades para Nombre
    """
    @property
    def Nombre(self):
        return self.Nombre
    
    @Nombre.setter
    def Nombre(self, pDato):
        self.Nombre=pDato
    """
#Hacemos uso de funciones de interfaz
persona1=Persona("Susana",20)
persona1.muestra()
persona1.set_dato(67)
persona1.muestra()



