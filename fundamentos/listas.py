"""
* Listas en Python: Secuencia

- Una lista es una colección ordenada y mutable de elementos.
- Se definen utilizando corchetes [].
- Sería equivalente a lo que en otros lenguajes se conoce por arrays, o vectores.
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
IMPORTANTE: En terminos de rapidez y eficiencia para agregar múltiples elementos en una lista,
se recomienda utilizar el método `extend()` y el operador `+=`.
- `+=` es eficiente cuando se necesita concatenar listas o strings.
- Si solo necesitas agregar un elemento a la lista utiliza el método `append()`,
es muy eficiente para este propósito, ya que realiza la operación de inserción directa.

* Métodos y operaciones comunes de las listas:
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
# Ideal cuando ya tienes una lista de elementos que deseas agregar a otra lista.
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
* Slicing (subdivisión de secuencias) en listas
El slicing permite extraer una subsecuencia de elementos de una secuencia
(como listas, cadenas, tuplas, etc.) utilizando la sintaxis:
sequence[start:stop:step]
- start: Índice de inicio (opcional), por defecto es 0.
- stop: Índice donde se detiene el slicing (opcional), por defecto es el final de la secuencia.
- step: Paso o intervalo entre los elementos seleccionados (opcional), por defecto es 1.
"""

slicing = [2, 3, 4, 5, 6, 7]

# Obtiene los primeros 3 elementos de la lista.
print("Primeros 3 elementos:", slicing[:3])  # Imprime [2, 3, 4]

# Obtiene los últimos 3 elementos de la lista.
print("Últimos 3 elementos:", slicing[-3:])  # Imprime [5, 6, 7]

# Slicing con saltos: selecciona elementos desde el índice 1 hasta el 4, con un salto de 3.
print(
    "Elementos desde el segundo al quinto con salto de 3:", slicing[1:5:3]
)  # Imprime [3, 6]

# Ejemplo de slicing extendido
slicing_extended = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Selecciona elementos a partir del índice 1 hasta el final, con un salto de 4.
result = slicing_extended[1::4]
print("Slicing extendido:", result)  # Imprime [20, 60]

# Esta vez vamos a seleccionar elementos de la lista en orden inverso con un salto de 3.
# Inicia en el último elemento, se omite el inicio (por lo tanto va hasta el inicio de la lista),
# y utiliza un paso de -3.
reversed_slicing = slicing_extended[::-3]
print("Slicing extendido en orden inverso:", reversed_slicing)  # Imprime [90, 60, 30]

# `clear()` elimina todos los elementos de una lista
numbers.clear()
print("Lista después de clear():", numbers)  # Imprime []

# Uso del método index() para encontrar la posición o índice de un elemento
fruits = ["apple", "banana", "cherry"]
print("Índice de 'cherry' en fruits:", fruits.index("cherry"))  # Imprime 2

# Contar las apariciones de un elemento en la lista usando count()
print("Número de apariciones de 'apple':", fruits.count("apple"))  # Imprime 1

# `sort()` ordena los elementos de una lista de menor a mayor
fruits.sort()
print("Lista fruits ordenada:", fruits)  # Imprime ['apple', 'banana', 'cherry']

# Para ordenar de mayor a menor con `sort()` usamos reverse=True
fruits.sort(reverse=True)
print(
    "Lista fruits ordenada de mayor a menor:", fruits
)  # Imprime ['cherry', 'banana', 'apple']

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
print("agregando 6 a new_numbers:", new_numbers)

# La lista `numbers` ahora contiene [1, 2, 3, 4, 5, 6]
print("numbers:", numbers)

# Desempaquetar elementos dentro de una lista con el operador *
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = [*lista1, *lista2]
print("lista combinada:", lista_combinada)  # Salida: [1, 2, 3, 4, 5, 6]

# Agregar multiples valores a una lista con el operador +=
# Extiende la lista en una sola operación.
lista = [1, 2, 3]
lista += [4, 5, 6]
print("Lista:", lista)  # Salida: [1, 2, 3, 4, 5, 6]

# Iterar dos listas a la vez con la función `zip()`
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)
