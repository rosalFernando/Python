import sqlite3

miConexion=sqlite3.connect("primeraBase")

miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_PRODUCTOS VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('balon',15,'deportes')")
"""
variosProductos=[

	("camiseta",10,"deportes"),
	("jarron",90,"ceramica"),
	("camion",20,"jugueteria")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)
"""

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()
for producto in variosProductos:
	print(producto[0])

miConexion.commit()

miConexion.close()