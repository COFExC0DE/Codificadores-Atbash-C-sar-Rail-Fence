'''
                   _____________________________________
          ________|       __ __  ___         ___        |________
          \       |   /\    |   |   |   /\  |___  |   | |       /
           \      |  /__\   |   |---   /__\     \ |---| |      /
            \     | /    \  |   |___| /    \ ___/ |   | |     /
            /     |                                     |     \
           /      |_____________________________________|      \
          /__________)                               (__________\
'''


def posicion(letra, posicion_lista):
    '''
    busca en la lista la posicion de la letra, por medio de un ciclo para saber en donde se encuentra en la lista del alfabeto ordenado,
    para cambiar en la misma posicion de la lista2.
    '''

    i = 0
    regresar_pos_alfabeto = 0

    while(i < len(posicion_lista)):

        if(letra == posicion_lista[i]):

            regresar_pos_alfabeto = i
            
        i += 1
        
    return regresar_pos_alfabeto


def aplicar_reglas(letra, alfabeto, alfabeto_al_reves):
    '''
    Al saber la posicion de la letra en la lista de el alfabeto ordenado, cambiamos la letra en la misma posicion del alfabeto al reves
    '''
    posicion_en_alfabeto = posicion(letra, alfabeto)

    if(posicion_en_alfabeto != -1):
        
        cambiar_letra = alfabeto_al_reves[posicion_en_alfabeto]
        

    return cambiar_letra

    
def atbash(oracion):
    '''
    Se ingresara una oracion, la cual vamos a sacar letra por letra con un ciclo, para luego determinar la poisicion en la lista del alfabeto y
    remplazarla en la lista del alfabeto al reves. 
    '''
    
    i=0

    alfabeto = [' ','a','b','c','d','e','f','g','h','i','j','k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabeto_al_reves = [' ','z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

    toda_la_palabra = ' '
    
    while(i < len(oracion)):
        
        letra = oracion[i]            
        toda_la_palabra += aplicar_reglas(letra, alfabeto, alfabeto_al_reves)
        
        i += 1
        
    return toda_la_palabra      



'''
                   ________________________________
          ________|  _     ___  ___          __   |________
          \       | |     |    |___    /\   |__|  |       /
           \      | |     |---     \  /__\  |  \  |      /
            \     | |___  |___  ___/ /    \ |   \ |     /
            /     |                               |     \
           /      |_______________________________|      \
          /__________)                         (__________\
'''		  




def posicion_cesar(letra, lista):

    '''
    Sabremos en la lista del alfabeto, en que posicion de la letra nos encontramos, para asi cambiar la letra
    '''
    
    i = 0
    pos_lista = 0

    while(i < len(lista)):
        
        if(letra == lista[i]):

            pos_lista = i
            
        i += 1
        
    return pos_lista


def aplicar_reglas_cesar(letra, alfabeto,numero):
    '''
    Al saber la posicion de la letra, le sumaresmos las posiciones que le asigne del 1 hasta el 15, a la derecha
    de la lista del alfabeto para cambiarla por la posicion nueva
    '''
    pos = posicion_cesar(letra, alfabeto)

    if(pos < (26 - int(numero))):
        
        nueva_letra = alfabeto[pos + int(numero)]

    else:   
            nueva_letra = alfabeto[(26 - pos) + (int(numero)-2)]
            
    return nueva_letra
    
def cesar(oracion, numero):
    '''
    Se ingresara una oracion, la cual vamos a sacar letra por letra con un ciclo, para luego determinar la poisicion en la lista del alfabeto,
    luego ingresaremos un numero entero, para saber cuantas letras se va a cambiar hacia la derecha.
    '''
    
    i=0
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    toda_la_palabra = ''

    while(i < len(oracion)):
        
        letra = oracion[i]
        
        if (letra == ' '):
            toda_la_palabra += ' '
            
        else:    
            toda_la_palabra += aplicar_reglas_cesar(letra, alfabeto,numero)
        
        i += 1
        
    return toda_la_palabra


'''
                   ______________________________________________________
          ________|  __          __ __         ___  ___        ___   ___ |________
          \       | |__|    /\     |   |      |    |    |\  | |     |    |       /
           \      | |  \   /__\    |   |      |--  |--  | \ | |     |--  |      /
            \     | |   \ /    \ __|__ |___   |    |___ |  \| |___  |___ |     /
            /     |                                                      |     \
           /      |______________________________________________________|      \
          /__________)                                                (__________\
'''
    
    

def leer_palabra1(oracion):

    '''
    Determinaremos la primera fila del codificador, mediante un ciclo en el cual guarda la primera letra,
    y luego va guardando la cuarta letra que aprasca en la lista 
    '''
    i=0
    salida = ''
    numero = 0
    oracion = quitar_espacios(oracion)
    
    while(i < len(oracion)):

        letra = oracion[i]

        if(i == numero):

            numero += 4

            i+=3

        
        salida += letra

        i+=1

    return salida        
    

def leer_palabra2(oracion):
    '''
    Determinaremos la fila del medio del codificador, mediante un ciclo en el cual guarda la segunda letra,
    y luego va guardando la tercera letra que aprasca en la lista 
    '''
    i=1
    salida = ''
    numero = 1
    oracion = quitar_espacios(oracion)

    while(i < len(oracion)):

        
        letra = oracion[i]
        
        if(i == numero):
            
            numero +=2
            i += 1
            
            
        salida += letra
        i+=1

    return salida


def leer_palabra3(oracion):
    '''
    Determinaremos la fila del medio del codificador, mediante un ciclo en el cual guarda la tercer letra,
    y luego va guardando la cuarta letra que aprasca en la lista 
    '''
    i=2
    salida = ''
    numero = 2
    oracion = quitar_espacios(oracion)
    
    while(i < len(oracion)):

        letra = oracion[i]    

        salida += letra

        i+=4

    return salida

def quitar_espacios(oracion):

    '''
    Lee la oracion letra por letra, y detertmina los espaccios que hay en la oracion y los elimina si existen, para
    asi poder agrupar mas facilmente los valor que se necesitan.
    '''
    
    i=0
    salida = ''
    while(i < len(oracion)):

        letra = oracion[i]

        if(letra == ' '):
               sal = i + 1
               letra = oracion[sal]
               i += 1

        salida += letra

        i += 1

    return salida

def unir_oracion(oracion):
    '''
    Guarda en una sola lista las oraciones codificadas y agrupa las 3 oraciones codificada para luego mostrar la codificacion,
    pero antes de ello, en un ciclo agruparemos las oraciones en grupos de 5 letras y dejaremos un espacio.
    '''
    i=0
    oracion = leer_palabra1(oracion) + leer_palabra2(oracion) + leer_palabra3(oracion)
    numero = 5
    salida= ''
    
    while(i < len(oracion)):

        letra = oracion[i]

        if(i == numero):
            numero += 5
            salida += ' '
            
        salida += letra

        i+=1
            
    return salida

'''
                   _________________________________
          ________|                     __ __       |________
          \       |   /\    /\     /\     |   |\  | |       /
           \      |  /  \  /  \   /__\    |   | \ | |      /
            \     | /    \/    \ /    \ __|__ |  \| |     /
            /     |                                 |     \
           /      |_________________________________|      \
          /__________)                           (__________\
'''

def main():

            
        continuar = True
        while continuar:
            print('\n [1] Atbash \n [2] Cesar \n [3] Rail Fence \n')
            escoger = input(' Escoja un algoritmo: ')

            if(escoger == '1'):
                oracion = input('\n Mensaje a cifrar: ')
                print(atbash(oracion))

                print('----------------------------------------------------------------------------')
           
            elif(escoger == '2'):
                n = input('\n Desplazamiento (1-7): ')

                if (int(n) >= 8):
                    
                    print('\n Ingrese un valor del 1 - 7 ')
                else:    
                    oracion = input('\n Mensaje a cifrar: ')
                    print(' ' + cesar(oracion, n ))
                
                print('-----------------------------------------------------------------------------')

            elif(escoger == '3'):
                oracion = input('\n Mensaje a cifrar: ')
                print(' '+ unir_oracion(oracion))

                print('\n----------------------------------------------------------------------------')

            else:    
                 print("\n INGRESE UN VALOR VALIDO [1], [2], [3]")
                 print('\n----------------------------------------------------------------------------')
   
                           
if __name__ == '__main__':
        main()








