from io import open
import sys

arch=open("contador.txt","a+")
arch.seek(0)
contenido=arch.readline()

if len(contenido)==0:
    contenido="0"
    arch.write(contenido)

arch.close()

try:
    contador=int(contenido)

    if len(sys.argv)==2:
        if sys.argv[1]=="inc":
            contador+=1
        elif sys.argv[1]=="dec":
            contador-=1

    print(contador)

    fichero=open("contador.txt","w")
    fichero.write(str(contador))
    fichero.close()

except:
    print("Archivo corrupto")


