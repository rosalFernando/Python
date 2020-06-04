#encapsulacion de metodos

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
			chequeo=self.__chequeoInterno()

		if self.__enmarcha and chequeo:
			return "el coche esta en marcha."
		elif self.__enmarcha and chequeo==False:
			return "algo ha ido mal en el chequeo, no se puede arrancar."
		else:
			return "el coche esta parado."

		

	def estado(self):
		print("el coche tiene ", self.__ruedas, "ruedas. un ancho de ", 
			self.__anchoChasis,"  y un largo de ", self.__largoChasis)
	
	#metodo encapsulado para uso interno de la clase. "__" para encapsular	
	def __chequeoInterno(self):
		print("realizando chequeo interno.")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
			return True
		else:
			return False


miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("-----------------------------")

print("creacion de segundo objeto.")

miCoche2=Coche()

print(miCoche.arrancar(False))

miCoche2.estado()