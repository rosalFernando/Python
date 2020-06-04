def divide():
	try:
		op1=float(input("Introduce el primer numero: "))
		op2=float(input("Introduce el segundo numero: "))

		print("la division es: "+ str(op1/op2))

	except ValueError:
		print("el valor introducido es erroneo")
	except ZeroDivisionError:
		print("no se puede dividir entre 0")
	finally:

		print("calculo finalizado.")


divide()