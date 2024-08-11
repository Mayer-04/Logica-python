"""
* Estructuras de control - Bucles en Python

Los bucles permiten repetir un bloque de código varias veces según una condición.
Python tiene dos tipos principales de bucles:

- `while`: Repite el bloque de código mientras una condición (expresión) sea verdadera.
- `for`: Itera sobre una secuencia (como una lista, tupla, diccionario, string o rango), 
en el orden que aparecen en la secuencia y ejecuta un bloque de código por cada elemento.

Además, Python ofrece las siguientes herramientas adicionales para el control de bucles:

- `break`: Termina el bucle antes de que se complete normalmente.
- `continue`: Salta el resto del código dentro del bucle y pasa a la siguiente iteración.
- `else`: Ejecuta un bloque de código al final del bucle, pero solo si el bucle no se interrumpió con `break`.
- En un bucle `for`, la cláusula `else` se ejecuta después de que el bucle alcance su iteración final.
- En un bucle `while`, la cláusula `else` se ejecuta después de que la condición sea falsa.
- `pass`: Actúa como un marcador de posición donde se necesita una declaración, pero no se necesita hacer nada.

Algunas consideraciones adicionales:

- Evita modificar la lista sobre la que estás iterando: Esto puede causar resultados inesperados o errores. 
Si necesitas modificar la lista, considera crear una copia.
- Utiliza list comprehensions cuando sea posible: Son más rápidas y más fáciles de leer para tareas simples.
"""

# Bucle while básico
# Este bucle sigue ejecutándose mientras la condición sea verdadera

contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1  # Incrementa el contador en cada iteración

# Importante: Asegúrate de que la condición eventualmente se vuelva falsa para evitar bucles infinitos.

# Bucle for básico
# Este bucle itera sobre una secuencia (en este caso, una lista)

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta comer {fruta}")

# La variable 'fruta' toma el valor de cada elemento de la lista en cada iteración.

# Usando range() con for
# `range()` genera una secuencia de números enteros, útil para iterar un número específico de veces

for i in range(5):
    print(f"Iteración {i}")

# `range()` puede tomar hasta tres argumentos: inicio, fin y paso
for i in range(1, 10, 2):
    print(f"Número impar: {i}")


# Iterar sobre los índices de una secuencia, combinando range() y len()
# Se recomienda usar `enumerate()`
names = ["John", "Corey", "Adam", "Steve"]

for i in range(len(names)):
    print("Índice:", i, ", Nombre:", names[i])

# Bucle for con enumerate()
# `enumerate()` permite acceder tanto al índice como al valor de los elementos en una secuencia

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Esto es especialmente útil cuando necesitas el índice de los elementos en la iteración.

# Usando break para salir de un bucle
# `break` se usa para terminar un bucle prematuramente

for fruta in frutas:
    if fruta == "banana":
        break  # El bucle termina si se encuentra con "banana"
    print(f"Me gusta comer {fruta}")

# Usando continue para saltar una iteración
# `continue` salta el resto del código en la iteración actual y pasa a la siguiente

for fruta in frutas:
    if fruta == "banana":
        continue  # Salta la iteración actual si la fruta es "banana"
    print(f"Me gusta comer {fruta}")

# Bucle else
# El bloque `else` en un bucle se ejecuta solo si el bucle no se interrumpió con `break`

for fruta in frutas:
    print(f"Me gusta comer {fruta}")
else:
    print(
        "He terminado de comer todas las frutas."
    )  # El `else` aquí se ejecuta porque no hubo un `break`.

# Bucle while con else
contador = 0
while contador < 3:
    print(f"El contador es: {contador}")
    contador += 1
else:
    print("El bucle while ha terminado.")


# Uso de bucles anidados
# Puedes anidar bucles (un bucle dentro de otro)

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Comprensión de listas (List Comprehensions)
# Una forma concisa y eficiente de crear listas

# Ejemplo: Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)
