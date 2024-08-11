"""
* Listas en Python

- Una lista es una colección ordenada y mutable de elementos.
- Se definen utilizando corchetes [].
- Pueden contener elementos de cualquier tipo de datos (números, cadenas, listas, etc.).
- Son mutables, lo que significa que sus elementos pueden modificarse después de la creación.
- Se pueden anidar listas dentro de listas (listas de listas).
- Son iterables, es decir, se pueden recorrer usando bucles como for.
- Se pueden concatenar utilizando el operador + y repetir utilizando el operador *.
- Las listas se representan como objetos de la clase list en Python.
- Utilizan un arreglo dinámico internamente para gestionar los elementos.
- Se pueden crear usando la función list().
- Se pueden convertir a otros tipos de datos, como tuplas (tuple), conjuntos (set), 
diccionarios (dict) y cadenas de texto (str).
- Cuando asignas una lista a una variable, no copia los datos, la variable solo apunta a la lista existente.

Métodos y operaciones comunes de las listas:
- append(x): Añade un elemento al final de la lista.
- extend(iterable): Añade todos los elementos de un iterable al final de la lista.
- insert(i, x): Inserta un elemento en la posición especificada.
- remove(x): Elimina la primera aparición del valor especificado.
- pop([i]): Elimina y retorna el elemento en la posición especificada.
- clear(): Elimina todos los elementos de la lista.
- index(x[, start[, end]]): Retorna el índice de la primera aparición del valor especificado.
- count(x): Retorna el número de veces que el valor especificado aparece en la lista.
- sort(key=None, reverse=False): Ordena los elementos de la lista.
- reverse(): Invierte el orden de los elementos de la lista.
- copy(): Retorna una copia superficial de la lista.
"""

# Crear una lista vacía utilizando la función list()
new_list = list()
print("Lista vacía usando list():", new_list)  # Imprime []

# Crear una lista vacía utilizando corchetes []
empty_list = []
print("Lista vacía usando corchetes []:", empty_list)  # Imprime []

# Crear una lista con elementos enteros
numbers = [1, 2, 3, 4, 5]
print("Lista de enteros:", numbers)  # Imprime [1, 2, 3, 4, 5]

# Crear una lista con elementos de diferentes tipos de datos
other_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(
    "Lista con diferentes tipos:", other_list
)  # Imprime [1, "Hello", 3.14, True, [1, 2, 3]]

# Acceder a los elementos de una lista usando índices
# Si se usa un índice fuera del rango, Python arroja un IndexError
print("Primer elemento:", other_list[0])  # Imprime 1
print("Segundo elemento:", other_list[1])  # Imprime "Hello"
print("Tercer elemento:", other_list[2])  # Imprime 3.14
print("Cuarto elemento:", other_list[3])  # Imprime True
print("Último elemento:", other_list[-1])  # Imprime [1, 2, 3]
print("Primer elemento de la lista anidada:", other_list[4][0])  # Imprime 1

# Obtener la longitud de una lista usando len()
print("Longitud de la lista numbers:", len(numbers))  # Imprime 5

# Modificar un elemento de una lista usando su índice
numbers[0] = 10
print("Lista modificada:", numbers)  # Imprime [10, 2, 3, 4, 5]

# Concatenar dos listas utilizando el operador +
numbers = numbers + [6, 7, 8]
print("Listas concatenadas:", numbers)  # Imprime [10, 2, 3, 4, 5, 6, 7, 8]

# Desestructurar una lista en variables individuales
a, b, c, d, e = other_list
print(
    "Elementos desempaquetados:", a, b, c, d, e
)  # Imprime 1 Hello 3.14 True [1, 2, 3]

# Copiar una lista usando el método copy()
new_copy = numbers.copy()
print("Copia de la lista numbers:", new_copy)  # Imprime [10, 2, 3, 4, 5, 6, 7, 8]

# Añadir un elemento al final de una lista usando append()
empty_list.append("Hello")
print("Lista después de append():", empty_list)  # Imprime ["Hello"]

# Insertar un elemento en una posición específica de la lista usando insert()
numbers.insert(0, 0)
print("Lista después de insert(0, 0):", numbers)  # Imprime [0, 10, 2, 3, 4, 5, 6, 7, 8]

# Añadir varios elementos a una lista usando extend()
empty_list.extend("Mayer")
print(
    "Lista después de extend():", empty_list
)  # Imprime ["Hello", "M", "a", "y", "e", "r"]

# Remover el primer elemento que coincide con el valor especificado usando remove()
numbers.remove(10)
print("Lista después de remove(10):", numbers)  # Imprime [0, 2, 3, 4, 5, 6, 7, 8]

# Remover y retornar el último elemento de una lista usando pop()
last_element = numbers.pop()
print("Elemento eliminado con pop():", last_element)  # Imprime 8
print("Lista después de pop():", numbers)  # Imprime [0, 2, 3, 4, 5, 6, 7]

# Eliminar un elemento de una lista por su índice usando del
del numbers[0]
print("Lista después de del numbers[0]:", numbers)  # Imprime [2, 3, 4, 5, 6, 7]

"""
* Slicing de listas
- sequence[start:stop:step]
- start: Índice de inicio, 0 por defecto
- stop: Índice de fin del slicing, fin de la lista por defecto
- step: Es el paso o salto entre elementos de la secuencia. Por defecto es 1
"""
print("Primeros 3 elementos:", numbers[:3])  # Imprime [2, 3, 4]

# Slicing extendido
slicing_extended = [10, 20, 30, 40, 50, 60, 70, 80, 90]
result = slicing_extended[1::4]
print(result)  # Imprime [20, 60]

# Remover todos los elementos de una lista usando clear()
numbers.clear()
print("Lista después de clear():", numbers)  # Imprime []

# Uso del método index() para encontrar la posición o índice de un elemento
fruits = ["apple", "banana", "cherry"]
print("Índice de 'cherry' en fruits:", fruits.index("cherry"))  # Imprime 2

# Contar las apariciones de un elemento en la lista usando count()
print("Número de apariciones de 'apple':", fruits.count("apple"))  # Imprime 1

# Ordenar los elementos de una lista usando sort()
fruits.sort()
print("Lista fruits ordenada:", fruits)  # Imprime ['apple', 'banana', 'cherry']

# Invertir el orden de los elementos de una lista usando reverse()
fruits.reverse()
print("Lista fruits invertida:", fruits)  # Imprime ['cherry', 'banana', 'apple']

# Iterar a través de los elementos de una lista usando un bucle for
for fruit in fruits:
    print(fruit)

# Crear una lista por comprensión de números del 0 al 9
numeros = [x for x in range(10)]
print("Lista de números del 0 al 9:", numeros)

# Crear una lista de listas - Matrices
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3:", matriz)

# Acceder a elementos en una lista de listas
elemento = matriz[1][2]
print("Elemento en la posición [1][2] de la matriz:", elemento)  # Imprime 6

# * Asignar una lista a una variable
# No se pasa pasa por valor si no por referencia
numbers = [1, 2, 3, 4, 5]
print("Lista numbers:", numbers)

# Asignar la lista `numbers` a la nueva variable `new_numbers`
new_numbers = numbers
print("new_numbers:", new_numbers)

new_numbers.append(6)
print("new_numbers:", new_numbers)

# La lista `numbers` ahora contiene [1, 2, 3, 4, 5, 6]
print("numbers:", numbers)
