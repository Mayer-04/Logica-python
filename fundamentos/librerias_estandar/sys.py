from sys import getsizeof

"""
* sys - Módulo para interactuar con el sistema operativo
La función `getsizeof` se utiliza para obtener el tamaño de un objeto en bytes.
"""

# Tamaño de una cadena
cadena = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
print("Tamaño de la cadena:", getsizeof(cadena), "Bytes")

# Tamaño de una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Tamaño de la lista:", getsizeof(lista), "Bytes")

# Tamaño de una tupla
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tamaño de la tupla:", getsizeof(tupla), "Bytes")

# Tamaño de un conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Tamaño del conjunto:", getsizeof(conjunto), "Bytes")

# Tamaño de un diccionario
diccionario = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
}
print("Tamaño del diccionario:", getsizeof(diccionario), "Bytes")

# Tamaño de un rango
rango = range(1, 11)
print("Tamaño del rango:", getsizeof(rango), "Bytes")
