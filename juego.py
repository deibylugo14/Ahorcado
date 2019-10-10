from tkinter import *
import tkinter as tk
import random as rm
from nivelD import *

class juego (niveles):

    def __init__(self):
        self.ventanaPrincipal()

    def ventanaPrincipal(self):
        self.raiz =tk.Tk()#ventana principal
        #nombre tamaño y color
        self.raiz.title("juego ahorcado")
        self.raiz.geometry("625x409")
        self.raiz.configure(bg="deep sky blue2")
        #PLANTILLAS CANVAS DONDE SE Ejecutara el juego 
        self.canvas = Canvas(self.raiz,height=330,width=370,bg='light blue')#recuadro que apareceen el medio
        self.canvas.create_line(100,50,100,230,tags="Linea") #Vertical de la base de la soga
        self.canvas.create_line(100,50,150,50,tags="Linea") #linea horizontal
        self.canvas.create_rectangle(0,370,375,236,fill="sea green2")
        self.canvas1 = Canvas(self.raiz,height=30,width=370,bg='cadet blue2')#recuadro donde aparce "ADIVIDA LA PALABRA"
        self.canvas1.pack()
        self.canvas.pack()
        self.label2 = Label(self.raiz, text="¡ADIVINA LA PALABRA!", bg="light blue3",font= 59)
        self.label2.place(x=225, y=6,)
        #boton comenzar con su nombre comando(llama al tipo lvl) y color asignado
        self.boton= tk.Button(self.raiz,text="!!JUGAR!!",command=self.dificultad,bg="tan1")
        self.boton.place(x=10, y=100, width=100, height=30)#ordena en un lugar espesifico de la pantalla el boton jugar
        #boton sali del juego con su configuraciones(ubicacion color tamaño)
        self.boton2= tk.Button(self.raiz,text="!!SALIR!!",command=quit,bg="tan2")
        self.boton2.place(x=10, y=240, width=100, height=30)

ventaJ = juego()


