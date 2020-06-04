import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''

		CREATE TABLE PRODUCTOS(
		ID INTEGER  PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50),
		PRECIO INTEGER,
		SECCION VARCHAR(20)
		)
	''')

productos=[

	("balon",15,"deportes"),
	("camiseta",10,"deportes"),
	("jarron",90,"ceramica"),
	("camion",20,"jugueteria")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR03','tren',15,'jugueteria')")

miConexion.commit()

miConexion.close()