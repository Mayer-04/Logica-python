""""
Variables
- En Python no es necesario utilizar palabras reservadas para declarar variables
- La convencion es usar snake_case para las variables
- Las variables hay que verlas como etiquetas
- Los nombres de las variables deben ser descriptivos
- Palabras reservadas: Palabras que no podemos usar para nombrar nuestras variables porque ya Python las utiliza.
"""

a = 2
b = 5
mi_nombre = "Mayer"

# f strings
resultado = f"El resultado de {a} y {b} es: {a+b}"

# Declarar múltiples variables en una sola línea
c, d, e = 1, 2, 3


# Usar una variable con alcance global
new_variable = "Andres"


def my_function():
    global new_variable
    new_variable = "Mayer"
    print(new_variable)


my_function()
print(new_variable)

"""
Constantes
- En Python no existen constantes.
- Por convención las constantes se escriben en mayúsculas.
- Solo se pueden usar para lectura y no escritura
"""

MY_NAME = "Mayer"
