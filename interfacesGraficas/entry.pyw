from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,padx=10,pady=10)
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

nombreLabel=Label(miFrame,text="nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)
apellidoLabel=Label(miFrame,text="apellido:",)
apellidoLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)
direccionLabel=Label(miFrame,text="direccion de casa:")
direccionLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)
passLabel=Label(miFrame,text="contraseña:")
passLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)



raiz.mainloop()