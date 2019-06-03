#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk, font, messagebox
import sys

class Window():
    def __init__(self): 
        self.window = Tk()
        self.states = []  
        self.initial_state = ''
        self.final_states = []
        self.transitions = {}
        self.colours =['#A500FD','#101010']
        self.style = ttk.Style()
        self.style.configure('colorFondo.TFrame', background='#202020')
        self.style.configure('colorAceptado.TFrame', background='#0DD400')
        self.style.configure('colorRechazado.TFrame', background='#F20505')  #49F52B
        self.style.configure('color.TLabel', background='#202020', foreground='#FFFFFF')
        self.style.configure('labelAceptado.TLabel', background='#0DD400', foreground='#000000')
        self.style.configure('labelRechazado.TLabel', background='#F20505', foreground='#000000')
        self.window.title("Transiciones")
        self.window.resizable(0,0)
        self.fuente = font.Font(weight='bold')
        self.transitionsFrame()
        self.window.mainloop()

    def transitionsFrame(self):
        self.frame = ttk.Frame(self.window, borderwidth=4,padding=(140,120), style='colorFondo.TFrame')
        self.etiq_state = ttk.Label(self.frame, text="Ingrese transición de la forma: estado, simbolo, estado llegada", font=self.fuente, padding=(5,5), style='color.TLabel')
        self.etiq_msj = ttk.Label(self.frame, text="( Termina de ingresar dejando texto en blanco )", font='Helvetica', padding=(5,5), style='color.TLabel')
        self.state = StringVar()
        self.input_state = ttk.Entry(self.frame, textvariable=self.state, width=30)
        self.boton = ttk.Button(self.frame, text="Aceptar", padding=(5,5), command = self.validTransitions)
        self.WindowConf(self.frame)
        
    #Estado inicial
    def initialStateFrame(self):
        self.frame.destroy()
        self.frameInitialState = ttk.Frame(self.window, borderwidth=4, padding=(140,120),style='colorFondo.TFrame' )
        self.etiq_state = ttk.Label(self.frameInitialState, text="Ingrese estado inicial", font=self.fuente, padding=(5,5), style='color.TLabel')
        self.etiq_msj = ttk.Label(self.frameInitialState, text="", font='Helvetica', padding=(5,5), style='color.TLabel')
        self.boton = ttk.Button(self.frameInitialState, text="Aceptar", padding=(5,5), command = self.initialStateValid)
        self.input_state = ttk.Entry(self.frameInitialState, textvariable=self.state, width=30)
        self.window.title("Estado inicial")
        self.windowConf3(self.frameInitialState)
    
    
    #Estados finales    
    def finalStatesFrame(self):
        self.frameInitialState.destroy()
        self.frameFinalState = ttk.Frame(self.window, borderwidth=4, padding=(140,120), style='colorFondo.TFrame')
        self.etiq_state = ttk.Label(self.frameFinalState, text="Ingrese estado final:", font=self.fuente, padding=(5,5), style='color.TLabel')
        self.etiq_msj = ttk.Label(self.frameFinalState, text="( Termina de ingresar dejando texto en blanco )", font='Helvetica', padding=(5,5), style='color.TLabel')
        self.boton = ttk.Button(self.frameFinalState, text="Aceptar", padding=(5,5), command = self.finalStatesValid)
        self.input_state = ttk.Entry(self.frameFinalState, textvariable=self.state, width=30)
        self.window.title("Estados Finales")
        self.WindowConf(self.frameFinalState)
    
    
        
    def wordAcceptedFrame(self):
        self.state.set("")
        self.frameFinalState.destroy()
        self.frameTransitions = ttk.Frame(self.window, borderwidth=4, padding=(90,80), style='colorFondo.TFrame')
        self.frameWord = ttk.Frame(self.window, borderwidth=4, padding=(90,294), style='colorFondo.TFrame')
        self.etiq_transition = ttk.Label(self.frameTransitions, text="Transiciones", font=self.fuente, style='color.TLabel')
        self.item1 = StringVar()
        self.item2 = StringVar()
        self.item3 = StringVar()    
        self.canvas = Canvas(self.frameTransitions, width=150, height=530)
        for index, item in enumerate(self.transitions.keys()): 
            self.item1.set(item[0])
            self.item2.set(item[1]) 
            self.item3.set(self.transitions[item])
            self.canvas.create_text(50,10+(index*15),text =('δ('+self.item1.get()+','+self.item2.get()+') = '+self.item3.get()))
         
        

        self.etiq_state = ttk.Label(self.frameWord, text="Ingrese palabra:", font=self.fuente,  style ='color.TLabel')
        self.boton = ttk.Button(self.frameWord, text="Verificar", command = self.verificateWord)
        self.input_state = ttk.Entry(self.frameWord, textvariable=self.state, width=30)
        self.window.title("Ingreso de palabra")
        self.wordWindow(self.frameTransitions, self.frameWord)
    
    def otherWord1(self):
        self.acceptedFrame.destroy()
        return self.wordAcceptedFrame()
    
    def otherWord2(self):
        self.rejectedFrame.destroy()
        return self.wordAcceptedFrame()
    
    def acceptedWindow(self):
        self.frameTransitions.destroy()
        self.frameWord.destroy()
        self.acceptedFrame = ttk.Frame(self.window, borderwidth=4, padding=(140,120), style ='colorAceptado.TFrame')
        self.etiq_state = ttk.Label(self.acceptedFrame, text="Palabra aceptada!", font=self.fuente, padding=(5,5), style ='labelAceptado.TLabel')
        self.botonVolver = ttk.Button(self.acceptedFrame, text="Ingresar otra palabra", command = self.otherWord1)
        self.botonTerminar = ttk.Button(self.acceptedFrame, text="Salir", command = self.window.destroy)
        self.window.title("Palabra aceptada")
        self.windowConf2(self.acceptedFrame)
    
    def rejectedWindow(self):
        self.frameTransitions.destroy()
        self.frameWord.destroy()
        self.rejectedFrame = ttk.Frame(self.window, borderwidth=4, padding=(140,120), style ='colorRechazado.TFrame')
        self.etiq_state = ttk.Label(self.rejectedFrame, text="Palabra Rechazada!", font=self.fuente, padding=(5,5), style ='labelRechazado.TLabel')
        self.botonVolver = ttk.Button(self.rejectedFrame, text="Ingresar otra palabra", command = self.otherWord2)
        self.botonTerminar = ttk.Button(self.rejectedFrame, text="Salir", command = self.window.destroy)
        self.window.title("Palabra rechazada")
        self.windowConf2(self.rejectedFrame)
    
    def windowConf2(self, frame):
        frame.grid(column=0, row=0)
        self.etiq_state.grid(column=0, row=0,pady=10)
        self.botonVolver.grid(column=0, row=3, pady=10)
        self.botonTerminar.grid(column=1, row=3, pady=10)
        
        
    def verificateWord(self):
        self.flag = True
        state = self.state
        self.estado_actual = self.initial_state 
        
        #revisa si cada simbolo de la palabra existe en alfabeto
        self.word_accepted = all(elem in self.alphabet for elem in set(state.get())) 
        
        if not(state.get()):
            self.acceptedWindow() if self.estado_actual in self.final_states else self.rejectedWindow()
        
        else:
            if self.word_accepted:
                for symbol in state.get():
                    if (self.estado_actual, symbol) in self.transitions.keys(): #revisa si existe una transición
                        self.estado_actual = self.transitions[(self.estado_actual, symbol)]
                        
                    else:
                        self.flag = False  
                        break               
            
            
                if self.flag and self.estado_actual in self.final_states:
                    self.acceptedWindow()
                
                else:
                    self.rejectedWindow()
                
            else:
                #funcion para filtrar elementos que no estan en alfabeto
                #not_alphabet = notInAlphabetSymbols(pal, alphabet)
                #print("Palabra no aceptada ya que los simbolos ( "+ not_alphabet+" ) no existen en el alfabeto del AFD")    
                self.rejectedWindow()

    def constructionAFD(self):
        self.input_states = [state[0] for state in list(self.transitions.keys())]
        self.output_states = [state for state in self.transitions.values()]
        self.alphabet = sorted(set([state[1] for state in list(self.transitions.keys())]))
        return sorted(set(self.input_states + self.output_states))
    
    def WindowConf(self, frame): 
        frame.grid(column=0, row=0)
        self.etiq_state.grid(column=0, row=1, columnspan = 1)
        self.input_state.grid(column=0, row=3, pady = 4)
        self.etiq_msj.grid(column=0, row=2, pady = 4)
        self.boton.grid(column=0, row=9, pady =4) 
        self.input_state.focus_set()
    
    def wordWindow(self, frame1, frame2):
        frame1.grid(column = 0, row = 0)
        frame2.grid(column = 1, row= 0)
        self.etiq_transition.grid(column=0, row=0,pady = 14)
        self.canvas.grid(column=0, row=1, padx = 5)
        self.etiq_state.grid(column=1, row=0, padx = 6,pady = 14)
        self.input_state.grid(column=1, row=1, padx = 6,pady = 14)
        self.boton.grid(column=1, row=2, padx = 6,pady = 14) 
        self.input_state.focus_set()
    
    def windowConf3(self, frame):
        frame.grid(column=0, row=0)
        self.etiq_state.grid(column=0, row=1, columnspan = 1)
        self.input_state.grid(column=0, row=3, pady = 4)
        self.boton.grid(column=0, row=9, pady =4) 
        self.input_state.focus_set()
    
    def validTransitions(self):
        trans = self.state
        if not(trans.get()) and len(self.transitions) == 0:
            askbox = messagebox.askquestion('','No ingresó transiciones, desea salir?',icon = 'warning')
            if askbox == 'yes':
                sys.exit()
            else:
                return self.transitionsFrame()        
        if trans.get():
            self.separate_trans = [elem.strip() for elem in trans.get().split(',') if elem and not(elem.isspace())]
            
            if len(self.separate_trans) != 3 or len(self.separate_trans[1]) > 1:
                messagebox.showerror("Error", "Transición invalida")
                self.state.set("")
                self.input_state.focus_set()
    
            else:
                self.actual_state, self.symbol, self.arrive_state = self.separate_trans[0], self.separate_trans[1], self.separate_trans[2]
                if (self.actual_state, self.symbol) in self.transitions.keys():
                    askbox = messagebox.askquestion('Reemplazo transición','Estado ya lleva esa transición a otro estado, Desea reemplazarla?',icon = 'warning')
                    if askbox == 'yes':
                        self.transitions[(self.actual_state, self.symbol)] = self.arrive_state
                    
                        
                else:
                    self.transitions[(self.actual_state, self.symbol)] = self.arrive_state
                    
                
                trans.set("")
                self.input_state.focus_set()
        else:
            self.states = self.constructionAFD()
            return self.initialStateFrame()    

     
    def finalStatesValid(self):
        state = self.state.get()
        if (state in self.states) and (state not in self.final_states): 
                self.final_states.append(state)
                
        else:
                
            if state == '' and len(self.final_states) > 0:
                return self.wordAcceptedFrame()
            
            elif len(state) != 0:
                messagebox.showerror("Error", "Estado final invalido")
            
            else:
                messagebox.showerror("Error", "Debe ingresar al menos un estado final")
            
            
            
        self.state.set("")
        self.input_state.focus_set()


    def initialStateValid(self):
        state = self.state
        if state.get() not in self.states:
            if state.get() != '':
                messagebox.showerror("Error", "Estado inicial invalido")
            else:
                messagebox.showerror("Error", "Debe ingresar un estado inicial")
            state.set("")
            self.input_state.focus_set()
        
        else:
            self.initial_state = state.get()
            state.set("")
            self.input_state.focus_set()
            self.finalStatesFrame()
            
def main():
    window = Window()

if __name__ == '__main__':
    main()
