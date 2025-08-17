import os
import re
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system()=="Windows" else os.system('clear')

def leer_texto(longitud_min=0,longitud_max=100,mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto=input("> ")
        if longitud_min<=len(texto)<=longitud_max:
            return texto
        
def dni_valido(dni,lista):
    if not re.match('[0-9]{2}[A-Z]$',dni):
        print("DNI incorrecto, debe cumplir con el formato")
        return False
    
    for cliente in lista:
        if cliente.dni==dni:
            print("DNI ya registrado")
            return False
    return True