#switch no existe en python, nuevas formas de hacer lo mismo
salario_presidente=int(input("introduce salario de presidente"))
print("salario del presidente: "+ str(salario_presidente))
salario_director=int(input("introduce salario de presidente"))
print("salario del director: "+ str(salario_director))
salario_jefe_area=int(input("introduce salario de presidente"))
print("salario del jefe de area: "+ str(salario_jefe_area))
salario_administrativo=int(input("introduce salario de presidente"))
print("salario del administrativo: "+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("todo el orden")
else:
	print("algo falla")