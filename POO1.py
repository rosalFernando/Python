class Coche():

	#propiedades de la clase
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

	#comportamiento de clase (metodos)
	def arrancar(self):
		self.enmarcha=True

	def estado(self):
		if self.enmarcha:
			return "el coche esta en marcha."
		else:
			return "el coche esta parado."

miCoche=Coche()
print("el largo del coche es: ",miCoche.largoChasis)
print("el coche tiene: ", miCoche.ruedas, " ruedas")
miCoche.arrancar()

print(miCoche.estado())

