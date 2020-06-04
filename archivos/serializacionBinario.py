import pickle
"""
#escritura
listaNombres=["pedro","ana","maria","isabel"]

ficheroBinario=open("binario","wb")


#volcado de datos al archivo
pickle.dump(listaNombres,ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)
"""
#lectura
fichero=open("binario","rb")

lista=pickle.load(fichero)

print(lista)
fichero.close()