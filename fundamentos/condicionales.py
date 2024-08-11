"""
* Estructuras de control - Condicionales

Las estructuras condicionales permiten que un programa ejecute diferentes bloques de código en función de ciertas
condiciones.

- `if`: Evalúa una condición y, si es verdadera, ejecuta un bloque de código.
- `elif`: Se usa después de un `if` inicial para verificar una nueva condición si la primera es falsa.
Es una abreviación de “else if”.
- `else`: Se ejecuta si todas las condiciones anteriores (`if` y `elif`) son falsas.
- `match`: Introducido en Python 3.10, similar a `switch` en otros lenguajes, 
permite seleccionar un bloque de código para ejecutar basado en el valor de una expresión.

Las condiciones que se evalúan en estas estructuras deben resolverse en valores booleanos 
(`True` o `False`) para determinar el flujo de ejecución.

- Es mala practica poner `pass` dentro de un `else` ya que es redundante.
"""

numero = 5

# Condicional if básico
# Verificamos si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")  # Se ejecuta si la condición es verdadera

# Introducción a las condiciones con 'if' y 'else'
# Este ejemplo verifica si un número es positivo o negativo

numero = -3

# Condición para verificar si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")
else:
    print(
        "El número es negativo o cero."
    )  # Se ejecuta si la condición del 'if' es falsa

# Introducción a las condiciones con 'if', 'elif' y 'else'
# Este ejemplo verifica si un número es positivo, negativo o cero

numero = 0

# Se evalúan múltiples condiciones secuencialmente
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print(
        "El número es cero."
    )  # Se ejecuta si todas las condiciones anteriores son falsas

# Uso de múltiples condiciones con 'if', 'elif' y 'else'
# Este ejemplo clasifica a una persona según su edad

edad = 25

if edad < 12:
    print("Eres un niño.")
elif 12 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 60:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

# Curiosidad: Condiciones en una sola línea con el Operador Ternario
# Sintaxis: <valor_si_true> if <condición> else <valor_si_false>
# Este operador es útil para expresiones cortas y claras

numero = 5
mensaje = (
    "Positivo" if numero > 0 else "No positivo"
)  # Asigna 'Positivo' si la condición es verdadera, de lo contrario 'No positivo'
print(mensaje)  # Imprime 'Positivo'

"""
* Profundizando en el operador ternario:
Si la calificación es 6 o más, se asignará 'Aprobado', de lo contrario 'Reprobado'.
"""
calificacion = 8
condicion = calificacion >= 6
mensaje = "Aprobado" if condicion else "Reprobado"
print(
    mensaje
)  # Imprime 'Aprobado' porque la condición es verdadera (calificación >= 6)

# Uso del operador walrus (:=) - A partir de Python 3.8+
# Este operador permite asignar y evaluar en una misma expresión.
# Útil cuando queremos utilizar una variable tanto en la condición como en el bloque de código

if (n := 10) > 5:
    print(
        f"El número {n} es mayor que 5."
    )  # Asigna 10 a 'n' y verifica si es mayor que 5 en una sola línea


# A partir de Python 3.10: La sentencia match (similar a switch en otros lenguajes)
# match recibe una expresión y compara su valor con uno o más bloques `case`
# Este ejemplo usa 'match' para verificar el estado de una luz de tráfico

color = "verde"

match color:
    case "verde":
        print("Puedes avanzar.")
    case "amarillo":
        print("Precaución.")
    case "rojo":
        print("Detente.")
    case _:
        print(
            "Color desconocido."
        )  # Caso por defecto si ninguno de los anteriores coincide


# Ejemplo 2 con `match` y agrupación de opciones
def http_error(status):
    match status:
        case 400:
            return "Petición incorrecta"
        case (
            401 | 403 | 405
        ):  # Agrupar varias opciones en el mismo `case` con el operador `|`
            return "No autorizado"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Algo anda mal con internet"


print(http_error(404))

# Ejemplo 3 con `match` y tuplas

x = 0
y = 10
point = (x, y)

match point:
    case (0, 0):
        print("En el origen")
    case (0, y):
        print(f"En el eje Y: {y}")
    case (x, 0):
        print(f"En el eje X: {x}")
    case (x, y):
        print(f"En algún lugar: X={x}, Y={y}")
    case _:
        print("No es un punto válido")
