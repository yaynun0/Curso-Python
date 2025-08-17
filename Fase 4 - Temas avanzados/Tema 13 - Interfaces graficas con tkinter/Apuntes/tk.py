from tkinter import *

root = Tk()

"""

#Variables dinamicas
texto=StringVar()
texto.set("Un nuevo texto")

Label(root,text="Hola mundo").pack(anchor="nw")
label=Label(root,text="Una etiqueta")
label.pack(anchor="center")
Label(root,text="Otra etiqueta").pack(anchor="se")

label.config(bg="green",fg="blue",font=("Verdana",24))
label.config(textvariable=texto)

"""

imagen=PhotoImage(file="imagen.gif")
Label(root,image=imagen,bd=0).pack(side="left")

root.mainloop()