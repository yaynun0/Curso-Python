from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Configuración de la raíz
root = Tk()

def test():
    #MessageBox.showinfo("Hola","Hola mundo") #i
    #MessageBox.showwarning("Hola","Hola mundo") #!
    #MessageBox.showerror("Hola","Hola mundo") #x
    """resultado=MessageBox.askquestion("Salir","Estas seguro que quieres salir sin guardar?")
    if resultado=="yes":
        root.destroy()"""
    #resultado=MessageBox.askokcancel("Salir","Estas seguro que quieres salir sin guardar?")
    #resultado=MessageBox.askyesno("Salir","Estas seguro que quieres salir sin guardar?")
    #resultado=MessageBox.askretrycancel("Reintentar","No se puede conectar")
    #if resultado:
    #    test()
    
    
    #color=ColorChooser.askcolor(title="Elige un color")
    #print(color)

    """ruta=FileDialog.askopenfilenames(title="Abrir un archivo",initialdir="C:/Users\lgera\OneDrive\Escritorio\CursoPython",
                                     filetypes=(("Archivos de texto","*.txt"),
                                                ("Archivos de python","*.py"),
                                                ("Todos","*.*")))
    print(ruta)"""

    #arch=FileDialog.asksaveasfile("Guardar archivo",mode="",defaultextension=)      Equivale a open('ruta',mode)
    pass

Button(root,text="Presiona",command=test).pack()


# Finalmente bucle de la apliación
root.mainloop()