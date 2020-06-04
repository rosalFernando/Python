class Persona():

	def __init__(self,nombre,edad,lugarResidencia):
		self.nombre=nombre
		self.edad=edad
		self.lugarResidencia=lugarResidencia

	def descripcion(self):

		print("nombre: ",self.nombre,", edad: ",self.edad, ", residencia: ", self.lugarResidencia)

class Empleado(Persona):

	def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("salario: ",self.salario,", antiguedad: ",self.antiguedad)


miPersona=Empleado(15000,15,"fernando",27,"Cordoba")

miPersona.descripcion()

#comprobacion de si un objeto pertenece a una clase
print(isinstance(miPersona,Empleado))
print(isinstance(miPersona,Persona))