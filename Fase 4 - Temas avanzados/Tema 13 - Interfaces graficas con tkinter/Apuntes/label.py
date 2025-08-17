from tkinter import *

# Configuración de la raíz
root = Tk()
"""
# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="¡Hola mundo!").pack(anchor="nw")
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="¡Última etiqueta!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)
"""


"""
#Imagenes en ventana
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")
"""

texto=Text(root)
texto.pack()
texto.config(width=30,height=10, font=("Arial",12),padx=5,pady=5,selectbackground="red")


# Finalmente bucle de la apliación
root.mainloop()