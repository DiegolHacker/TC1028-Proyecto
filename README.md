# TC1028-Proyecto
Primer avance del proyecto 1 de la clase de TC1028

### Contexto

Mi programa por ahora se llama "Números de la suerte", y consiste en un juego de apuestas donde se le dan varios números secretos al usuario (entre 10 y 15, esta por definir según la dificultad) y el usuario debe poner 2 números consecutivos, si esos 2 números se encuentran juntos en alguna de las posiciones de los números que se le den al usuario (queda definir si solo se comprobara horizontal o también verticalmente) el usuario gana. Pretendo implementar un sistema de créditos, donde, por ejemplo, el usuario empiece con 100 créditos, cada turno de juego cueste 5, y si gana se le den 50 hasta que pierda o se vaya.

### Importancia

Mi proyecto se vuelve interesante sobre todo en la parte de comprobar si esa secuencia de números existe dentro de las listas, ya que pretendo usar ciclos while y funciones for para automatizar este proceso en cierta medida, además de que tendrá una interfaz dinámica gracias al uso de la librería system para poder limpiar la consola y cambiar los visuales en tiempo real, revelando los números al ganar o perder, llevando cuenta de los créditos, mostrando los números como una cuadrícula, etc. También usaré la librería Random para poder generar números aleatorios y que el juego verdaderamente se base en la suerte.

## Algoritmo

0. Limpiar la consola en cada iteración donde se vuelva a imprimir.

1. Imprimir los créditos iniciales y unas instrucciones en una interfaz acomodada, restar 5 créditos al empezar a jugar.
2. Generar números enteros aleatorios y guardarlos en una lista.
3. Imprimir cuadros negros para representar los números ocultos, así como los créditos restantes
4. Pedir 2 números consecutivos al usuario en variables diferentes. Teniendo ya el primer número, comprobar si el segundo número es igual al primer numero +- uno, si no pedir que vuelva a ingresar el número a través de un ciclo while que sea cierto hasta que se obtenga una respuesta válida.
5. A través de un ciclo for comprobar en cada celda de la lista si alguno de los 2 números se encuentra en la lista, si es cierto comprobar si el siguiente número coincide con el otro número, si esto es cierto, definir una variable de ganador a cierto para detener el ciclo e imprimir un mensaje de victoria.
6. Cuando el estado de vistoria sea cierto, revelar los números al usuario e imprimirlos en forma de cuadrícula con un ciclo for para imprimir uno por uno, sumar los créditos al total, preguntar si se desea volver a jugar.


Usando la funcion randint() de la libreria random generar 10 o 15 números aleatorios, guardarlos en 1,2, o 3 listas diferentes (dependiendo de si hare comprobaciones verticales)
