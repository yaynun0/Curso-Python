personas=[]
with open("personas.txt","r",encoding="utf8") as arch:
    for linea in arch:
        linea=linea.replace("\n","")
        dato=linea.split(';')
        personas.append({'id':dato[0],'nombre':dato[1],'apellido':dato[2],'nacimiento':dato[3]})

print(personas)
