#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font, messagebox

import sys

class Aplicacion():
    def __init__(self): 
        self.window = Tk()
        self.states = [] # Estados
        self.initial_state = ''
        self.final_states = []
        self.cont = 0
        self.titles = ['Estados', 'Estado inicial', 'Estados finales', 'Transiciones', 'Construcción AFD']
        self.etiquetas = ['Ingrese estado: ','Ingrese estado inicial: ','Ingrese estado final : ','Ingrese transición Estado,Simbolo: ']
        self.window.title(self.titles[self.cont])
        self.window.resizable(0,0)
        self.fuente = font.Font(weight='bold')
        self.frame = ttk.Frame(self.window, borderwidth=4,relief="raised", padding=(140,120))
        self.etiq_state = ttk.Label(self.frame, text=self.etiquetas[self.cont], font=self.fuente, padding=(5,5))
        self.etiq_msj = ttk.Label(self.frame, text="(Termina si no ingresa nada)", font=self.fuente, padding=(1,3))
        self.state = StringVar()
        self.input_state = ttk.Entry(self.frame, textvariable=self.state, width=30)
        self.separator = ttk.Separator(self.frame, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command=self.statesValid)
        self.WindowConf()
        self.window.mainloop()

    def secondFrame(self):
        del self.etiq_state
        del self.boton1
        
        self.etiq_state = ttk.Label(self.frame, text="Ingrese estado inicial", font=self.fuente, padding=(5,5))
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command=self.initialStateValid)
        self.window.title("Estado inicial")
        self.WindowConf()
        del self.etiq_msj
        
    #configurando posiciones de la ventana y sus componentes
    def WindowConf(self): 
        self.frame.grid(column=0, row=0)
        self.etiq_state.grid(column=0, row=1, columnspan = 1)
        self.etiq_msj.grid(column=0, row=2, columnspan = 1, pady = 15) 
        self.input_state.grid(column=0, row=3, pady = 10)
        self.boton1.grid(column=0, row=9, pady = 15) 
        self.input_state.focus_set()
    
    def initialStateValid(self):
        state, states = self.state, self.states 
        if state.get() not in states:
            messagebox.showerror("Error", "Estado inicial invalido")
        
        state.set("")
        self.input_state.focus_set()
    
    
    def statesValid(self):
        state = self.state
        if state.get() and not state.get().isspace():  #Validar ingreso  
            if state.get() in self.states:
                messagebox.showerror("Error", "Estado repetido")
            else:
                self.states.append(state.get().strip())

            print(self.states)
        else:
            self.secondFrame() 
            
        state.set("")
        self.input_state.focus_set()
        if len(self.states) == 0: sys.exit()
        return self.states    
      

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()