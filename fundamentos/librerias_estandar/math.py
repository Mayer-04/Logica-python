import math

"""
* Librería Math

Funciones incorporadas de la librería estandar `math`

- math.sqrt: Retorna la raiz cuadrada de un número.
- math.pow: Retorna el valor de `x` elevado a la potencia `y`.
- math.pi: Retorna el valor de `pi`.
- math.e: Retorna el valor del número de Euler.
- math.log: Retorna el logaritmo natural de un número.
- math.log10: Retorna el logaritmo base 10 de un número.
- math.sin: Retorna el seno de un número.
- math.cos: Retorna el coseno de un número.
- math.tan: Retorna la tangente de un número.
- math.degrees: Convierte un angulo en grados a radianes.
- math.radians: Convierte un angulo en radianes a grados.
- math.ceil: Redondea un número hacia arriba.
- math.floor: Redondea un número hacia abajo.
- math.trunc: Elimina los decimales de un número.
- math.factorial: Retorna el factorial de un número.

Utilice `help(math)` para obtener detalles sobre la librería `math`.
"""

# Constantes

# Constante `pi`
# Retorna el valor de `pi`.
print(math.pi)  # Salida: 3.141592653589793

# Constante `e`
# Retorna el valor del número de Euler
print(math.e)  # Salida: 2.718281828459045

# Constante `nan`
# Representa un número que no está definido. "Not a Number".
print(math.nan)  # Salida: nan

# Constante `inf`
# Representa un número infinito. "Infinity".
print(math.inf)  # Salida: inf

# Función `trunc`
# Elimina la parte decimal de un número.
# Devuelve la parte entera.
print(math.trunc(2.5))  # Salida: 2

# Función `ceil`
# Redondea un número hacia arriba.
print(math.ceil(2.5))  # Salida: 3

# Función `floor`
# Redondea un número hacia abajo.
print(math.floor(2.5))  # Salida: 2

# Función `abs`
# Retorna el valor absoluto de un número.
# Es una función nativa de Python y no pertenece a la librería math.
print(abs(-5))  # Salida: 5

# Función `factorial`
# Retorna el factorial de un número.
print(math.factorial(5))  # Salida: 120

# Función `fabs`
# Retorna el valor absoluto de un número como un número flotante.
print(math.fabs(-5))  # Salida: 5.0

# Función `sqrt`
# Retorna la raiz cuadrada de un número.
print(math.sqrt(4))  # Salida: 2.0

# Función `pow`
# Retorna el valor de `x` elevado a la potencia `y`.
# El valor retornado es un número flotante.
print(math.pow(2, 3))  # Salida: 8.0

# Función `log`
# Retorna el logaritmo natural de un número.
print(math.log(10))  # Salida: 2.302585092994046

# Función `log10`
# Retorna el logaritmo base 10 de un número.
print(math.log10(100))  # Salida: 2.0

# Función `sin`
# Retorna el seno de un número.
print(math.sin(math.radians(90)))  # Salida: 1.0

# Función `cos`
# Retorna el coseno de un número.
print(math.cos(math.radians(180)))  # Salida: -1.0

# Función `tan`
# Retorna la tangente de un número.
print(math.tan(math.radians(45)))  # Salida: 1.0

# Función `degrees`
# Convierte un angulo en grados a radianes.
print(math.degrees(math.pi))  # Salida: 180.0
