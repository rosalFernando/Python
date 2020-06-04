#bucle for
"""
for i in ["uno","dos","tres","cuatro"]:
	print(i)
	"""
contador=0
email=False
direccion=input("introduce una direccion de email: ")
"""
for i in ["voy","al gym", 3]:
	print("hola", end=" ")#argumento end separacion de impresion
"""
"""
for i in direccion:
	if i=="@" or i==".":
		contador=contador+1
if contador==2:
	print("email correcto")
else:
	print("email incorrecto")
"""
"""
for i in range(5,50,4):
	print(f"valor de la variable {i}")#notacion especial para concatenar

"""

for i in range(len(direccion)):
	if direccion[i]=="@":
		email=True

if email:
	print("email correcto")
else:
	print("email incorrecto")
