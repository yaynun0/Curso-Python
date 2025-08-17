import math,random
def leer_numero(ini,fin,mensaje):
    while True:
        try:
            n=int(input(mensaje))
        except:
            print("Error: Numero no valido")
        else:
            if n>=ini and n<=fin:
                break

    return n

def generador():
    numeros=leer_numero(1,20,"¿Cuantos numeros quieres generar? [1-20]: ")
    modo=leer_numero(1,3,"¿Como quieres redonder los numeros? [1]Al alza [2]A la baja [3]Normal: ")
    l=[]
    for i in range(numeros):
        n=random.uniform(0,101)
        match modo:
            case 1:
                n=math.ceil(n)
            case 2:
                n=math.floor(n)
            case 3:
                n=round(n)
        l.append(n)

    print(l)

    return l 

generador()


