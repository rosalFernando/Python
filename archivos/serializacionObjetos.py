import pickle

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

coche1=Vehiculo("citroen","c15")
coche2=Vehiculo("seat","iniza")
coche3=Vehiculo("ferrari","italia")

#coleccion de objetos
coches=[coche1,coche2,coche3]

fichero=open("coches","wb")

pickle.dump(coches,fichero)

fichero.close()

del(fichero)

ficheroApertura=open("coches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:

	print(c.estado())