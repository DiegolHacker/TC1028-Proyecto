#Código para imprimir las listas de: https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/#:~:text=use%20join()%20function%20to,character%20specified%20with%20the%20function.
#Primer código completamente funcional, finalizado, el 26/08/2022 10:13.

#requiere de la instalación de la libreria inputimeout, usar el comando pip install inputimeout en la consola (cmd/powershell)


import os
os.system("pip install inputimeout") #Instala la librería inputimeout al correr el programa.
import random
import math
import time
import inputimeout

os.system("cls") #borra la consola, conventirlo en función en una próxima iteración.

jugar = True
puntos = 100

n = " "
rand = int(random.randint(1,9))

def tablero(value, largo, lista): #funciones para generar los tableros.
    for i in range(largo):
        value = int(random.randint(1,9))
        lista.append([value])

def empt_tablero(value, large, lista):
    for i in range(large):
        lista.append([value])


def prnt_tablero(contador, lista): #función para imprimir los tableros.
    while contador <= 9:
        if contador != 4:
            print("|"+" ".join(map(str,lista[contador]))+"|", end = '') #imprimir tablero, junto a las lineas para que se vea bonito y ordenado
        if contador == 4:
            print("|"+" ".join(map(str,lista[contador]))+"|") #imprimir tablero con salto de linea. Se me hace que le puedo quitar el +" " pero ya no le quiero mover.
        contador+=1

condicion = True
iniciar = None

while condicion: #en este ciclo while se implementa la función inputimeout de la librería del mismo nombre para generar una interfaz dinámica donde el texto pueda parpadear de forma automática, y donde se detenga en cuanto detecte un input del usuario
    if condicion:
        print("     Apuestronic\n       Diegol©\n\n\n\n""Pulsa enter para continuar",  end = '') 
        try: #Intenta ejecutar la función inputimeout, esta devuelve error al no ser contestada, así se evita que se detenga el programa.
            iniciar = inputimeout.inputimeout(timeout=0.5) #genera un input, si no se contesta en 0.5 segundos continúa con la ejecución del programa.
        except Exception:
            pass
        if iniciar == "":
            condicion = False
    if condicion:
        os.system("cls")
        print("     Apuestronic\n       Diegol©\n\n\n\n",  end = '')
        try:
            iniciar = inputimeout.inputimeout(timeout=0.5)
        except Exception:
            pass
        if iniciar == "":
            condicion = False
    os.system("cls")

condicion = True
iniciar = None

while condicion: #Usé el mismo código para la interfaz de las instrucciones, en la próxima versión lo convertiré en una función
    if condicion:
        print("            Instrucciones\n\nDebes seleccionar 2 números contiguos\ndel 1 al 9. Si estos números se \nencuentran juntos en el tablero, ganas \n50 puntos, si no, pierdes 5 puntos. \n\nPulsa enter para continuar") #Nota para mimismo: podría hacer que funcionara el parpadeo de la interfaz que quería implementar con una libreria que llevara track of time y poner un if input en menos de 1 segundo, para que cada segundo se actualice, o un pedo asi.
        try:
            iniciar = inputimeout.inputimeout(timeout=0.5)
        except Exception:
            pass
        if iniciar == "":
            condicion = False
    if condicion:
        os.system("cls")
        print("            Instrucciones\n\nDebes seleccionar 2 números contiguos\ndel 1 al 9. Si estos números se \nencuentran juntos en el tablero, ganas \n50 puntos, si no, pierdes 5 puntos.\n\n\n")
        try:
            iniciar = inputimeout.inputimeout(timeout=0.5)
        except Exception:
            pass
        if iniciar == "":
            condicion = False
    os.system("cls")
#print("     Apuestronic\n       Diegol©\n\n\n\n""Pulsa enter para continuar") #Nota para mimismo: podría hacer que funcionara el parpadeo de la interfaz que quería implementar con una libreria que llevara track of time y poner un if input en menos de 1 segundo, para que cada segundo se actualice, o un pedo asi.
#input()
#os.system("cls")
#print("            Instrucciones\n\nDebes seleccionar 2 números contiguos\ndel 1 al 9. Si estos números se \nencuentran juntos en el tablero, ganas \n50 puntos, si no, pierdes 5 puntos. \n\nPulsa enter para continuar")
#input()

while jugar: #el juego se ejecutara mientras la condición de jugar sea cierta

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


    empt_tablero(n, x, empty_board)

    prnt_tablero(z2, empty_board)

    tablero(rand, x, board)

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

    menorstr = str(menor)   #solo convirtiendo los números a str pude hacer que la comprobación jalara DX
    mayorstr = str(mayor)

    os.system("cls")
    print("Puntos:",puntos)

    prnt_tablero(z, board)

    while z3 <= 9:
        #estas casillas son los valores de la y las casillas al rededor de la que estamos comprobando
        casilla = "".join(map(str,board[z3]))       #debido al formato de los elementos de la lista no me dejaba compararlos así nomas, cuando los imprimia en el debug salía como [5] por ejemplo,
        if z3<=8:
            casilla2 = "".join(map(str,board[z3+1]))  #logre hacer que se compararan añadiendo la variable sola mapeada como str a una variable vacía, para quitarle el formato.
        casilla3 = "".join(map(str,board[z3-1]))
        if z3<=4:
            casilla4 = "".join(map(str,board[z3+5])) #estas 2 son para comparar las casillas verticalmente, si la de arriba o la de abajo cumple con los requisitos
        casilla5 = "".join(map(str,board[z3-5]))

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
