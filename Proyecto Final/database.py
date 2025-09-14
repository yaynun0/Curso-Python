import csv
import config

class Cliente:
    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"


class Clientes:
    lista=[]
    with open(config.DATABASE_PATH,newline='\n') as archivo:
        reader=csv.reader(archivo,delimiter=';')
        for dni,nombre,apellido in reader:
            cliente=Cliente(dni,nombre,apellido)
            lista.append(cliente)


    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
            
    @staticmethod
    def crear(dni,nombre,apellido):
        cliente=Cliente(dni,nombre,apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni,nombre,apellido):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni==dni:
                Clientes.lista[indice].nombre=nombre
                Clientes.lista[indice].apellido=apellido
                Clientes.guardar()
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(dni):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni==dni:
                cl=Clientes.lista.pop(indice)
                Clientes.guardar()
                return cl
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH,'w',newline='\n') as archivo:
            writer=csv.writer(archivo,delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni,cliente.nombre,cliente.apellido))
        