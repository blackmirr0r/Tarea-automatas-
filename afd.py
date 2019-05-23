#AFD que desde usuario debe ingresar estado inicial 
#Estados finales, alfabeto y transiciones 
import sys 
from tkinter import *  #LIBRERIA AUN NO USADA


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


#funcion que devuelve simbolos que no estan en el ALFABETO
def notInAlphabetSymbols(pal, alphabet):
    pal = sorted(set("".join(pal)))
    not_in_alphabet = [symbol for symbol in pal if symbol not in alphabet]
    return " - ".join(not_in_alphabet)

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

#string estado, simbolo que luego será tupla 
tupla = input("Ingrese par Estado, Simbolo (Termina si no ingresa nada): ")

while tupla:
    #arreglo de string tupla para eliminar caracteres indeseados
    arr_tupla = [i.strip() for i in tupla.split(',') if i] 
    
    #verifica si arr_tupla es de la forma estado,simbolo
    while len(arr_tupla) != 2 or arr_tupla[0] not in states or arr_tupla[1] in states:
        print("Entrada invalida")
        tupla = input("Ingrese par Estado, Simbolo (Termina si no ingresa nada): ")
        arr_tupla = [i.strip(' ') for i in tupla.split(',')]
        if not(tupla): break
        
    if not(tupla): break

    #Estado de llegada 
    arrive_state = input("Ingrese Estado de llegada: ")
    while arrive_state not in states:
        print("Estado invalido")
        arrive_state = input("Ingrese Estado de llegada: ")

    #agregar clave - valor al diccionario 
    transitions[tuple(arr_tupla)] = arrive_state 
    print(transitions)
    print()   
    tupla = input("Ingrese par Estado, Simbolo (Termina si no ingresa nada): ")
    
print()


######################################################################
#          Construcción Alfabeto y Verificación de Aceptacion AFD
######################################################################

#construir alfabeto en base a simbolos ingresados en transiciones
alphabet = [symbol[1] for symbol in transitions.keys()]

pal = input("Ingrese la palabra a revisar: ")

#NO SE SI SE PUEDE INGRESAR NADA PERO SI SE PUEDE COMENTEN EL WHILE
while not(pal):
    pal = input("Ingrese la palabra a revisar: ")

estado_actual = init_state 
#revisa si cada simbolo de la palabra existe en alfabeto
word_accepted = all(elem in alphabet for elem in set(pal)) 

if word_accepted:
    for i in pal:
        if (estado_actual, i) in transitions.keys(): #revisa si existe una transición
            estado_actual = transitions[(estado_actual, i)]
        else:
            print("Palabra no aceptada")
            break
    
    if estado_actual in accept_states:
        print("Palabra aceptada")
    
else:
    #funcion para filtrar elementos que no estan en alfabeto
    not_alphabet = notInAlphabetSymbols(pal, alphabet)
    print("Palabra no aceptada ya que los simbolos ( "+ not_alphabet+" ) no existen en el alfabeto del AFD")
 
  
