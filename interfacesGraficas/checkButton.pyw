from tkinter import *

root=Tk()
root.title("ejemplo")

playa=IntVar()
montania=IntVar()
turismoRural=IntVar()

def opcionesViaje():
	opcionEscogida=""

	if playa.get()==1:
		opcionEscogida+=" playa"
	if montania.get()==1:
		opcionEscogida+=" montaña"
	if turismoRural.get()==1:
		opcionEscogida+=" rutismo Rural"
	textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="descarga.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="elige destinos", width=50).pack()

Checkbutton(frame,text="playa",variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text="montaña",variable=montania,onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text="turismo rural",variable=turismoRural,onvalue=1, offvalue=0, command=opcionesViaje).pack()


textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()