from tkinter import *

def sumar():
    r.set(float(n1.get())+float(n2.get()))
    borrar()
    
def restar():
    r.set(float(n1.get())-float(n2.get()))
    borrar()
    
def mult():
    r.set(float(n1.get())*float(n2.get()))
    borrar()
    
def borrar():
    n1.set("")
    n2.set("")

# Configuración de la raíz
root = Tk()
root.config(bd=15)

n1=StringVar()
n2=StringVar()
r=StringVar()


Label(root,text="Numero 1").pack()
Entry(root,justify="center",textvariable=n1).pack()#Primer numero
Label(root,text="Numero 2").pack()
Entry(root,justify="center",textvariable=n2).pack() #Segundo numero
Label(root,text="Resultado").pack()
Entry(root,justify="center",textvariable=r,state="disabled").pack() #Resultado
Label(root,text=" ")
Button(root,text="Sumar", command=sumar).pack(side="left")
Button(root,text="Restar", command=restar).pack(side="left")
Button(root,text="Producto", command=mult).pack(side="left")


# Finalmente bucle de la apliación
root.mainloop()