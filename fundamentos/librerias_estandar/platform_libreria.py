import platform

"""
CPython es la implementación de Python más utilizada, la más rápida y la más madura.
Tanto el intérprete como los módulos están escritos en el lenguaje de programación C.

- CPython está instalado por defecto en la mayor parte de las distribuciones Linux y en las últimas versiones 
de Mac OS como de Windows.
"""

# Verificar la implementación de Python que estamos usando.
print(platform.python_implementation())  # CPython
