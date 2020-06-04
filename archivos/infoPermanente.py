import pickle

class Persona():

	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad

		print("se ha creado una persona nueva llamada: ",self.nombre)

	def __str__(self):
		return "{}{}{}".format(self.nombre,self.genero,self.edad)


class listaPersonas():
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno","ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("se cargaron {} personas del fichero ".format(len(self.personas)))

		except:
			print("fichero vacio")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregaPersona(self,p):
		self.personas.append(p)
		self.guardarPersonasFichero()

	def mostrarPersona(self):
		for p in self.personas:
			print(p)

	def guardarPersonasFichero(self):
		listaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas,listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfo(self):
		print("informacion del fichero: ")

		for p in self.personas:
			print(p)



miLista=listaPersonas()

p=Persona("juan","masculino",69)
miLista.agregaPersona(p)


miLista.mostrarInfo()
