from tkinter import *
import tkinter as tk
from juego import *


class menu (juego):

    def __init__(self):
        self.setVentanaPrincipal()

    def setVentanaPrincipal(self):
        self.menuP =tk.Tk()#ventana principalventanamenuP= juego()
        #nombre tamaño y color
        self.menuP.title("juego ahorcado")
        self.menuP.geometry("500x400")
        self.menuP.configure(bg="dark slategray1")
        #boton comenzar con su nombre comando(llama al tipo lvl) y color asignado
        self.boton= tk.Button(self.menuP,text="COMENZAR",command=self.ventanaPrincipal,bg="salmon1")
        self.boton.place(x=150, y=50, width=200, height=50)#ordena en un lugar espesifico de la pantalla el boton COMENZAR
        
        self.botonS= tk.Button(self.menuP,text="AUTORES",command=self.datos,bg="salmon1")
        self.botonS.place(x=150, y=110, width=200, height=50)

        self.botonS= tk.Button(self.menuP,text="SALIR",command=quit,bg="salmon1")
        self.botonS.place(x=150, y=170, width=200, height=50)

    def datos (self):
        self.label2 = Label(self.menuP, text="Autores Del Juego", bg="white",font= 59)
        self.label2.place(x=50, y=270,)
        self.label2 = Label(self.menuP, text="* Juan Pablo Corredor Serrano", bg="white",font= 59)
        self.label2.place(x=50, y=300,)
        self.label2 = Label(self.menuP, text="* Luis Miguel Garcia", bg="white",font= 59)
        self.label2.place(x=50, y=330,)
        self.label2 = Label(self.menuP, text="* Deiby Lugo", bg="white",font= 59)
        self.label2.place(x=50, y=360,)
    def getMenu(self):
        return self.menuP 

ventanaP= menu()
menuI = ventanaP.getMenu()
menuI.mainloop()