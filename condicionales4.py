#uso de and, or, in
"""
print("programa de becas.")

distancia_escuela=int(input("introduce la distancia a la escuela en Km: "))
print("la distancia es: "+ str(distancia_escuela)+ " Km")

numero_hermanos=int(input("introduce el numero de heramnos: "))
print("numero de hermanos: "+str(numero_hermanos))

salario_familiar=int(input("introduce salario anual bruto: "))
print("salario: "+str(salario_familiar)+ " €")

if distancia_escuela > 40 and numero_hermanos>2 or salario_familiar<=20000:
	print("tienes derecho a beca")
else:
	print("no tienes derecho a beca")

"""

#uso de in

print("asignaturas optativas")
print("-------------")
print("informatica grafica")
print("pruebas de software")
print("usabilidad y accesibilidad")
print("-------------")

opcion=input("escribe la asignatura escogida: ")
asignatura=opcion.lower()#pone todo a minuscula

if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
	print("asignatura elegida: " + asignatura)
else:
	print("la asignatura " + asignatura + " no existe.")
