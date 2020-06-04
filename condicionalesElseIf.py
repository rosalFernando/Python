print("Verificacion de acceso")

nota=int(input("introduce tu nota: "))


if nota<5:
	print("insuficiente")

elif nota<6:
	print("suficiente")
elif nota<7:
	print("bien")
elif nota<9:
	print("notable")

else:
	print("sobresaliente")