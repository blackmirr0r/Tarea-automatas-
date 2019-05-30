import sys 


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


def notInAlphabetSymbols(pal, alphabet):
    pal = sorted(set("".join(pal)))
    not_in_alphabet = [symbol for symbol in pal if symbol not in alphabet]
    return " - ".join(not_in_alphabet)

###############################################
#           Ingreso transiciones
###############################################

transitions = {} 

trans = input("Ingrese transición de la forma (e_actual, simbolo, e_llegada): ").strip()
if not(trans): sys.exit()

while trans: 
    separate_trans = [elem.strip() for elem in trans.split(',') if elem and not(elem.isspace())]
    
    while len(separate_trans) != 3:
        print("Transición invalida")
        trans = input("Ingrese transición de la forma (e_actual, simbolo, e_llegada): ").strip()
        separate_trans = [elem.strip() for elem in trans.split(',') if elem]
    
    actual_state, symbol, arrive_state = separate_trans[0], separate_trans[1], separate_trans[2]
    if (actual_state, symbol) in transitions.keys():
        option = input("\nEstado ya lleva esa transición a otro estado... Desea reemplazarla? (S | N): ")
        if option in ('S','s'):
            transitions[(actual_state, symbol)] = arrive_state
    else:
        transitions[(actual_state, symbol)] = arrive_state

    
    print(transitions)
    trans = input("Ingrese transición de la forma (e_actual, simbolo, e_llegada): ").strip()
    

###############################################
#           Recolección de datos
###############################################

input_states = [state[0] for state in list(transitions.keys())]

output_states = [state for state in transitions.values()]

alphabet = sorted(set([state[1] for state in list(transitions.keys())]))
print("Alfabeto\n", alphabet)

states = sorted(set(input_states + output_states))
print("Estados\n", states)

###############################################
#           Estado inicial y Estados finales 
###############################################
print("----------------------------------------------------\n")
initial_state = input("\nIngrese estado inicial: ")

while initial_state not in states:
    print("Estado inicial invalido")
    initial_state = input("\nIngrese estado inicial: ")

accept_states = acceptStatesValid(states, "Ingrese estado final (Termina si no ingresa nada): ")
print(initial_state)
print(accept_states)

###############################################
#          Verificación de aceptación AFD 
###############################################

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
            for index, symbol in enumerate(pal):
                if (estado_actual, symbol) in transitions.keys(): #revisa si existe una transición
                    estado_actual = transitions[(estado_actual, symbol)]
                    
                else:
               	    flag = False  
               	    break               
        
        
            if flag and estado_actual in accept_states:
                print("Palabra aceptada")
            else:
                print("Palabra no aceptada")
            
        else:
            #funcion para filtrar elementos que no estan en alfabeto
            not_alphabet = notInAlphabetSymbols(pal, alphabet)
            print("Palabra no aceptada ya que los simbolos ( "+ not_alphabet+" ) no existen en el alfabeto del AFD")    
