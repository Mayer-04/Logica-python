"""
* Módulos en Python

Un módulo es un archivo Python que contiene código y definiciones de funciones, clases, variables, etc.
- Ayuda a reutilizar código de otros archivos.
- Este código puede ser importado en otro archivo Python para utilizar sus definiciones.

- import: Se usa para importar un módulo completo en tu programa.
- from: Se usa junto con import para importar algo específico de un módulo.
- as: Se usa para darle un nombre alternativo o alias a un módulo.
"""

# Importar el módulo `random`
import random

print(random.randint(1, 10))

# Importar el módulo `math` y dandole un alias `m` al mismo.
import math as m

print(m.pi)

# Importar algo específico de un módulo, en lugar de importar el módulo completo.
# "del módulo listas importa numbers"
from listas import numbers

print(numbers)


import listas

if __name__ == "__main__":
    # Este código solo se ejecuta si el archivo se ejecuta directamente
    print(listas.numbers)
