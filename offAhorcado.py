from tkinter import *

class comienzo :
    
    def adivinarP (self):
        palabraA = self.texto.get()
        fallas = 0
        vidas = 0
        for i in range (0,len(self.listaP)):
            if palabraA == self.listaP[i]:
                self.canvas.create_text(10+20*i,15,text=self.listaP[i],font=12,tags="text")
                fallas += 1
                self.vida += 1
            if self.vida == len(self.listaP):
                self.ganaste()
        if not (fallas > vidas):
           self.perdiste()
           vidas=0 
           fallas
           
    def ganaste (self):   
        self.label3 = Label(self.raiz, text="¡FELICIDADES HAS GANADO!", bg="khaki1",font=24)
        self.label3.place(x=126, y=35,width=370, height=330)
    
    def perdiste (self):
    
        self.fallas += 1
        if self.fallas == 1 :
            self.canvas.create_oval(143,51,180,85,fill="navajo white")#cabeza
        elif self.fallas == 2 :  
            self.canvas.create_line(160,86,160,189,tags="Linea")#cuerpo
        elif  self.fallas == 3:
            self.canvas.create_line(161,95,190,150,tags="Linea")#brazo izquierdo
        elif self.fallas == 4:
            self.canvas.create_line(159,95,137,150,tags="Linea")#brazo derecho
        elif self.fallas == 5:
            self.canvas.create_line(161,155,184,189,tags="Linea")#otro pie
        elif self.fallas == 6 : 
            self.label3 = Label(self.raiz, text="¡ X_X AHORCADO X_X !", bg="salmon",font=74)
            self.label3.place(x=126, y=35,width=370, height=330)
            self.enviar.destroy()
            self.resultado.destroy()
