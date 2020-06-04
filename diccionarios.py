#diccionarios.

midiccionario={
	"alemania":"berlin",
	"francia":"paris",
	"españa":"madrid",
	"portugal":"lisboa"
}

#añade clave valor
midiccionario["italia"]="budapest"

#valor de un diccionario por la clave
print(midiccionario["españa"])
print(midiccionario)

#cambia valor de clave
midiccionario["italia"]="roma"
print(midiccionario)

#eliminar elemento
del midiccionario["portugal"]
print(midiccionario)

midiccionario2={
	"alemania":"berlin",
	23:"jordan",
	"mosqueteros":3
}

print(midiccionario2)
#rellenar diccionario desde tupla
mitupla=["españa","francia","italia","alemania"]
midiccionario3={
	mitupla[0]:"madrid",
	mitupla[1]:"paris",
	mitupla[2]:"roma",
	mitupla[3]:"berlin"
}

print(midiccionario3)

#almacenar tupla en diccionario
midiccionario4={23:"jordan","nombre":"michael","equipo":"chicago", "anillos":[1991,1992,1993,1994]}

print(midiccionario4)

#almnacenar diccionario en diccionario
midiccionario4={23:"jordan","nombre":"michael","equipo":"chicago", "anillos":{"temporadas":[1991,1992,1993,1994]}}

print(midiccionario4["anillos"])

#imprime llaves
print(midiccionario4.keys())
#imprime valores
print(midiccionario.values())

#dice tamaño de diccionario
print(len(midiccionario))