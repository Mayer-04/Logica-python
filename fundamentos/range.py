"""
* Range - Rango

- Función `range` son objetos que generan una secuencia inmutable de números enteros.
- Se suelen utilizar para ser ejecutados en un bucle `for`.
- Los parámtros usados en range deben ser números enteros.
- `range` toma tres argumentos: start, stop y step (salto) entre elementos
- Si step se omite se establece en 1.
- Si se omite el parámetro start, se establece en 0.
- los rangos soportan índices negativos, esto toma los valores desde el final hasta el principio.

IMPORTANTE: La ventaja de usar un objeto de tipo `range` en vez de uno de tipo list o tuple,
es que con range siempre se usa una cantidad fija (y pequeña) de memoria,
"""

rango = range(10)

print(rango)  # range(0, 10)

print(11 in range)
