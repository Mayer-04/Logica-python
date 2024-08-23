"""
* None

Es un valor especial que representa la ausencia de un valor o un valor nulo, 
pero no es considerado un tipo de dato básico como cadenas, booleanos o enteros.

- Es usado para indicar la `ausencia de un valor` o un `valor nulo`.
- Las variables pueden ser inicializadas con None para indicar que no se le ha asignado un valor aún.
- Si una función en Python no tiene una sentencia return por defecto devuelve None.
- el objeto None ocupa espacio en memoria, y la variable que apunta a None también ocupa espacio.
- None se considera como `False` en el contexto booleano
"""

# Definiendo una variable que no contiene un valor - None
my_var = None

# Imprimiendo la variable
print(my_var)  # Imprime None

# Tipo de dato de la variable
print(type(my_var))  # Imprime <class 'NoneType'>
