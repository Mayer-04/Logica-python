"""
Funciones en Python

- Una función es un conjunto de instrucciones que realizan una tarea específica.
- Se escribe con la palabra clave def y el nombre de la función.
- Pueden retornar un valor de salida.
- Se pueden utilizar como argumentos de otras funciones.
"""


# Definiendo una función
def saludar():
    print("Hola mundo")


# Llamando a la función
saludar()


# Funciones con parámetros
def saludar2(name):
    """

    Args:
        name (_type_): _description_
    """
    print(f"Hola {name}")


saludar2("Mayer")


# Funciones con parámetros por defecto
def saludar3(name="Mayer"):
    print(f"Hola {name}")


saludar3("Andres")
saludar3()  # Imprime: Hola Mayer


# Funciones que devuelven o retornan valores
def sumar(num1, num2):
    """Devuelve la suma de a y b."""
    return num1 + num2


# Guardamos lo retornado en una variable
result = sumar(1, 2)
print("Result:", result)


"""
Funciones lambda
    - Una función lambda es una función que no tiene nombre (anónimas).
    - Es una función anonima que se puede pasar como argumento a otras funciones.
    - Pueden retornar un valor de salida.
    - Son utiles en combinación con funciones como map(), filter() y reduce().
"""


sumar_lambda = lambda num1, num2: num1 + num2

result_lambda = sumar_lambda(1, 2)
print("Result Lambda:", result_lambda)


# Funciones animadas (Closures)
def funcion_externa(x):
    """Esta función contiene una función anidada."""

    def funcion_interna(y):
        return x + y

    return funcion_interna


# Usando la función anidada
suma_10 = funcion_externa(10)
resultado = suma_10(5)
print(f"El resultado de la función anidada es: {resultado}")


# Función recursiva
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))  # Imprime: 120


# Argumentos por nombre
# Ppermite ignorar el orden en el que se definen los parámetros y hacer el código más claro
def describir_persona(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")


describir_persona(edad=30, nombre="Ana")


# Función con parámetros arbitrarios **
# número indeterminado de parámetros por nombre clave-valor
# Creando un diccionario dinamico con **
def indeterminados_nombre(**kwargs):
    print(kwargs)


indeterminados_nombre(n=5, c="Hola Plone", l=[1, 2, 3, 4, 5])


# Funciones con parámetros arbitrarios
# Parámetros arbitrarios: Se pueden pasar cualquier número de argumentos a una función con *
def saludar4(*args):
    for name in args:
        print(f"Hola {name}")


saludar4("Mayer", "Andres", "Carlos")


# Sentencia pass
# La sentencia pass en Python no hace nada. Es una sentencia vacía que no hace nada.
def pass_func():
    pass  # No hace nada


pass_func()


# Retornar multiples valores, separados por comas
# Los valores multiples se retornan como una tupla y se pueden reasignar a diferentes variables
def prueba():
    return "Plone CMS", 20, [1, 2, 3]


prueba()  # Imprime: ('Plone CMS', 20, [1, 2, 3])


# Callbacks - Funciones que se pasan como argumentos
