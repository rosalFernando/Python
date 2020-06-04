from tkinter import *
from tkinter import messagebox

root=Tk()

#ventana emergente
def infoAdicional():
	messagebox.showinfo("Procesador de Fernando", "Procesador de textos version 2020.")


def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def avisoSalir():
	valor=messagebox.askokcancel("Salir","¿Deseas salir?")
	if valor==True:
		root.destroy()

def avisoCerrar():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar, documento bloqueado")
	if valor==False:
		root.destroy()


menu=Menu(root)
root.config(menu=menu, width=300,height=300)

archivoMenu=Menu(menu,tearoff=0)
archivoMenu.add_command(label="Nuevo...")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=avisoCerrar)
archivoMenu.add_command(label="Salir", command=avisoSalir)

archivoEdicion=Menu(menu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(menu,tearoff=0)
archivoAyuda=Menu(menu,tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)

menu.add_cascade(
	label="Archivo",
	menu=archivoMenu
	)
menu.add_cascade(
	label="Edicion",
	menu=archivoEdicion
	)
menu.add_cascade(
	label="Herramientas",
	menu=archivoHerramientas
	)
menu.add_cascade(
	label="Ayuda",
	menu=archivoAyuda
	)





root.mainloop()