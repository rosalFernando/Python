from tkinter import *

#construye raiz de ventana
raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)#permite o no redimensionar ventana. valores 1 o 0, true o false
raiz.iconbitmap("icono.ico")#icono de ventana
#raiz.geometry("650x350")#tamaño de ventana

raiz.config(bg="blue")

miFrame=Frame()#creacion de frame
miFrame.pack()#empaquetado

miFrame.config(bg="red")
miFrame.config(width="650",height="350")#se da tamaño al frame y la raiz se adapta
miFrame.config(bd="35")
miFrame.config(relief="groove")
miFrame.config(cursor="pirate")
raiz.mainloop()#siempre en ultimo lugar