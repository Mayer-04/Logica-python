"""
* Diccionarios en Python:

- Un diccionario es una estructura de datos que almacena pares clave-valor, donde cada clave es única.
- Se define entre llaves {} y puede contener elementos de cualquier tipo de dato 
(strings, enteros, listas, otros diccionarios, etc.).
- Los diccionarios son mutables, lo que significa que puedes agregar, 
eliminar o modificar pares clave-valor después de su creación.
- Se pueden anidar, es decir, un diccionario puede contener otros diccionarios como valores.
- Los diccionarios son iterables, permitiendo recorrer sus claves, valores o ambos utilizando bucles como `for`.

Operaciones comunes con diccionarios:
- Creación de diccionarios.
- Acceso, adición y eliminación de elementos.
- Iteración sobre diccionarios.
- Métodos comunes como `keys()`, `values()`, `items()`, y `get()`.
"""

# Crear un diccionario vacío usando el constructor dict()
my_dict = dict()
print(my_dict)  # Imprime {} (diccionario vacío)

# Crear un diccionario vacío usando llaves {}
empty_dict = {}
print(empty_dict)  # Imprime {} (diccionario vacío)

# Crear un diccionario con elementos iniciales
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': 3}

# Obtener la longitud de un diccionario (cantidad de pares clave-valor)
print(len(my_dict))  # Imprime 3

# Acceder a los elementos de un diccionario usando claves
print(my_dict["a"])  # Imprime 1 (valor asociado a la clave 'a')
print(my_dict["b"])  # Imprime 2 (valor asociado a la clave 'b')
print(my_dict["c"])  # Imprime 3 (valor asociado a la clave 'c')

# Añadir un nuevo par clave-valor al diccionario
my_dict["d"] = 4
print(my_dict)  # Imprime {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Modificar el valor asociado a una clave existente
my_dict["a"] = 10
print(my_dict)  # Imprime {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Eliminar un elemento del diccionario usando la clave
del my_dict["d"]
print(my_dict)  # Imprime {'a': 10, 'b': 2, 'c': 3}

# Verificar si una clave existe en el diccionario
print("a" in my_dict)  # Imprime True (la clave 'a' está presente)
print("z" in my_dict)  # Imprime False (la clave 'z' no está presente)

# Iterar sobre las claves del diccionario
for key in my_dict:
    print(
        f"Clave: {key}, Valor: {my_dict[key]}"
    )  # Imprime cada clave y su valor asociado

# Iterar solo sobre los valores del diccionario
for value in my_dict.values():
    print(f"Valor: {value}")  # Imprime cada valor del diccionario

# Iterar sobre los pares clave-valor del diccionario
for key, value in my_dict.items():
    print(
        f"Clave: {key}, Valor: {value}"
    )  # Imprime cada clave junto a su valor asociado

# Crear un diccionario anidado (diccionario dentro de otro diccionario)
nested_dict = {"a": 1, "b": 2, "c": {"d": 4, "e": 5}}
print(nested_dict)  # Imprime {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}

# Acceder a un valor dentro de un diccionario anidado
print(nested_dict["c"]["d"])  # Imprime 4 (valor asociado a la clave 'd' dentro de 'c')

# Eliminar un elemento dentro de un diccionario anidado
del nested_dict["c"]["e"]
print(nested_dict)  # Imprime {'a': 1, 'b': 2, 'c': {'d': 4}}

# Métodos comunes de los diccionarios
print(
    nested_dict.keys()
)  # Imprime las claves del diccionario: dict_keys(['a', 'b', 'c'])
print(
    nested_dict.values()
)  # Imprime los valores del diccionario: dict_values([1, 2, {'d': 4}])
print(
    nested_dict.items()
)  # Imprime los pares clave-valor del diccionario: dict_items([('a', 1), ('b', 2), ('c', {'d': 4})])

# Obtener un valor de manera segura usando el método get()
element = nested_dict.get("a")  # Devuelve 1 si la clave "a" existe, sino devuelve None
print(element)  # Imprime 1

# Intentar obtener un valor para una clave inexistente usando get()
element = nested_dict.get("z")  # Devuelve None si la clave "z" no existe
print(element)  # Imprime None

# Usar el método setdefault() para obtener un valor o establecer un valor predeterminado si la clave no existe
element = nested_dict.setdefault("f", 6)  # Añade 'f': 6 si no existe y lo devuelve
print(element)  # Imprime 6
print(nested_dict)  # Imprime {'a': 1, 'b': 2, 'c': {'d': 4}, 'f': 6}
