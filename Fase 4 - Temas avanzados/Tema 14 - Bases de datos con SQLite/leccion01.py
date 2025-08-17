import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor= conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Hector',27,'hector@ejemplo.com')")

#cursor.execute("SELECT * FROM usuarios")
#print(cursor)

#usuarios=[
#    ('Andres',51,'andres@ejemplo.com'),
#    ('Barabara',88,'barb@ejemplo.com'),
#    ('Carlos',54,'carlos@ejemplo.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)",usuarios)


cursor.execute("SELECT * FROM usuarios")

usuarios=cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conexion.commit()

conexion.close()


