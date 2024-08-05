"""
sets: Conjuntos

- Es una colección desordenada de elementos.
- Los elementos no se pueden repetir, son únicos y mutables.
- Se definen entre llaves {} o usando la función set().
- Pueden contener elementos de cualquier tipo de datos.
- No es una estructura ordenada.
- Internamente utiliza un hashmap para la búsqueda rápida.

Operaciones comunes con sets:
- Creación de sets.
- Añadir y eliminar elementos.
- Comprobar existencia de elementos.
- Operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.
"""

# Creación de un set vacío con el constructor set()
new_set = set()

# Inicialmente Python trata las llaves vacías {} como un diccionario
opmt_set = {}
print(opmt_set)  # Imprime {}
print(type(opmt_set))  # Imprime <class 'dict'>

# Conversión de un diccionario vacío a un set
opmt_set = {1, 2, 3, 4, 5}
print(opmt_set)  # Imprime {1, 2, 3, 4, 5}
print(type(opmt_set))  # Imprime <class 'set'>

# Añadir elementos a un set
new_set.add("Andres")
print(new_set)  # Imprime {'Andres'}

# Intentar agregar un elemento duplicado no cambia el set
new_set.add("Andres")
print(new_set)  # Imprime {'Andres'}

# Añadir múltiples elementos a un set
new_set.update([1, 2, 3])
print(new_set)  # Imprime {'Andres', 1, 2, 3}

# Crear una copia de un set
copy_set = new_set.copy()
print(copy_set)  # Imprime {'Andres', 1, 2, 3}

# Eliminar un elemento de un set si existe
new_set.remove("Andres")
print(new_set)  # Imprime {1, 2, 3}

# Eliminar un elemento sin generar un error si no existe
new_set.discard("Andres")
print(new_set)  # Imprime {1, 2, 3}

# Comprobar si un elemento existe en un set
print("Andres" in new_set)  # Imprime False
print(1 in new_set)  # Imprime True

# Recorrer un set
for element in new_set:
    print(element)

# Limpiar un set
new_set.clear()
print(new_set)  # Imprime set()

# Unión de sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)  # Imprime {1, 2, 3, 4, 5}

# Unión de dos sets con el operador |
set_operator = set1 | set2
print("set_operator:", set3)  # Imprime {1, 2, 3, 4, 5}

# Intersección de sets
set4 = set1.intersection(set2)
print(set4)  # Imprime {3}

# Intersección de dos sets con el operador &
set_intersection = set1 & set2
print("set_intersection:", set3)  # Imprime {3}

# Diferencias de sets
set5 = set1.difference(set2)
print(set5)  # Imprime {1, 2}

# Diferencia simétrica de sets (elementos que están en set1 o en set2 pero no en ambos)
set6 = set1.symmetric_difference(set2)
print(set6)  # Imprime {1, 2, 4, 5}

# Subset y Superset
set7 = {1, 2}
print(set7.issubset(set1))  # Imprime True (set7 es un subconjunto de set1)
print(set1.issuperset(set7))  # Imprime True (set1 es un superconjunto de set7)

# Los frozensets son conjuntos inmutables, una vez creados, no se pueden modificar.
# Conjunto de elementos desordenados únicos e inmutables.
conjunto_inmutable = frozenset([1, 2, 3, 4])
print("Frozenset:", conjunto_inmutable)
