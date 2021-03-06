
class Vehiculo():

	def __init__(self, marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frenar(self):

		self.frena=True

	def estado(self):
		print("marca: ", self.marca, "\nModelo: ", self.modelo,
			"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,
			"\nFrenado: ",self.frena)

class Furgoneta(Vehiculo):
	def carga(self,carga):
		self.cargado=carga
		if self.cargado:
			return "la furgoneta esta cargada."
		else:
			return "la furgoneta no esta cargada."
print("-------------------------------")
mifurgoneta=Furgoneta("renault","Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))
print("-------------------------------")

class Moto(Vehiculo):
	haceCaballito=""

	def caballito(self):
		self.haceCaballito="Voy haciendo el gilipollas"
	def estado(self):
		print("marca: ", self.marca, "\nModelo: ", self.modelo,
			"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,
			"\nFrenado: ",self.frena,"\n",self.haceCaballito)
miMoto=Moto("honda","CBR")

miMoto.caballito()

miMoto.estado()

print("-------------------------------")

class VElectricos(Vehiculo):
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100

	def cargaEnergia(self):
		self.cargando=True

"""
al dar herencia a una clase siempre se tiene en cuenta el constructor
de la primera clase que incluye en la herencia
"""
class BicicletaElectrica(VElectricos,Vehiculo):
	
	pass

miBici=BicicletaElectrica("orbea","kc")

