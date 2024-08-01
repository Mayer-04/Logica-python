"""
* Listas en Python

- Un conjunto ordenado de elementos.
- Se definen entre corchetes [].
- Pueden contener elementos de cualquier tipo de datos.
- Son mutables, es decir, se pueden modificar después de ser creadas.
- Se pueden anidar, lo que significa que una lista puede contener otras listas.
- Se pueden iterar utilizando bucles como for.
- Se pueden concatenar utilizando el operador +.
- Internamente, las listas se representan como objetos de la clase list.
- Utilizan un arreglo dinámico internamente para almacenar los datos.
- Se pueden crear utilizando la función list().
- Se pueden convertir a otros tipos de datos como tuplas (tuple), conjuntos (set), 
diccionarios (dict) y cadenas de texto (str).

Métodos comunes de las listas:
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
print(new_list)  # Imprime []

# Crear una lista vacía utilizando corchetes []
empty_list = []
print(empty_list)  # Imprime []

# Crear una lista con elementos enteros
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Imprime [1, 2, 3, 4, 5]

# Crear una lista con elementos de diferentes tipos de datos
other_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(other_list)  # Imprime [1, "Hello", 3.14, True, [1, 2, 3]]

# Acceder a los elementos de una lista usando índices
# Si se usa un índice fuera del rango, Python arroja un IndexError
print(other_list[0])  # Imprime el primer elemento: 1
print(other_list[1])  # Imprime el segundo elemento: "Hello"
print(other_list[2])  # Imprime el tercer elemento: 3.14
print(other_list[3])  # Imprime el cuarto elemento: True
print(other_list[-1])  # Imprime el último elemento: [1, 2, 3]
print(other_list[4][0])  # Imprime el primer elemento de la lista anidada: 1

# Obtener la longitud de una lista usando len()
print(len(numbers))  # Imprime 5

# Modificar un elemento de una lista usando su índice
numbers[0] = 10
print(numbers)  # Imprime [10, 2, 3, 4, 5]

# Concatenar dos listas utilizando el operador +
numbers = numbers + [6, 7, 8]
print(numbers)  # Imprime [10, 2, 3, 4, 5, 6, 7, 8]

# Desestructurar una lista en variables individuales
a, b, c, d, e = other_list
print(a)  # Imprime 1
print(b)  # Imprime "Hello"
print(c)  # Imprime 3.14
print(d)  # Imprime True
print(e)  # Imprime [1, 2, 3]

# Copiar una lista usando el método copy()
new_copy = numbers.copy()
print(new_copy)  # Imprime [10, 2, 3, 4, 5, 6, 7, 8]

# Añadir un elemento al final de una lista usando append()
empty_list.append("Hello")
print(empty_list)  # Imprime ["Hello"]

# Insertar un elemento en una posición específica de la lista usando insert()
numbers.insert(0, 0)
print(numbers)  # Imprime [0, 10, 2, 3, 4, 5, 6, 7, 8]

# Añadir varios elementos a una lista usando extend()
empty_list.extend("Mayer")
print(empty_list)  # Imprime ["Hello", "M", "a", "y", "e", "r"]

# Remover el primer elemento que coincide con el valor especificado usando remove()
print(numbers)  # Imprime [0, 10, 2, 3, 4, 5, 6, 7, 8]
numbers.remove(10)
print(numbers)  # Imprime [0, 2, 3, 4, 5, 6, 7, 8]

# Remover y retornar el último elemento de una lista usando pop()
# También se puede especificar el índice del elemento a remover
last_element = numbers.pop()
print(last_element)  # Imprime 8
print(numbers)  # Imprime [0, 2, 3, 4, 5, 6, 7]

# Eliminar un elemento de una lista por su índice usando del
del numbers[0]
print(numbers)  # Imprime [2, 3, 4, 5, 6, 7]

# Remover todos los elementos de una lista usando clear()
numbers.clear()
print(numbers)  # Imprime []

# Uso del método index() para encontrar la posición de un elemento
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Imprime 1

# Contar las apariciones de un elemento en la lista usando count()
print(fruits.count("apple"))  # Imprime 1

# Ordenar los elementos de una lista usando sort()
fruits.sort()
print(fruits)  # Imprime ['apple', 'banana', 'cherry']

# Invertir el orden de los elementos de una lista usando reverse()
fruits.reverse()
print(fruits)  # Imprime ['cherry', 'banana', 'apple']

# Iterar a través de los elementos de una lista usando un bucle for
for fruit in fruits:
    print(fruit)

# Uso de listas por comprensión para crear una nueva lista basada en una existente
squares = [x**2 for x in range(10)]
print(squares)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
