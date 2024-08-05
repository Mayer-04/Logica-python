"""
* Cadenas de Texto o Strings
- Son secuencias de caracteres
- Con triples comillas dobles o simples podemos crear una cadena con salto de línea
"""

# Se pueden crear usando comillas dobles o simples
print("Python")
print("Python")

# Cadena con salto de línea
print(
    """
    Python
    es un lenguaje 
    de programación
    """
)

# Concatenar strings
print("Python " + "es un lenguaje de programación")

# Multiplicar strings
print("Python " * 3)

# Salto de línea
print("Python\nes un lenguaje de programación")

# Tabulación
print("Python\tes un lenguaje de programación")

# Longitud de una cadena
print(len("Python"))

"""
* Formatear strings
 %s - String
 %d - Entero
 %f - Float
"""
name = "Mayer"
age = 24
active = True

print("Mi nombre es %s, tengo %d años y estoy %s" % (name, age, active))
print("Mi nombre es {}, tengo {} años y estoy {}".format(name, age, active))
# Formateo de una cadena con f - Interpolación de variables
print(f"Mi nombre es {name}, tengo {age} años y estoy {active}")

# Las cadenas son secuencias inmutables
name = "Mayer"
print(name[2])

# Slicing de strings
print(name[1:])

print(name[-1])

# Reversión de strings
print(name[::-1])

## Recorrer strings
for character in name:
    print(character)

"""
* Métodos o funciones de strings
Las funciones que empiezan con is lo que hace es comprobar si una cadena empieza con ese valor
"""
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.count("a"))
print(name.startswith("M"))
print(name.endswith("r"))
print(name.find("y"))
print(name.split())
print(name.replace("y", "a"))
print("Python".isnumeric())
