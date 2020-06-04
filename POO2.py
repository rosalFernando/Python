class Coche():

	#constructor
	def __init__(self):

		#propiedades de la clase
		self.__largoChasis=250
		self.__anchoChasis=120
		#variable encapsulada
		self.__ruedas=4
		self.__enmarcha=False

	#comportamiento de clase (metodos)
	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if self.__enmarcha:
			return "el coche esta en marcha."
		else:
			return "el coche esta parado."

		

	def estado(self):
		print("el coche tiene ", self.__ruedas, "ruedas. un ancho de ", 
			self.__anchoChasis,"  y un largo de ", self.__largoChasis)
		
		

miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("-----------------------------")

print("creacion de segundo objeto.")

miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()