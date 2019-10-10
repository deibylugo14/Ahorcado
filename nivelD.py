from tkinter import *
import tkinter as tk
import random as rm
from offAhorcado import *

class niveles (comienzo):
    
    def dificultad(self):#encuentranlos botones de dificultad con surespectivo color tamaño y pocision
        #botones de elegir l nivel de complejidad de la palabra ("facil""medio""dificil")
        self.botonF = tk.Button(self.raiz,text=" FACIL ",command=self.facil_L,bg="seagreen1")
        self.botonF.place(x=10, y=135, width=100, height=30)#configuracion de tamaño ubicasion de FACIL
        self.botonM = tk.Button(self.raiz,text=" MEDIO ",command=self.medio_L,bg="seagreen2")
        self.botonM.place(x=10, y=170, width=100, height=30)#configuracion de tamaño ubicasion de MEDIO
        self.botonD = tk.Button(self.raiz,text="DIFICIL",command=self.dificil_L,bg="seagreen3")
        self.botonD.place(x=10, y=205, width=100, height=30)#configuracion de tamaño ubicasion de DIFICIL
        #self.enviar= tk.Button(self.canvas,text="Enviar",command=self.cabeza,bg="light salmon4")
        #self.enviar.place(x=115, y=240, width=150, height=30)       
        
    def facil_L (self):
        self.palabra = ["METODO","CLASE","OBJETO","GRUPO","JAVA","SCRIPT","CANVAS"]#palabras a adivinar
        self.lista = rm.choice(self.palabra)#hace que muestrre una palabra aleatoria
        self.inicioJuego(self.lista.lower())

    def medio_L (self):
        self.palabraM = ["PROGRAMACION","INTERNET","ARCHIVO","VARIABLE","DICCIONARIO"]
        self.listaM = rm.choice(self.palabraM)
        self.inicioJuego(self.listaM.lower())

    def dificil_L (self):
        self.palabraD = ["DIDACTICO","DILATACIONES","OVOVIVIPARO","ORNITORRINCO","ESTRUCTURADO","ELECTROENCEFALOGRAMA"]
        self.listaD = rm.choice(self.palabraD)
        self.inicioJuego(self.listaD.lower())
        
        
    def inicioJuego (self,listas):
        self.listaP = listas
        for i in range(0, len(self.listaP)):
            self.canvas.create_text(10+20*i,16,text =" _ ",font= 12,tags="text")
            
        self.texto = StringVar()
        self.resultado = Entry(self.raiz, textvariable = self.texto)
        self.enviar= tk.Button(self.raiz,text="Enviar",command=self.adivinarP,bg="green2")
        self.enviar.pack(side=BOTTOM)
        self.resultado.pack(side=BOTTOM)
        self.vida = int(0)
        self.fallas = 0
