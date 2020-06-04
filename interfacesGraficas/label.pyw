from tkinter import *

root=Tk()

miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miImagen=PhotoImage(file="image.png")
Label(miFrame,text="Hola mundo",fg="red",font=("Algerian",18)).place(x=100,y=200)
Label(miFrame,image=miImagen).place(x=200,y=200)
root.mainloop()