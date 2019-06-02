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


# Inicio del programa ingresando transiciones de la forma: estado, simbolo, estado de llegada
transitions = {} 

trans = input("Ingrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
if not(trans): sys.exit() # Si usuario no ingresa nada entonces el programa acaba 

#Si usuario ingresa una transicion se analiza si ésta es valida y se guarda en diccionario
while trans: 
    separate_trans = [elem.strip() for elem in trans.split(',') if elem and not(elem.isspace())]
    
    while len(separate_trans) != 3 or len(separate_trans[1]) > 1:
        print("Transición invalida")
        trans = input("\nIngrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
        separate_trans = [elem.strip() for elem in trans.split(',') if elem and not(elem.isspace())]
    
    actual_state, symbol, arrive_state = separate_trans[0], separate_trans[1], separate_trans[2]
    #Para validar que Autómata no sea AFND se analiza si estado,simbolo ya se encuentra almacenado
    if (actual_state, symbol) in transitions.keys():
        
        #Si este está se pregunta si desea reemplazarlo o desea dejarlo como está 
        option = input("\nEstado ya lleva esa transición a otro estado... Desea reemplazarla? (S | N): ")
        if option in ('S','s'):
            transitions[(actual_state, symbol)] = arrive_state  
    else:
        transitions[(actual_state, symbol)] = arrive_state

    print('\n',transitions, '\n')
    trans = input("\nIngrese transición de la forma: estado, simbolo, estado llegada\n >> ").strip()
    

#Se realiza la recolección de datos 

input_states = [state[0] for state in list(transitions.keys())]
output_states = [state for state in transitions.values()]
# Se guarda el alfabeto con cada simbolo ingresado con la 2da posición de cada transición 
alphabet = sorted(set([state[1] for state in list(transitions.keys())]))

#Se guardan estados juntando estado de entrada y estados de llegada ya que 
#Si en algun caso un estado esta aislado de los demas o no tiene estados de llegada 
states = sorted(set(input_states + output_states))


#Ingreso de estado inicial
initial_state = input("\nIngrese estado inicial: ")

while initial_state not in states:
    print("Estado inicial invalido")
    initial_state = input("\nIngrese estado inicial: ")

accept_states = acceptStatesValid(states, "Ingrese estado final (Termina si no ingresa nada): ")

#Ingreso de palabra y se analiza si ésta es aceptada o rechazada 
while True:
    flag = True
    pal = input("Ingrese la palabra a revisar: ")
    estado_actual = initial_state 
    
    #revisa si cada simbolo de la palabra existe en alfabeto
    word_accepted = all(elem in alphabet for elem in set(pal)) 
    
    #Si se ingresa la palabra vacía se analiza si está o no en estado aceptado
    if not(pal):
        print("Palabra aceptada") if estado_actual in accept_states else print("Palabra no aceptada")
    
    else:
        if word_accepted:
            for symbol in pal:
                #revisa si existe una transición
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
