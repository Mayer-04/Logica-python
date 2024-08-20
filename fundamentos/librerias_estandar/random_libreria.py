import random

"""
* Librería Random

Funciones incorporadas de la librería estandar `random`

- random.randint(): Retorna un número aleatorio entre dos números enteros.
- random.random(): Retorna un número aleatorio entre cero y uno.
- random.choice(): Retorna un elemento aleatorio de una secuencia (lista, tupla, conjunto, etc.).
- random.choices(): Retorna una lista de elementos aleatorios de una secuencia (lista, tupla, conjunto, etc.).
- random.shuffle(): Baraja una lista de elementos aleatoriamente. Modifica la lista original.
"""


# Generar un número aleatorio entre dos números enteros
print(random.randint(1, 10))  # Imprime un número aleatorio entre 1 y 10


# Generar un número aleatorio entre cero y uno
# (0 es excluido y 1 es incluido)
# El valor devuelve es un número de tipo `float`
print(random.random())  # Imprime un número aleatorio entre 0 y 1


# Elegir un elemento aleatorio de una lista
print(random.choice([1, 2, 3, 4, 5]))  # Imprime un elemento aleatorio de la lista


# Elegir una lista de elementos aleatorios de una lista
# El valor `k` es el número de elementos que se quieren obtener
# Los valores aleatorios generados pueden repetirse
print(
    random.choices([1, 2, 3, 4, 5], k=3)
)  # Imprime una lista de 3 elementos aleatorios. Ejemplo: [1, 3, 5]


# Elegir una lista de elementos aleatorios de una tupla
# La tupla la convierte en una lista
print(
    random.choices((1, 2, 3, 4, 5), k=3)
)  # Imprime una lista de 3 elementos aleatorios

# Barajar una lista de elementos aleatorios
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)

# La lista original ahora esta desordenada
print("Lista original:", shuffle_list)