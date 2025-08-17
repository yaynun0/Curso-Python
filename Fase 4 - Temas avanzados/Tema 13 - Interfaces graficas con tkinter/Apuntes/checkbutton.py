from tkinter import *

def seleccionar():
    cadena=""
    if (leche.get()):
        cadena+="Con leche"
    else:
        cadena+="Sin leche"
    if (azucar.get()):
        cadena+=" y con azucar"
    else:
        cadena+=" y sin azucar"
        
    monitor.config(text=cadena)
        
        


    



# Configuración de la raíz
root = Tk()
root.title("Cafetería")
root.config(bd=15)

leche=IntVar()
azucar=IntVar()

imagen=PhotoImage(file="imagen.gif")
Label(root,image=imagen).pack(side="left")

frame=Frame(root)
frame.pack(side="right")

Label(frame,text="¿Como quieres el café?").pack(anchor="w")
Checkbutton(frame,text="Con leche",variable=leche,onvalue=1,offvalue=0,command=seleccionar).pack(anchor="w")
Checkbutton(frame,text="Con azucar",variable=azucar,onvalue=1,offvalue=0,command=seleccionar).pack(anchor="w")


monitor=Label(frame)
seleccionar()
monitor.pack()



# Finalmente bucle de la apliación
root.mainloop()