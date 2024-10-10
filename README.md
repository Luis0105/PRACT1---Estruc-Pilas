# PRACT1---Estruc-Pilas
En este programa se presenta dibujos de los distintos estados de una estructura tipo pila, si se llevan a cabo las siguientes operaciones, como eliminar o insertar letras o datos. 

¿Con cuántos elementos quedó la pila?
R = La pila se quedó con dos elementos (letras) que son V y R.

¿Hubo algún caso de error (desbordamiento o subdesbordamiento)? Si ocurrió algún error, explícalo.
R = Se presento subdesbordamiento al no permitir que se realizara la operación de eliminación cuando no había elementos en la pila, este error se produjo cuando se intentó eliminar un elemento de la pila después de que había quedado vacía, es decir, tras eliminar "X". En este caso, el método eliminar() verificó que el tope era 0 y no pudo realizar la operación, indicando que la pila estaba vacía.
