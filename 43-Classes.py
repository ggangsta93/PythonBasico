#Definimos una clase

class Persona:
    "Esta es la clase persona"

    #Variable de clase
    cantidad=0

    #Atributo publico
    valor = 0

    #Atributo privador
    __dato=20

    #No hay constructor explicitom pero usamos __init__
    
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

#Imprimimos el doc sring
print(Persona.__doc__)

#Creamos la instancia
persona1 = Persona("Aldo",18)

#Accedemos a atributo
persona1.valor=5

#Invocamos metodo
persona1.muestra()

#Un atributo privado
persona1.__dato = 3
print("Intento imprimir el dato ",persona1.__dato)
print("-----")

#invocamos metodo
persona1.muestra()

#Creamos otra instancia
persona2 = Persona("Ana",20)
persona2.muestra()
del persona2

print("----------------------HERENCIA------")

class Empleado(Persona):
    #Atributo de empleado
    sueldo = 0

    #Inicializacion
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        self.sueldo = salario
    
    #Metodo que aprovecha el metodo de la clase padre
    def muestraEmpleado(self):
        Persona.muestra(self)
        print("El sueldo es ",self.sueldo)
    
    #Override de un metodo
    def muestraSaludo(self):
        super().muestraSaludo()
        print("y ",self.Nombre," tiene trabajo.")

#Probamos la variable de la clase

Persona1 = Empleado("Javier",18,1500)
Persona2 = Empleado("Maria",20,1200)

Persona1.valor=50
Persona1.ponCantidad(2)#Atributo de clase haciendo uso de interface, (Persona1.cantidad=2 <--Esto no funciona)


Persona1.muestraEmpleado()
Persona2.muestraEmpleado()

Persona1.muestraSaludo()#Aqui se demuestra el override







