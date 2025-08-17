import sqlite3

conexion=sqlite3.connect("productos.db")
cursor=conexion.cursor()

#cursor.execute('''
 #   CREATE TABLE usuarios (dni VARCHAR(9) PRIMARY KEY,
#              nombre VARCHAR(100),
#               edad INTEGER,
#               email VARCHAR(100)
#               )
#''')

#usuarios=[
#    ('123456789','Hector',43,'hector@ejemplo.com'),
#    ('432843279','Andres',51,'andres@ejemplo.com'),
#    ('983243243','Barabara',88,'barb@ejemplo.com'),
#    ('261476847','Carlos',54,'carlos@ejemplo.com'),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)",usuarios)

#cursor.execute("INSERT INTO usuarios VALUES ('26147684A','Carlos',54,'carlos@ejemplo.com')")

cursor.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        marca VARCHAR(50) NOT NULL,
        precio FLOAT NOT NULL           
    )
''')

conexion.commit()
conexion.close()