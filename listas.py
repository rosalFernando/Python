miLista=["maria","pepe","marta","antonio"]

print(miLista[:])
print(miLista[-1])
print(miLista[0:2])

miLista.insert(2,"yo")
miLista.append("yo al final")
miLista.extend([1,2,3,4])

print(miLista[:])
print(miLista.index("pepe"))
print("pepe" in miLista)
print("matao" in miLista)

miLista.remove(2)
print(miLista[:])

miLista2=["lista","añadida"] * 3

miLista3=miLista+miLista2

print(miLista3[:])