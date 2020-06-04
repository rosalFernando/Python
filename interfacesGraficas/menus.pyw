from tkinter import *

root=Tk()

menu=Menu(root)
root.config(menu=menu, width=300,height=300)

archivoMenu=Menu(menu,tearoff=0)
archivoMenu.add_command(label="Nuevo...")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(menu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(menu,tearoff=0)
archivoAyuda=Menu(menu,tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

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