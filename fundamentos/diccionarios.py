"""
Diccionarios en Python:

- Un diccionario es una colección desordenada de elementos que se almacenan como pares clave-valor.
- Se definen entre llaves {}.
- Pueden contener elementos de cualquier tipo de datos.
- Son mutables, es decir, se pueden modificar después de ser creados.
- Se pueden anidar, lo que significa que un diccionario puede contener otros diccionarios.
- Se pueden iterar utilizando bucles como for.

Operaciones comunes con diccionarios:
- Creación de diccionarios.
- Acceso, adición y eliminación de elementos.
- Iteración sobre diccionarios.
- Métodos comunes como keys(), values(), items(), y get().
"""

# Constructor de diccionarios vacíos
my_dict = dict()

# Crear un diccionario vacío usando llaves
ompt_dict = {}
print(ompt_dict)  # Imprime {}

# Creando un diccionario con elementos
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': 3}

# Longitud de un diccionario
print(len(my_dict))  # Imprime 3

# Accediendo a los elementos de un diccionario usando claves
print(my_dict["a"])  # Imprime 1
print(my_dict["b"])  # Imprime 2
print(my_dict["c"])  # Imprime 3

# Añadiendo elementos a un diccionario
my_dict["d"] = 4
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Eliminando elementos de un diccionario
del my_dict["d"]
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': 3}

# Iterando sobre un diccionario
for key in my_dict:
    print(key)  # Imprime las claves del diccionario
    print(my_dict[key])  # Imprime los valores del diccionario

# Iterando sobre los valores de un diccionario
for value in my_dict.values():
    print(value)

# Iterando sobre las claves y los valores de un diccionario
for key, value in my_dict.items():
    print(key, value)

# Creando un diccionario anidado
my_dict = {"a": 1, "b": 2, "c": {"d": 4, "e": 5}}
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}

# Accediendo a los elementos de un diccionario anidado
print(my_dict["c"]["d"])  # Imprime 4

# Eliminando elementos de un diccionario anidado
del my_dict["c"]["e"]
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': {'d': 4}}

# Verificar si un elemento está presente en un diccionario
print("a" in my_dict)  # Imprime True
print("z" in my_dict)  # Imprime False

# Métodos comunes de los diccionarios
print(my_dict.keys())  # Imprime las claves del diccionario: dict_keys(['a', 'b', 'c'])
print(
    my_dict.values()
)  # Imprime los valores del diccionario: dict_values([1, 2, {'d': 4}])
print(
    my_dict.items()
)  # Imprime los pares clave-valor del diccionario: dict_items([('a', 1), ('b', 2), ('c', {'d': 4})])

# Obtener un valor de manera segura usando el método get()
element = my_dict.get("a")  # Devuelve 1 si la clave "a" existe, sino devuelve None
print(element)  # Imprime 1

# Intentar obtener un valor para una clave inexistente con get()
element = my_dict.get("z")  # Devuelve None si la clave "z" no existe
print(element)  # Imprime None
