import sys 

# Función validadora de estados finales 
def acceptStatesValid(states, s):
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


def showTransitions(transitions):
    for trans in transitions.keys():
        print('d('+trans[0]+','+trans[1]+') = '+transitions[trans])
        

#Diccionario que almacena transiciones
transitions = {} 

trans = input("Ingrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
if not(trans):
    exit = input("No ingresó transiciones, Desea salir? (S / n)") # Si usuario no ingresa nada entonces el programa acaba 
    if exit in ('S', 's'): sys.exit()
    else:
        trans = input("Ingrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
        

while trans: 
    separate_trans = [elem.strip() for elem in trans.split(',') if elem and not(elem.isspace())]
    
    while len(separate_trans) != 3 or len(separate_trans[1]) > 1:
        print("Transición invalida")
        trans = input("\nIngrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
        separate_trans = [elem.strip() for elem in trans.split(',') if elem and not(elem.isspace())]
    
    actual_state, symbol, arrive_state = separate_trans[0], separate_trans[1], separate_trans[2]
    #Para validar que Autómata no sea AFND
    if (actual_state, symbol) in transitions.keys():
        
        option = input("\nEstado ya lleva esa transición a otro estado... Desea reemplazarla? (S | N): ")
        if option in ('S','s'):
            transitions[(actual_state, symbol)] = arrive_state  

    else:
        transitions[(actual_state, symbol)] = arrive_state

    trans = input("\nIngrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
    

#Estados 
input_states = [state[0] for state in list(transitions.keys())]
output_states = [state for state in transitions.values()]
states = list(set(input_states + output_states))

#Alfabeto
alphabet = list(set([state[1] for state in list(transitions.keys())]))

initial_state = input("\nIngrese estado inicial: ")

while initial_state not in states:
    print("Estado inicial invalido")
    initial_state = input("\nIngrese estado inicial: ")


#Estados finales
accept_states = acceptStatesValid(states, "Ingrese estado final (Termina si no ingresa nada): ")


showTransitions(transitions)

#Ingreso de palabra y se analiza si ésta es aceptada o rechazada 
while True:
    flag = True
    pal = input("Ingrese la palabra a revisar: ")
    estado_actual = initial_state 
    
    #revisa si cada simbolo de la palabra existe en alfabeto
    word_accepted = all(elem in alphabet for elem in set(pal)) 
    
    if not(pal):
        print("Palabra aceptada") if estado_actual in accept_states else print("Palabra no aceptada")
    
    else:
        if word_accepted:
            for symbol in pal:
                if (estado_actual, symbol) in transitions.keys(): 
                    estado_actual = transitions[(estado_actual, symbol)]
                    
                else:
               	    flag = False  
               	    break               
        
        
            if flag and estado_actual in accept_states:
                print("Palabra aceptada")
            
            else:
                print("Palabra no aceptada")
            
        else:
           
            print("Palabra no aceptada")    
