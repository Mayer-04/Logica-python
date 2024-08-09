"""
* Variables y Constantes en Python

- En Python, no es necesario utilizar palabras reservadas para declarar variables.
- La convención de nombres para las variables en Python es usar snake_case (minúsculas con guiones bajos).
- Las variables pueden ser vistas como etiquetas que referencian valores.
- Los nombres de las variables deben ser descriptivos para mejorar la legibilidad del código.
- Palabras reservadas: Son términos reservados por Python que no se pueden usar como nombres de variables.
"""

# Declaración de variables
a = 2  # Variable de tipo entero (int)
b = 5  # Variable de tipo entero (int)
mi_nombre = "Mayer"  # Variable de tipo cadena de texto (str)

# Uso de f-strings para formatear cadenas de texto con variables
resultado = f"El resultado de sumar {a} y {b} es: {a + b}"
print(resultado)  # Imprime el resultado de la suma de 'a' y 'b'

# Declaración múltiple de variables en una sola línea
c, d, e = 1, 2, 3  # Variables de tipo entero (int)

# Es una buena práctica declarar variables en líneas separadas para mayor claridad, pero en casos simples
# se puede hacer en una sola línea como en el ejemplo anterior.

# Intercambiar valores entre variables
x, y = 10, 20  # Asignación múltiple
x, y = y, x  # Intercambio de valores entre 'x' y 'y'
print(
    f"Después del intercambio, x = {x}, y = {y}"
)  # Imprime los valores intercambiados

# Uso de variables globales
# En general, el uso de variables globales se debe evitar a menos que sea necesario, ya que puede
# dificultar la comprensión y el mantenimiento del código.
new_variable = "Andres"  # Variable global


def my_function():
    """
    Esta función modifica la variable global 'new_variable' y la imprime.
    Es importante declarar la variable como 'global' para modificar su valor dentro de la función.
    """
    global new_variable  # Indica que se usará la variable global
    new_variable = "Mayer"  # Modifica el valor de la variable global
    print(
        f"Valor de 'new_variable' dentro de la función: {new_variable}"
    )  # Imprime el nuevo valor de la variable global


my_function()
# Llama a la función que modifica y muestra 'new_variable'
print(f"Valor de 'new_variable' fuera de la función: {new_variable}")
# Imprime el valor final de la variable global

"""
* Constantes

- En Python no existen constantes verdaderas. Sin embargo, se pueden definir utilizando convenciones.
- Por convención, las constantes se escriben en mayúsculas y se deben usar solo para lectura, no para escritura.
- Las constantes ayudan a indicar que ciertos valores no deben ser modificados durante la ejecución del programa.
"""

MY_NAME = "Mayer"  # Constante (por convención, se usa en mayúsculas)
print(f"Mi nombre es: {MY_NAME}")  # Imprime el valor de la constante

# Intento de modificar una constante
# Aunque no es recomendable, técnicamente se puede modificar el valor de una "constante" en Python.
# Esto es solo para fines ilustrativos y no es una práctica recomendada.

MY_NAME = "Andres"  # No recomendado: Modificar una "constante"
print(
    f"Mi nuevo nombre es: {MY_NAME}"
)  # Imprime el nuevo valor, lo cual muestra la flexibilidad de Python
