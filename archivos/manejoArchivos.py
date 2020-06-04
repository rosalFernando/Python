from io import open


"""
#escritura
archivoTexto=open("archivo.txt","w")
frase="prueba de escritura en archivo \n de python"

archivoTexto.write(frase)

archivoTexto.close()
"""
"""
#lectura
archivoTexto=open("archivo.txt","r")
texto=archivoTexto.read()

archivoTexto.close()

print(texto)
"""

"""
#guarda informacion en una variable
archivoTexto=open("archivo.txt","r")
lineasTexto=archivoTexto.readlines()
archivoTexto.close()
print(lineasTexto)
print(lineasTexto[0])
print(lineasTexto[1])
"""
"""
#añadir informacion
archivoTexto=open("archivo.txt","a")
archivoTexto.write("\n nueva linea de texto añadida")
archivoTexto.close()
"""

#serializacion puntero
archivoTexto=open("archivo.txt","r+") #lectura y escritura

#seek inicia la lectura a partir del numero de caracter que se le dice
#archivoTexto.seek(11)
"""
al aladir un numero al read() se lee hasta ese numero de caracter
print(archivoTexto.read(11))
"""
"""
#colocar puntero a la mitad del texto
archivoTexto.seek(len(archivoTexto.read())/2)

print(archivoTexto.read())
"""
"""
#modificar archivo
listaTexto=archivoTexto.readlines()

listaTexto[1]="esta linea ha sido incluida desde el exterior \n"

archivoTexto.seek(0)

archivoTexto.writelines(listaTexto)
archivoTexto.close()
"""
