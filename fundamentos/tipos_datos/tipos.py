"""
Anotaciones de tipo en Python (Type Annotations)
-------------------------------------------------
Las anotaciones de tipo permiten especificar los tipos de datos que se espera que tengan 
las variables, los parámetros de las funciones y los valores de retorno. 

Beneficios:
- Mejoran la legibilidad del código y sirven como documentación explícita.
- Facilitan la detección de errores en editores de código que soportan análisis estático 
(por ejemplo, PyCharm) nos dara una advertencia en tiempo de ejecución.
- Aunque Python no impone el uso estricto de tipos en tiempo de ejecución.
- Las anotaciones son útiles para herramientas como linters, así como para otros programadores que lean el código.

Nota:
Python no valida los tipos en tiempo de ejecución, 
por lo que las anotaciones no impiden asignar un tipo de dato incorrecto.
"""

# Variable sin anotación de tipo (dinámica)
# Esta variable podría cambiar a cualquier tipo de dato más adelante
no_tipado = "Texto sin tipo específico"

# Variable con anotación de tipo
tipado: str = "Texto tipado"  # Se indica que 'tipado' debería ser una cadena (str)

# A pesar de la anotación de tipo, Python permite cambiar el tipo de dato en tiempo de ejecución
tipado = 1  # Esto no genera un error en Python
print(f"tipado: {tipado}")  # Output: 1

# Ejemplo con una lista de strings
my_list: list[str] = ["uno", "dos", "tres"]
print(f"my_list: {my_list}")  # Output: my_list: ['uno', 'dos', 'tres']

# Ejemplo con una tupla de enteros
my_tuple: tuple[int, int, int] = (1, 2, 3)
print(f"my_tuple: {my_tuple}")  # Output: my_tuple: (1, 2, 3)

# Ejemplo con un diccionario
my_dict: dict[str, int] = {"uno": 1, "dos": 2, "tres": 3}
print(f"my_dict: {my_dict}")  # Output: my_dict: {'uno': 1, 'dos': 2, 'tres': 3}


# Ejemplo de función con anotaciones de tipo
def suma(a: int, b: int) -> int:
    """Suma dos números enteros.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        int: La suma de los dos números.
    """
    return a + b


resultado = suma(1, 2)
print(f"Resultado de la suma: {resultado}")  # Output: Resultado de la suma: 3


# Ejemplo de anotaciones en funciones que no retornan valor (None)
def imprimir_mensaje(mensaje: str) -> None:
    """Imprime un mensaje en la consola.

    Args:
        mensaje (str): Mensaje a imprimir.
    """
    print(mensaje)


imprimir_mensaje("Hola, anotaciones de tipo!")  # Output: Hola, anotaciones de tipo!


# Ejemplo de anotaciones de tipo con clases
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def saludar(self) -> str:
        """Devuelve un saludo personalizado."""
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."


persona = Persona("Mayer", 24)
print(persona.saludar())  # Output: Hola, mi nombre es Mayer y tengo 24 años.
