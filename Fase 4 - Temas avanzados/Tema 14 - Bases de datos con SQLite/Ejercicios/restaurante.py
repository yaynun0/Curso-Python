import sqlite3

def crear_bd():
	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()

	try:

		cursor.execute('''
				CREATE TABLE categoria(
	                id INTEGER PRIMARY KEY AUTOINCREMENT,
	                nombre VARCHAR(100) UNIQUE NOT NULL)
			''')
	except sqlite3.OperationalError:
		print("La tabla de Categorias ya existe")
	else:
		print("La tabla de Categorias se ha creado")


	try:
		cursor.execute('''
				CREATE TABLE plato(
	                id INTEGER PRIMARY KEY AUTOINCREMENT,
	                nombre VARCHAR(100) UNIQUE NOT NULL, 
	                categoria_id INTEGER NOT NULL,
	                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
			''')
	except sqlite3.OperationalError:
		print("La tabla de Platos ya existe")
	else:
		print("La tabla de Platos se ha creado")

	conexion.close()

def agregar_categoria():
	categoria=input("Ingrese el nombre de la nueva categoria\n > ")
	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categoria))
	except sqlite3.IntegrityError:
		print("\nLa categoria '{}' ya existe".format(categoria))
	else:
		print("\nCategoria '{}' creada correctamente".format(categoria))


	conexion.commit()
	conexion.close()

def agregar_plato():
	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()

	categorias=cursor.execute("SELECT * FROM categoria").fetchall()
	print("Selecciona una categoria para añadir el plato")

	for categoria in categorias:
		print("[{}] {}".format(categoria[0], categoria[1]))

	cat_usuario=int(input("\n> "))

	plato=input("\nNombre del nuevo plato: \n>")

	try:
		cursor.execute("INSERT INTO plato VALUES (null,'{}',{})".format(plato,cat_usuario))
	except sqlite3.IntegrityError:
		print("\nEl plato '{}' ya existe".format(plato))
	else:
		print("\nPlato '{}' creada correctamente".format(plato))


	conexion.commit()
	conexion.close()

def mostrar_menu():
	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()

	categorias=cursor.execute("SELECT * FROM categoria").fetchall()
	
	print("\t\t\t ~~~MENU~~~")
	for cat in categorias:
		print("\n\t '{}'\n".format(cat[1]))
		platos=cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(cat[0])).fetchall()
		for pl in platos:
			print("* {}\n".format(pl[1]))

	conexion.close()

#Crear base de datos
crear_bd()

#Menu

while True:
	print("\nBienvenido al gestor del restaurante")
	opcion=input("\nIntroduce una opcion:\n [1] Agregar una categoria\n [2] Agregar un plato\n [3] Mostrar menu \n [4] Salir del programa\n\n >")

	if opcion=="1":
		agregar_categoria()
	elif opcion=="2":
		agregar_plato()
	elif opcion=="3":
		mostrar_menu()
	elif opcion=="4":
		break
	else:
		print("Opcion incorrecta")