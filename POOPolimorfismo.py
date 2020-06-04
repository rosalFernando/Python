class Coche():
	def desplazamiento(self):
		print("me desplazo utilizando 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("me desplazo utilizando 2 ruedas")


class Camion():
	def desplazamiento(self):
		print("me desplazo utilizando muchas ruedas")


def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Coche()

desplazamientoVehiculo(miVehiculo)
