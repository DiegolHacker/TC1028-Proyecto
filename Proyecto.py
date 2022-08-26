#Código para imprimir las listas de: https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/#:~:text=use%20join()%20function%20to,character%20specified%20with%20the%20function.
#Primer código completamente funcional, finalizado, el 26/08/2022 10:13.

import os
import random
import math #no usé esta librería para nada

os.system("cls") #borra la consola :P

jugar = True
puntos = 100

#def check(tablero, variable): #función para comparar las listas con los números, no funcionó :C
#    for x in tablero:
#        if variable == x:
#            return True
#        else:
#            return False

print("     Apuestronic\n       Diegol©\n\n\n\n""Pulsa enter para continuar") #Nota para mimismo: podría hacer que funcionara el parpadeo de la interfaz que quería implementar con una libreria que llevara track of time y poner un if input en menos de 1 segundo, para que cada segundo se actualice, o un pedo asi.
input()
os.system("cls")
print("            Instrucciones\n\nDebes seleccionar 2 números contiguos\ndel 1 al 9. Si estos números se \nencuentran juntos en el tablero, ganas \n50 puntos, si no, pierdes 5 puntos.")
#                  Instrucciones                Instrucciones                        Instrucciones                        Instrucciones                        Instrucciones        esto lo puse para ver cada cuanto tenia que poner el salto de linea xd
input()
while jugar: #el juego se ejecutara mientras la condición de juagr sea cierta

    os.system("cls")
    print("Puntos:",puntos)

    board = [] #lista vacía para los números aleatorios.
    empty_board = [] #lista vacia para el tablero sin descubrir

    x = 10 #Largo del tabero            Solo funciona visualmente pues no hace más comprobaciones fuera del rango especificado, pero podría cambiar los 9, los 4, y todo eso por variables que dependan una de la otra para hacerlo escalable.
    y = 2 #ancho del tablero (no se implementa para nada tho)            Hasta podría hacer que estos fueran inputs para determinar la dificultad del juego. Dehecho lo voy a hacer la próxima semana C:<
    z = 0       #las variables z son contadores para los ciclos de impresión y de validación. Podría usar la misma variable pero me sirven para el debug.
    z2 = 0
    z3 = 0
    mayor = 0
    menor = 0

    for i in range(x):
        n = "| |"
        empty_board.append([n]) #hacer tablero vacío



    while z2 <= 9:
        if z2 != 4:
            print(' '.join(empty_board[z]), end = '') #imprimir tablero vacío
        if z2 == 4:
            print(' '.join(empty_board[z])) #imprimir tablero con salto de línea
        z2+=1

    #for i in range(x):
    #    n = "|"+str(random.randint(1,9))+"|" #Este tablero funciona con el formato que quiero, pero convierto todo a str y no deberia de jalar :C
    #    board.append([n]) #hacer tablero

    for i in range(x):
        n = int(random.randint(1,9)) #generar números aleatorios
        board.append([n]) #rellenar tablero (board) de números aleatorios

    print("\n")

    n1 = int(input("Número 1:"))   #Pide el número al jugador. Puedes poner números mayores a 9 pero ps pierdes y ya.

    valido = False
    while valido == False:
        n2 = int(input("Número 2:"))
        if n2 + 1 == n1 or n2 - 1 == n1:    #Comprueba que el segundo número sea contiguo al primero.
            valido = True
        else:
            valido = False
            print("número inválido")

    if n1 > n2:
        mayor = n1
        menor = n2
    elif n2 > n1:
        mayor = n2
        menor = n1


    #for row in board:
    #	print (" asd".join(map(str, row)), end = '') #ya ni me acuerdo para que era esto

    menorstr = str(menor)   #solo convirtiendo lso números a str pude hacer que la comprobación jalara DX
    mayorstr = str(mayor)

    os.system("cls")
    print("Puntos:",puntos)

    while z <= 9:
        if z != 4:
            print("|"+" ".join(map(str,board[z]))+"|", end = '') #imprimir tablero, junto a las lineas para que se vea bonito y ordenado
            #print(*board, sep = ' ')
        if z == 4:
            print("|"+" ".join(map(str,board[z]))+"|") #imprimir tablero con salto de linea. Se me hace que le puedo quitar el +" " pero ya no le quiero mover.
            #print(*board, sep = ' ')
        z+=1


    while z3 <= 9:
        #estas casillas son los valores de la y las casillas al rededor de la que estamos comprobando
        casilla = "".join(map(str,board[z3]))       #debido al formato de los elementos de la lista no me dejaba compararlos así nomas, cuando los imprimia en el debug salía como [5] por ejemplo,
        if z3<=8:
            casilla2 = "".join(map(str,board[z3+1]))  #logre hacer que se compararan añadiendo la variable sola mapeada como str a una variable vacía, para quitarle el formato.
        casilla3 = "".join(map(str,board[z3-1]))
        if z3<=4:
            casilla4 = "".join(map(str,board[z3+5])) #estas 2 son para comparar las casillas verticalmente, si la de arriba o la de abajo cumple con los requisitos
        casilla5 = "".join(map(str,board[z3-5]))

#        print(casilla)           los ifs abajo de este fueron usado durante la fase de debug, para ver si si los podía comparar y para ver como python manejaba las variables

#        if(check(board, menor)):
#            print("hay una coincidencia con menor")
#            input("menor")

#        if casilla == menorstr: #darle el mism formato a menor que las variables dentro e la lista ['a'] a ver si asi si los compara bien
#            print("valor de menor: ", menorstr)
#            print("hay una coincidencia con menor")
#            input("menor")

        if casilla == menorstr and ((casilla2 == mayorstr or casilla3 == mayorstr) or (casilla4 == mayorstr or casilla5 == mayorstr)): #comprueba si a casilla en la que estamos y las de al rededor cumplen con las caracteristicas
            print("\n     Ganaste! \nPulsa Enter para continuar, escribe x para salir")
            z3 = 10 #en cuanto encuentra unas casillas ganadoras, el programa de validación se detiene
            puntos+=50

        elif z3 == 9:
            print("\n    Perdiste \nPulsa Enter para continuar, escribe x para salir")
            puntos-=5

        z3+=1

    a = input(" ")
    if a == "x":
        jugar = False
