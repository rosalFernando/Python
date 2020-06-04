"""
sentencias Continue Pass Else para utilizar
en varios tipos de bucles.
"""

#continue: ingnora la linea siguiente y pasa a la siguiente vuelta de bucle
"""
for letra in "Python":
	if letra=="h":
		continue
	print("viendo la letra: " + letra)
	"""
"""
este programa ignora el espacio en blanco con el continue
y pasa a la siguiente interaccion de esa manera
solo cuenta letras y no espacios en blanco

nombre="pildoras informaticas"

contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1

print(contador) 
"""

#pass devuelve un valor nulo.
#else 

email=input("introduce un email: ")

for i in email:
	if i=="@":
		arroba=True
		break
else:
	arroba=False

print(arroba)