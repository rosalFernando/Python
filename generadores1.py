"""
el generador devuelve solo un valor y cada vez que se llama
añade otro valor a la lista, asi que para imprimir valores concretos
debemos usar next para que vuelva a llamar al generador y devuelva el siguiente valor
"""
def generaPares(limite):
	num=1


	while num < limite:
		yield num*2
		num+=1

devuelvePares=generaPares(10)

print(next(devuelvePares))

print("aqui podria ir mas codigo")

print(next(devuelvePares))
print("aqui podria ir mas codigo")

print(next(devuelvePares))