"""
* Anotaciones de tipos (type hints) son una forma de anotar el tipo de un valor. 
Se utilizan para mejorar la legibilidad y la comprensión del código.

-  Usar anotaciones de tipos mejora la legibilidad y facilita la detección de errores
"""

no_tipado = "No tipado"

# Forzamos el tipo de dato de la variable - anotaciones de tipos
tipado: str = "Tipado"

# Cambiamos el tipo de dato de la variable - No genera error
tipado = 1
print(tipado)


# Anotaciones de tipos en funciones
def suma(a: int, b: int) -> int:
    return a + b


resultado = suma(1, 2)
print("resultado: ", resultado)
