from tkinter import *
from tkinter import filedialog as FD
from io import open


ruta="" 

def nuevo():
    global ruta
    mensaje.set("Nuevo archivo")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir archivo")
    ruta=FD.askopenfilename(initialdir='.',
                            filetype=(("Archivos de texto","*.txt"),),
                            title="Abrir archivo de texto")
    if ruta!="":
        arch=open(ruta,'r')
        contenido=arch.read()
        texto.delete(1.0,"end")
        texto.insert('insert',contenido)
        arch.close()
        root.title(ruta+" - Mi editor")


def guardar():
    mensaje.set("Guardar archivo")
    if ruta!="":
        contenido=texto.get(1.0,"end-1c")
        arch=open(ruta,'w+')
        arch.write(contenido)
        arch.close()
        mensaje.set("El archivo {} se ha guardado correctamente".format(ruta))
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar archivo como")
    arch=FD.asksaveasfile(title="Guardar archivo",mode="w",defaultextension=".txt")
    if arch is not None:
        ruta=arch.name
        contenido=texto.get(1.0,"end-1c")
        arch=open(ruta,'w+')
        arch.write(contenido)
        arch.close()
        mensaje.set("El archivo {} se ha guardado correctamente".format(ruta))
    else:
        mensaje.set("Guardado cancelado")
        ruta=""



# Configuración de la raíz
root = Tk()
root.title("Mi editor")


# Menú superior

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)
menubar.add_cascade(menu=filemenu,label="Archivo")



#Caja de texto central

texto=Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",12))

#Monitor inferior



mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root,textvar=mensaje,justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
root.mainloop()