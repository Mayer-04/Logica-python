"""
Funciones en Python

Una función es un bloque de código reutilizable que realiza una tarea específica. 
Las funciones permiten dividir el código en módulos más manejables, promoviendo la reutilización y la legibilidad.

- La sentencia return retorna un valor en una función. return sin una expresión como argumento retorna `None`. 

En este archivo, se exploran los siguientes conceptos:
- Declaración de funciones
- Parámetros y argumentos
- Valores por defecto
- Funciones anónimas (lambdas)
- Funciones como objetos de primera clase (closures)
- Desempaquetado de argumentos
- Anotaciones de funciones (type hints)
- Recursividad
- Argumentos por nombre y arbitrarios
- Uso de la sentencia `pass`
- Retorno de múltiples valores
- Callbacks
"""


# Declaración de funciones
# Una función se define usando la palabra clave `def`, seguida del nombre de la función y paréntesis.
def saludar():
    """Imprime un mensaje de saludo."""
    print("¡Hola, mundo!")


# Llamada a la función `saludar` sin argumentos.
saludar()


# Parámetros y argumentos
# Las funciones pueden recibir datos a través de parámetros,
# que se pasan como argumentos cuando se llama a la función.
def saludar_a(nombre):
    """Imprime un saludo personalizado utilizando el nombre proporcionado como argumento."""
    print(f"¡Hola, {nombre}!")


# Llamada a la función `saludar_a` pasando un argumento.
saludar_a("Mayer")


# Valores por defecto
# Puedes definir valores por defecto para los parámetros.
# Si no se proporciona un argumento, se usará el valor por defecto.
def saludar_con_titulo(nombre, titulo="Sr./Sra."):
    """Imprime un saludo personalizado utilizando un título y nombre.

    Parámetros:
    nombre (str): El nombre de la persona a saludar.
    titulo (str, opcional): El título a utilizar. Por defecto es 'Sr./Sra.'.
    """
    print(f"¡Hola, {titulo} {nombre}!")


# Usando el valor por defecto para `titulo`.
saludar_con_titulo("Gómez")

# Sobrescribiendo el valor por defecto para `titulo`.
saludar_con_titulo("Gómez", "Dr.")


# Funciones con múltiples parámetros
# Las funciones pueden tener múltiples parámetros para manejar más datos.
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dados la base y la altura.

    Parámetros:
    base (float): La longitud de la base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorno:
    float: El área del rectángulo.
    """
    return base * altura


# Llamada a la función `calcular_area_rectangulo` con múltiples argumentos.
area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area}")


"""
Funciones lambda
    - Una función lambda es una función anónima, es decir, que no tiene nombre.
    - Son útiles cuando se necesita una función simple y rápida.
    - Se suelen usar en combinaciones con funciones como `map()`, `filter()` y `reduce()`.
"""

# Definiendo una función lambda para sumar dos números.
sumar_lambda = lambda num1, num2: num1 + num2

# Usando la función lambda.
result_lambda = sumar_lambda(1, 2)
print("Resultado Lambda:", result_lambda)


# Funciones anidadas (Closures)
# Una función anidada es una función definida dentro de otra función.
def funcion_externa(x):
    """Contiene una función interna que utiliza la variable `x` de la función externa."""

    def funcion_interna(y):
        """Suma `x` y `y`, donde `x` proviene de la función externa."""
        return x + y

    # Retorna la función interna, formando un closure.
    return funcion_interna


# Usando la función anidada.
suma_10 = funcion_externa(10)
resultado = suma_10(5)  # Llama a `funcion_interna(5)`, donde `x` es 10.
print(f"El resultado de la función anidada es: {resultado}")


# Función recursiva
# Una función recursiva es aquella que se llama a sí misma.
def factorial(num):
    """Calcula el factorial de un número de manera recursiva.

    Parámetro:
    num (int): Un entero positivo cuyo factorial se quiere calcular.

    Retorno:
    int: El factorial de `num`.
    """
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# Calculando el factorial de 5.
print(factorial(5))  # Imprime: 120


# Argumentos por nombre (keyword arguments)
# Python permite llamar a las funciones especificando los argumentos por nombre,
# lo cual permite ignorar el orden de los parámetros.
def describir_persona(nombre, edad):
    """Imprime la descripción de una persona con su nombre y edad."""
    print(f"Nombre: {nombre}, Edad: {edad}")


# Llamando a la función `describir_persona` con argumentos por nombre.
describir_persona(edad=30, nombre="Maria")


# Función con parámetros arbitrarios (kwargs)
# Python permite recibir un número indeterminado de parámetros usando `**kwargs`,
# que crea un diccionario con los argumentos pasados por nombre.
def indeterminados_nombre(**kwargs):
    """Imprime los argumentos recibidos como pares clave-valor."""
    print(kwargs)


# Llamando a la función `indeterminados_nombre` con varios argumentos por nombre.
indeterminados_nombre(n=5, c="Hola Andres", l=[1, 2, 3, 4, 5])


# Funciones con parámetros arbitrarios (args)
# De forma similar, se puede recibir un número indeterminado de argumentos posicionales con `*args`.
def saludar_varios(*args):
    """Saluda a todas las personas cuyos nombres se pasan como argumentos."""
    for name in args:
        print(f"Hola {name}")


# Llamando a la función `saludar_varios` con múltiples nombres.
saludar_varios("Mayer", "Andrés", "Carlos")


# Sentencia pass
# La sentencia `pass` en Python no hace nada. Se usa como un marcador de posición en el código.
def pass_func():
    """Función que no realiza ninguna acción, útil como marcador de posición."""
    pass  # No hace nada


# Llamando a la función `pass_func` que no realiza ninguna acción.
pass_func()


# Retornar múltiples valores
# Python permite retornar múltiples valores desde una función, separados por comas.
# Los valores retornados se empaquetan automáticamente en una tupla.
def prueba():
    """Retorna una cadena, un entero y una lista."""
    return "Andres CMS", 20, [1, 2, 3]


# Llamando a la función `prueba` y desempaquetando los valores retornados.
resultado = prueba()
print(resultado)  # Imprime: ('Andres CMS', 20, [1, 2, 3])


# Callbacks - Funciones que se pasan como argumentos
# Se puede pasar una función como argumento a otra función, permitiendo la creación de callbacks.
def ejecutar_callback(func, valor):
    """Ejecuta una función (callback) pasada como argumento.

    Parámetros:
    func (function): La función a ejecutar.
    valor (any): El valor a pasar como argumento a la función `func`.

    Retorno:
    any: El resultado de ejecutar `func` con `valor`.
    """
    return func(valor)


# Ejemplo de uso de callback.
def mostrar_doble(numero):
    """Muestra el doble de un número."""
    print(numero * 2)


ejecutar_callback(mostrar_doble, 10)  # Imprime: 20


# Decoradores
# Los decoradores son funciones que se pueden utilizar para modificar el comportamiento de otras funciones.
