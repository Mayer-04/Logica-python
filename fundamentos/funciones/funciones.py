"""
* Funciones en Python

Una función es un bloque de código reutilizable que realiza una tarea específica. 
Las funciones permiten dividir el código en módulos más manejables, promoviendo la reutilización y la legibilidad.

- Declaración de funciones
- Parámetros y argumentos
- Valores por defecto
- Funciones anónimas (lambdas)
- Funciones como objetos de primera clase
- Desempaquetado de argumentos
- Anotaciones de funciones (type hints)
"""


# Declaración de funciones
# Una función se define usando la palabra clave `def`, seguida del nombre de la función y paréntesis.
def saludar():
    """Esta función imprime un mensaje de saludo."""
    print("¡Hola, mundo!")


# Llamada a la función
saludar()


# Parámetros y argumentos
# Las funciones pueden recibir datos a través de parámetros,
# que se pasan como argumentos cuando se llama a la función.
def saludar_a(nombre):
    """Esta función imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}!")


# Llamada a la función con un argumento
saludar_a("Carlos")

# Valores por defecto
# Puedes definir valores por defecto para los parámetros.
# Si no se proporciona un argumento, se usará el valor por defecto.


def saludar_con_titulo(nombre, titulo="Sr./Sra."):
    """Esta función imprime un saludo personalizado con un título."""
    print(f"¡Hola, {titulo} {nombre}!")


# Usando el valor por defecto
saludar_con_titulo("Gómez")

# Sobrescribiendo el valor por defecto
saludar_con_titulo("Gómez", "Dr.")


# Funciones con múltiples parámetros
def calcular_area_rectangulo(base, altura):
    """Esta función calcula el área de un rectángulo."""
    return base * altura


# Llamada a la función con múltiples argumentos
area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area}")


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
