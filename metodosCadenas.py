edad=input("Introduce la edad: ")

while edad.isdigit()==False:
	print("introduce valor numerico")
	edad=input("Introduce la edad: ")

if int(edad)<18:
	print("no puede pasar")


else:
	print("puede pasar")
