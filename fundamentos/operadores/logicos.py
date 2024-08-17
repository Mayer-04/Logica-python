"""
* Operadores Lógicos
- Se utilizan para tomar una decisión basada en múltiples condiciones.
- Actuan sobre valores booleanos (`True` o `False`).
- Son aplicables a todos los objetos de Python.
"""

number = 5

# and - y
# Devuelve el primer valor falso que encuentra, o el último valor si todos son verdaderos.
print(number > 0 and number < 10)

# or - o
# Devuelve el primer valor verdadero que encuentra, o el último valor si todos son falsos.
print(number > 0 or number < 10)

# not - no
# Devuelve el valor opuesto, si es verdadero devuelve falso y viceversa.
print(not number > 0)
