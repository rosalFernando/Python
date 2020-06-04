def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento:
		yield from elemento

ciudadesDevueltas=devuelveCiudades("madrid","barcelona","bilbao","cordoba")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))