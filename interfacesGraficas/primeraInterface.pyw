from tkinter import *

#construye raiz de ventana
raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)#permite o no redimensionar ventana. valores 1 o 0, true o false
raiz.iconbitmap("icono.ico")#icono de ventana
raiz.geometry("650x350")#tamaño de ventana

raiz.config(bg="blue")
raiz.mainloop()#siempre en ultimo lugar