def saludar():
    print("Hola desde saludos.saludar()")

class Saludo:
    def __init__(self):
        print("Hola desde Saludo.__init__")

if __name__ == '__main__':  #para no ejecutar código del modulo desde otro script
    saludar()