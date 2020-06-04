"""
def areaTriangulo(base,altura):
	return (base*altura)/2

print(areaTriangulo(5,7))

triangulo1=areaTriangulo(5,7)
triangulo2=areaTriangulo(4,5)
"""
area_triangulo=lambda base,altura:(base*altura)/2

print(area_triangulo(3,5))

destacarValor=lambda comision:"¡{}! €".format(comision)

comisionYo=12346
print(destacarValor(comisionYo))
