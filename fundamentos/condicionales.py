"""
Condicionales

- if
- elif
- else

La condición que se evalua se convierte en un valor booleano para ser evaluado.
Si el valor booleano es True, el programa continuará ejecutando el código que se encuentra dentro del if.
"""

# Condicional if
numero = 5

# Verificamos si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")

# Introducción a las condiciones con 'if' y 'else'
# Este ejemplo verifica si un número es positivo o negativo

numero = -3

# Verificamos si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")


# Introducción a las condiciones con 'if', 'elif' y 'else'
# Este ejemplo verifica si un número es positivo, negativo o cero

numero = 0

# Verificamos si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


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


# Curiosidad: Condiciones en una sola línea (Ternary operator)
# Sintaxis: <valor_si_true> if <condición> else <valor_si_false>
# Uso del operador ternario
numero = 5
mensaje = "Positivo" if numero > 0 else "No positivo"
print(mensaje)


# A partir de Python 3.10: La sentencia match (similar a switch en otros lenguajes)
# Introducción a las condiciones con 'match'
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
        print("Color desconocido.")


# Uso del operador walrus - A partir de Python 3.8+
# Puedes usar el operador := para asignar y evaluar en una misma expresión.
if (n := 10) > 5:
    print(f"El número {n} es mayor que 5.")
