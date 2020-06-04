import sqlite3

miConexion=sqlite3.connect("GestionProductosBBDD3")

miCursor=miConexion.cursor()
"""
miCursor.execute('''

		CREATE TABLE PRODUCTOS(
		ID INTEGER  PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
		PRECIO INTEGER,
		SECCION VARCHAR(20)
		)
	''')

productos=[

	("balon",15,"deportes"),
	("camiseta",10,"deportes"),
	("jarron",90,"ceramica"),
	("camion",20,"jugueteria"),
	("camisetas",20,"deportes")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR03','tren',15,'jugueteria')")
"""
"""
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='deportes'")
productos=miCursor.fetchall()
print(productos)
"""

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()

miConexion.close()