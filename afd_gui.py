#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font, messagebox

import sys

class Aplicacion():
    def __init__(self): 
        self.window = Tk()
        self.states = []  
        self.initial_state = ''
        self.final_states = []
        self.transitions = {}
        self.arrive_state = ''
        self.window.title("Estados")
        self.window.resizable(0,0)
        self.fuente = font.Font(weight='bold')
        self.frame = ttk.Frame(self.window, borderwidth=4,relief="raised", padding=(140,120))
        self.etiq_state = ttk.Label(self.frame, text="Ingrese estado: ", font=self.fuente, padding=(5,5))
        self.etiq_msj = ttk.Label(self.frame, text="", font=self.fuente, padding=(1,3))
        self.state = StringVar()
        self.input_state = ttk.Entry(self.frame, textvariable=self.state, width=30)
        self.separator = ttk.Separator(self.frame, orient=HORIZONTAL)
        self.input_state.bind('<Return>', self.statesValid)
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command = self.statesValid)
        self.WindowConf()
        self.window.mainloop()

    #Estado inicial
    def initialStateFrame(self, event):
        self.etiq_state.destroy
        self.boton1.destroy
        self.etiq_msj.destroy
        self.etiq_state = ttk.Label(self.frame, text="Ingrese estado inicial", font=self.fuente, padding=(5,5))
        self.etiq_msj = ttk.Label(self.frame, text="", font=self.fuente, padding=(1,3))
        self.input_state.bind('<Return>', self.initialStateValid)
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command = self.initialStateValid)
        self.window.title("Estado inicial")
        self.WindowConf()

    #Estados finales    
    def finalStatesFrame(self, event):
        self.state.set("") 
        self.etiq_state.destroy
        self.boton1.destroy
        self.etiq_state = ttk.Label(self.frame, text="Ingrese estado final", font=self.fuente, padding=(5,5))
        self.input_state.bind('<Return>', self.finalStatesValid)
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command=self.finalStatesValid)
        self.window.title("Estados finales")
        self.WindowConf()
    
    #Transiciones
    def transitionsFrame(self, event):
        self.state.set("") 
        self.etiq_state.destroy
        self.boton1.destroy
        self.etiq_state = ttk.Label(self.frame, text="Ingrese transición Estado, Simbolo: ", font=self.fuente, padding=(5,5))
        self.input_state.bind('<Return>', self.validTransitions)
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command=self.validTransitions)
        self.window.title("Transiciones")
        self.WindowConf()
    
    def arriveStateFrame(self, event):
        self.state.set("")
        self.etiq_state.destroy
        self.boton1.destroy
        self.etiq_state = ttk.Label(self.frame, text = "Ingrese Estado de llegada: ",  font=self.fuente, padding=(5,5))
        self.input_state.bind('<Return>', self.arriveStateValid)
        self.boton1 = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command=self.arriveStateValid)
        self.window.title("Estado de llegada")
        self.WindowConf()
    
    #configurando posiciones de la ventana y sus componentes
    def WindowConf(self): 
        self.frame.grid(column=0, row=0)
        self.etiq_state.grid(column=0, row=1, columnspan = 1)
        self.etiq_msj.grid(column=0, row=2, columnspan = 1, pady = 15) 
        self.input_state.grid(column=0, row=3, pady = 10)
        self.boton1.grid(column=0, row=9, pady = 15) 
        self.input_state.focus_set()
    
    
    def arriveStateValid(self, event):
        state = self.state
        if state.get() not in self.states:
            messagebox.showerror("Error", "Estado de llegada invalido")
            state.set("")
            self.input_state.focus_set()
    
        else:
            if tuple(self.arr_tupla) in self.transitions.keys():
                askbox = messagebox.askquestion('Reemplazo transición','Estado ya lleva esa transición a otro estado, Desea reemplazarla?',icon = 'warning')
                if askbox == 'yes':
                    self.arrive_state = state.get()
                    self.transitions[tuple(self.arr_tupla)] = self.arrive_state
                    print(self.transitions)
                
            else:
                self.arrive_state = state.get() 
                self.transitions[tuple(self.arr_tupla)] = self.arrive_state
                print(self.transitions)
            
            self.transitionsFrame(event)

    def validTransitions(self, event):
        tupla = self.state.get()
        if tupla:
            self.arr_tupla = [i.strip() for i in tupla.split(',') if i]
            if len(self.arr_tupla) != 2 or self.arr_tupla[0] not in self.states or self.arr_tupla[1] in self.states:
                messagebox.showerror("Error", "Transición invalida")
                self.state.set("")
                self.input_state.focus_set()
    
            else:
                self.arriveStateFrame(event)
                
        else:
            print("NUEVA VENTANA")    

    def finalStatesValid(self, event):
        state = self.state.get()
        if (state in self.states) and (state not in self.final_states): 
            self.final_states.append(state)
            print(self.final_states)
        else:
            if state == '' and len(self.final_states) > 0:
                return self.transitionsFrame(event)
            
            messagebox.showerror("Error", "Estado final invalido")
        
        self.state.set("")
        self.input_state.focus_set()

    
    def initialStateValid(self, event):
        state = self.state
        if state.get() not in self.states:
            messagebox.showerror("Error", "Estado inicial invalido")
            state.set("")
            self.input_state.focus_set()
        
        
        else:
            self.initial_state = state.get() 
            self.finalStatesFrame(event)
            
        

    
    def statesValid(self, event):
        state = self.state
        if state.get() and not state.get().isspace():  #Validar ingreso  
            if state.get() in self.states:
                messagebox.showerror("Error", "Estado repetido")
            else:
                self.states.append(state.get().strip())

            print(self.states)
        else:
            self.initialStateFrame(event) 
            
        state.set("")
        self.input_state.focus_set()
        if len(self.states) == 0: sys.exit()
     

def main():
      
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()