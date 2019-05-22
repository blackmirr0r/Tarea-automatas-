#AFD que desde usuario debe ingresar estado inicial 
#Estados finales, alfabeto y transiciones 
import sys 
from tkinter import * 


##############################################
#           Funciones de validación
##############################################

# Función validadora de estados 
def statesValid(s):
    states = [] 
    entr = input(s).strip()

    while entr and not(entr.isspace()):  #Validar ingreso  
        states.append(entr.strip()) 
        entr = input(s).strip()
        
        while entr in states:
            print("Estado repetido")
            entr = input(s).strip()
    
    return states 


#Función validadora de estados finales
def AcceptstatesValid(states, s):
    accept = []
    entr = input(s).strip()
    
    while True:
        if (entr in states) and (entr not in accept):
            accept.append(entr)
            
        
        else:
            if entr == '' and len(accept) > 0:
                return accept
            print("Estado final invalido")
        entr = input(s).strip()


###################################################################
#                   Ingreso de estados                            #
#   (Si no ingresa nada o solo espacios termina de ingresar)      #
###################################################################

states = statesValid("Ingrese estado (Termina si no ingresa nada): ") # lista de estados
if len(states) == 0: sys.exit()

##############################################
#           Estado inicial 
##############################################

init_state = input("Indique estado inicial: ")

while init_state not in states:
    print("Estado inicial invalido")
    init_state = input("Indique estado inicial: ").strip()

##############################################
#           Estados finales 
##############################################

accept_states = AcceptstatesValid(states, "Indique estado final (Termina si no ingresa nada): ")

print("\nEstados:  "+ " | ".join(states))
print("\nEstado inicial: ",init_state)
print("\nEstados finales: "+ " | ".join(accept_states)) if len(accept_states) > 1 else print("Estado final: "+" ".join(accept_states))
print()

##############################################
#           Transiciones  
##############################################

transitions = {} # diccionario de la forma (estado, simbolo): estado llegada 

tuple_trans = input("Ingrese par Estado, Simbolo (Termina si no ingresa nada): ")

while tuple_trans:
    tuple_trans = [i.strip(' ') for i in tuple_trans.split(',')] #entrada limpia de espacios para validar correctamente
    while len(tuple_trans) != 2 or tuple_trans[0] not in states:
        print("Entrada invalida")
        tuple_trans = input("Ingrese par Estado, Simbolo (Termina si no ingresa nada): ")
        tuple_trans = [i.strip(' ') for i in tuple_trans.split(',')]

    arrive_state = input("Ingrese Estado de llegada: ")
    while arrive_state not in states:
        print("Estado invalido")
        arrive_state = input("Ingrese Estado de llegada: ")

    #agregar clave - valor al diccionario 
    transitions[tuple(tuple_trans)] = arrive_state 
    print(transitions)
    print()   
    tuple_trans = input("Ingrese par Estado, Simbolo (Termina si no ingresa nada): ")
    
print()
pal = input("Ingrese la palabra a revisar: ")
estado_actual = init_state
for i in pal:
    if (estado_actual, i) in transitions.keys(): #revisa si existe una transición
        estado_actual = transitions[(estado_actual, i)]
    else:
        print("Palabra no aceptada")
        break
if estado_actual in accept_states:
    print("Palabra aceptada")
else:
    print("Palabra no aceptada")    


 
