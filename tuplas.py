nombreTupla=("juan",1,34,4)
nombreLista=["lajrf",3,5,6]
print(nombreTupla[2])

#combierte tupla en lista
milista=list(nombreTupla)

#convertir lista en tupla
mitupla=tuple(nombreLista)


print(milista)
print(mitupla)
#saber si un elemento esta en una tupla
print(3 in mitupla)

#contar numero de veces que se
#encientra un elemente en la tupla
print(mitupla.count(5))

#saber longitud de tupla
print(len(mitupla))

#tupla sin parentesis
mitupla2="juan",3,4,5
print(mitupla2)

#desempaquetar tupla
nombre,num1,num2,num3=mitupla2

print(nombre)
print(num3)
