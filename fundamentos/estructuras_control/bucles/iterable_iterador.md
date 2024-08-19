## Iterable

Un iterable es cualquier conjunto de elementos que puedes recorrer uno por uno.

- Los elementos pueden ser `indexados` (Podemos acceder a ellos mediante un índice). Sin embargo, no todos los iterables son indexados; esta característica es exclusiva de ciertos tipos de datos.
- **Acceso en diccionarios:** En Python, los diccionarios permiten acceder a sus elementos a través de claves asociadas. Estas claves deben ser de un tipo de dato inmutable, como números, cadenas de texto, tuplas, booleanos, entre otros.
- **Acceso en sets:** En el caso de los sets, no es posible acceder a un elemento por índice, ya que son colecciones no ordenadas que no permiten duplicados. Solo es posible verificar si un elemento existe dentro del set.

## Recorrer o Iterar

**Recorrer** o **Iterar** significa pasar por cada elemento de un conjunto, uno por uno, de manera ordenada. Esto es útil cuando queremos hacer algo con cada elemento, como procesarlos o manipularlos.

## Index o Indexado

Un índice es un número que indica la posición de un elemento dentro de una estructura de datos (colección o conjunto de datos).

Los índices en programación suelen comenzar en 0, por lo que el primer elemento tiene índice 0, el segundo tiene índice 1, y así sucesivamente.

- Cuando hablamos de acceder a un elemento por su índice, nos referimos a seleccionar un elemento específico dentro de un conjunto utilizando su posición.

- Normalmente, se utilizan `corchetes []` para acceder a un elemento. El número dentro de los corchetes indica la posición del elemento que queremos.

## Iterador

Un iterador es una herramienta o mecanismo que nos permite `movernos` por los elementos de un iterable. El iterador actúa como un "guía" que nos lleva de un elemento al siguiente.

- El iterador nos permite avanzar por los elementos del iterable, uno por uno.
- El iterador mantiene el estado de dónde te encuentras en el recorrido. Así, sabe qué elemento devolver a continuación.
- Cuando llegas al final del iterable, el iterador te indica que ya no hay más elementos para recorrer.

## Ejemplo en la vida real

Imagina que tienes una fila de personas esperando para entrar a un evento. Cada `persona` en la fila es un elemento en un iterable. El `"guía"` (el iterador) lleva a cada persona de la fila, una por una, al evento.
