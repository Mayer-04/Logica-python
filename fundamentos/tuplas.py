"""
* Tuplas en Python

- Un conjunto ordenado de elementos.
- Se definen entre paréntesis ().
- Pueden contener elementos de cualquier tipo de datos.
- Son inmutables, es decir, no se pueden modificar después de ser creadas.
- No se pueden eliminar elementos de una tupla.
- Se pueden utilizar para almacenar colecciones de datos que no deben cambiar.
- Son más eficientes en términos de memoria y tiempo de ejecución en comparación con las listas.

Métodos comunes de las tuplas:
- count(x): Retorna el número de veces que el valor especificado aparece en la tupla.
- index(): Retorna el índice de la primera aparición del valor especificado.

"""

# Crear una tupla vacía utilizando la función tuple()
my_tuple = tuple()
print(my_tuple)  # Imprime ()

# Crear una tupla vacía utilizando paréntesis
empty_tuple = ()
print(empty_tuple)  # Imprime ()

# Crear una tupla con elementos
numbers = (1, 2, 3, 4)
print(numbers)  # Imprime (1, 2, 3, 4)

# Acceder a los elementos de una tupla usando índices
print(numbers[0])  # Imprime el primer elemento: 1
print(numbers[-1])  # Imprime el último elemento: 4

# Desestructurar una tupla en variables individuales
a, b, c, d = numbers
print(a)  # Imprime 1
print(b)  # Imprime 2
print(c)  # Imprime 3
print(d)  # Imprime 4

# Métodos de tuplas

# Contar las apariciones de un elemento en la tupla usando count()
print(numbers.count(3))  # Imprime 1

# Encontrar el índice de un elemento en la tupla usando index()
print(numbers.index(3))  # Imprime 2

# Obtener la longitud de una tupla usando len()
print(len(numbers))  # Imprime 4

# Concatenar dos tuplas utilizando el operador +
new_tuple = numbers + (5, 6, 7)
print(new_tuple)  # Imprime (1, 2, 3, 4, 5, 6, 7)

# Repetir los elementos de una tupla utilizando el operador *
new_copy = numbers * 3
print(new_copy)  # Imprime (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# Obtener una sub-tupla usando slicing
print(new_copy[:4])  # Imprime (1, 2, 3, 4)

# Convertir una tupla a lista usando list()
new_list = list(numbers)
print(new_list)  # Imprime [1, 2, 3, 4]

# Crear una tupla con un solo elemento (es necesario usar una coma)
single_element_tuple = (42,)
print(single_element_tuple)  # Imprime (42,)

# Comprobar si un elemento existe en una tupla utilizando in
print(3 in numbers)  # Imprime True
print(5 in numbers)  # Imprime False

# Iterar a través de los elementos de una tupla usando un bucle for
for number in numbers:
    print(number)

# Usar tuplas como claves en diccionarios (ya que son inmutables)
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris"
}
print(locations)