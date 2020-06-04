"""
i=1

while i<=10:
	print("ejecucion" + str(i))
	i=i+1

print("fin ejecucion")

"""
#programa para introducir una edad correcta con bucle while
"""
edad=int(input("introduce la edad: "))

while edad<5 or edad>100:
	print("edad incorrecta, vuelve a intentarlo")
	edad=int(input("introduce la edad: "))

print("edad correcta.")
print("edad del aspirante " + str(edad))

"""

#hayar raiz cuadrada de un numero.
import math

print("programa de calculo de raiz cuadrada")

numero=int(input("introduce un numero: "))
intentos=0

while numero<0:
	print("no se puede hayar la raiz de un nuemero negativo")
	if intentos==2:
		print("has consumidos demasiados intentos. programa finalizado")
		break
	numero=int(input("introduce un numero: "))

	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("solucion de " + str(numero)+ "es " + str(solucion))
