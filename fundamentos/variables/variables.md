# Variables

En Python, una variable no es más que un nombre que hace referencia a un `objeto` en memoria. Esto significa que cuando creas una variable, lo que realmente estás haciendo es crear una referencia (o puntero) a un valor almacenado en una ubicación específica de la memoria.

Veamos un ejemplo:

```py
# Creamos una variable llamada "cantidad"
cantidad = 5
```

1.  Python primero evalúa la `expresión` a la derecha del signo igual (=), en este caso, el número 5.
2.  Como 5 es un número entero, Python crea un `objeto de tipo int` que almacena el valor 5.
3.  El objeto int que contiene el valor 5 se almacena en una ubicación específica de la memoria. Luego, Python asigna la variable cantidad para que apunte a esa dirección de memoria.
4.  Si más adelante asignas otro valor entero a otra variable con el mismo valor de `cantidad`, Python podría reutilizar el objeto existente en lugar de crear uno nuevo, gracias a una técnica conocida como "interning" o "internado" en Python.

Esto significa que las variables en Python no contienen los datos directamente, sino que actúan como referencias a los objetos en memoria.


## Interning o Internado



## Contador de referencias

Contador de referencias: Python mantiene un contador de referencias para cada objeto en memoria. Este contador aumenta cuando se crea una nueva referencia al objeto y disminuye cuando una referencia se elimina. Cuando el contador llega a cero, el recolector de basura de Python libera la memoria ocupada por ese objeto.
