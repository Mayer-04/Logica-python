"""
Funciones incorporadas en Python

- Funciones incorporadas son funciones predefinidas que se encuentran dentro del lenguaje.
- Se pueden utilizar para realizar operaciones matemáticas, realizar calculos, etc.

"""

# Función incorporada print
# Imprime una cadena de texto
print("Hola mundo")

# Función incorporada type
# Retorna el tipo de dato de un objeto
print(type("Hola mundo"))

# Función incorporada len
# Retorna la longitud de una cadena de texto
print(len("Hola mundo"))

# Función incorporada max
# Retorna el número maximo de una lista de elementos
print(max([1, 2, 3, 4, 5]))

# Función incorporada min
# Retorna el número minimo de una lista de elementos
print(min([1, 2, 3, 4, 5]))

# Función incorporada sum
# Retorna la suma de una lista de elementos
print(sum([1, 2, 3, 4, 5]))

# Función incorporada range
# Crea una lista de elementos con un rango de valores
print(list(range(1, 6)))

# Función incorporada abs
# Retorna el valor absoluto de un número
print(abs(-5))

# Función incorporada pow
# Retorna el valor de una potencia
print(pow(2, 3))


# Función incorporada round
# Redondea un número
print(round(3.14159265358979323846, 2))

# Función incorporada reversed
# Invierte el orden de una lista
print(list(reversed([1, 2, 3, 4, 5])))


# Función incorporada filter
# Filtra elementos de una lista por una condición dada por una función
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))


# Función incorporada map
# Aplica una función a cada elemento de una lista
print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5, 6])))


# Función incorporada help
# Muestra la documentación de una función
help(print)

# Función incorporada input
# Permite al usuario introducir datos en la consola
print(input("Introduce tu nombre: "))
