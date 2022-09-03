# TC1028-Proyecto
Primer avance del proyecto 1 de la clase de TC1028

## SE INSTALA LA LIBRERÍA inputimeout PARA PYHTON DE FORMA AUTOMÁTICA AL CORRER EL PROGRAMA USANDO EL COMANDO pip install inputimeout EN LA CONSOLA.

### Contexto

Mi programa por ahora se llama "Apuestronic", y consiste en un juego de apuestas donde se le dan varios números secretos al usuario (10)  y el usuario debe poner 2 números consecutivos, si esos 2 números se encuentran juntos en alguna de las posiciones de los números que se le den al usuario el usuario gana. El usuario empieza con 100 créditos, si gana se le suman 50, y si pierde se le quitan 5.

### Importancia

Mi proyecto se vuelve interesante sobre todo en la parte de comprobar si esa secuencia de números existe dentro de las listas, implementé ciclos while y funciones for para automatizar este proceso, además de que tiene una interfaz dinámica gracias al uso de la librería system para poder limpiar la consola y cambiar los visuales en tiempo real, revelando los números al ganar o perder, llevando cuenta de los puntos, mostrando los números en una cuadrícula, etc. También usé la librería Random para poder generar números aleatorios y que el juego verdaderamente se base en la suerte.

## Algoritmo

0. Limpiar la consola en cada iteración donde se vuelva a imprimir.

1. Imprimir los créditos iniciales y unas instrucciones en una interfaz acomodada.
2. Generar números enteros aleatorios y guardarlos en una lista.
3. Imprimir cuadros negros para representar los números ocultos en forma de cuadrícula, así como los créditos restantes
4. Pedir 2 números consecutivos al usuario en variables diferentes. Teniendo ya el primer número, comprobar si el segundo número es igual al primer numero +- uno, si no, pedir que vuelva a ingresar el número a través de un ciclo while que sea cierto hasta que se obtenga una respuesta válida.
5. A través de un ciclo while comprobar en cada celda de la lista si el número menor se encuentra en la lista, si es cierto comprobar si el siguiente número coincide con el mayor, si esto es cierto, desplegar un mensaje de victoria, y detener el ciclo de validación.
6. Cuando el estado de victoria sea cierto, revelar los números al usuario e imprimirlos en forma de cuadrícula con un ciclo while para imprimir uno por uno, sumar los créditos al total, preguntar si se desea volver a jugar.


Usando la funcion randint() de la libreria random generar 10 o 15 números aleatorios, guardarlos en 1 lista
