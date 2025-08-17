import sqlite3
from tkinter import *

root=Tk()
root.title("Restaurante sin nombre - Menu")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root,text="   Restaurante sin nombre   ",fg="darkgreen", font=("Times New Roman",28,"bold italic")).pack()
Label(root,text="   Menu del día   ",fg="green", font=("Times New Roman",24,"bold italic")).pack()



Label(root,text="").pack()

conexion=sqlite3.connect("restaurante.db")
cursor=conexion.cursor()

#Buscar categorias y platos en la bd

categorias=cursor.execute("SELECT * FROM categoria").fetchall()

for cat in categorias:
    
    Label(root,text=cat[1],fg="black", font=("Times New Roman",20,"bold italic")).pack()

    platos=cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(cat[0])).fetchall()
    for pl in platos:
        cat_fr=Frame(root)
        cat_fr.pack(fill=BOTH,padx=10)
        Label(cat_fr,text=pl[1], fg="gray", font=("Verdana",15,"italic")).pack(side="left")
        Label(cat_fr,text="$", fg="gray", font=("Verdana",15,"italic")).pack(side="right")

    Label(root,text="")


conexion.close()

Label(root,text="$150 ", fg="darkgreen", font=("Times New Roman",20,"bold italic")).pack(side="right")

root.mainloop()