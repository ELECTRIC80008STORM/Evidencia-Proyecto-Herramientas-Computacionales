# Evidencia del Proyecto - Herramientas Computacionales
Repositorio de nuestra evidencia final para la clase de Herramientas Computacionales.


## Juego de Pacman (Cambios realizados por Rommel - A01709922)

### Cambios en los valores de la lista _tiles_[]
Tras analizar la lista tiles y su efecto en la representación del mapa, concluimos que los valores de 0 representan un bloque de barrera con el cual ni los fantasmas ni pacman pueden interactuar, los valores de 1 representan los caminos por los que se pueden pasar y que poseen un punto. Al notar esto lo que se hizo fue reemplazar manualmente los valores para generar el nuevo tablero.


### Cambio en los valores de aparición de Pacman
Al cambiar el tablero fue necesario cambiar el punto de aparición de Pacman a un lugar del tablero para evitar problemas al iniciar en una barrera.


### Modificación de los valores en _ontimer_()
Después de analizar y experimentar con distintos valores en el tablero, se llegó a la conclusión que la función que afectaba la velocidad de movilidad de pacman y los fantasmas era la función de “ontimer()”, pues controlaba cada cuanto se activaba la función “move()”, misma función que permitía el movimiento de pacman y los fantasmas. Se redujo el tiempo de 100 milisegundos a 30 milisegundos, esto con el objetivo de que el movimiento se diera con mayor frecuencia, es decir, más rápido.



## Juego de Tic Tac Toe (Cambios realizados por Pablo Hazael - A01710778)

### Colores y tamaños

Para cambiar los colores del las figuras “X” y “O” se usó la función de "color()" el cual
viene de la librería turtle. También se modificaron los parámetros de “drawx()” y 
“drawo()”, cada uno de manera en la que quede centrada


### Validar si una casilla se encuentra ocupada

Para hacer una detección de las cajas primero creamos una lista con puros 0s, uno por cada caja.
Con una función le pasamos los parámetros de “x” y “y” detectamos en cuál de las cajas esta,
si esta caja tiene un 0 se le cambiamos por 1 y decimos que la caja está vacía.
Si la caja ya tenía un 1 entonces decimos que ya estaba llena y no la modificamos.
Finalmente metemos las funciones de tap dentro de un if para que no se
modifique el juego hasta que se elija una casilla disponible.



## Juego de Memory (Cambios realizados por Osvaldo del Valle - A01275702)

### Número de clics 

Para mostrar el número de clics que el usuario ha dado, mostramos un elemento label en la ventana,
esto para mostrar el valor ahí.
Dado que existe una función tap() que es la que se llama en cada clic podemos hacer que la función
updateTaps(), añadida por nosotros, se active a la par.
Esta función va a acceder al valor de una variable global y ahí sumarle 1 y asignar ese valor al label.


### Mostrar un mensaje cuando todos los tiles fueron descubierto

El código tiene un arreglo llamado hide, en él se guardan valores booleanos que se representan con un
False cuando ya se descubrieron los tiles.
Por lo tanto también cada vez que se da clic en un tile se llamará a la función implementada
“checkMarks()” para recorrer el arreglo buscando un True y cuando ya no lo haya significará que ya se descubrieron todos.
En este punto se estará renderizando en pantalla un label con la leyenda correspondiente.
