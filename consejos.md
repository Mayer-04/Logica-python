# Consejos en Python

## Modo Interactivo

Salir del modo interactivo con el comando:

```shell
exit()
```

### Windows

```bash
python
```

### MacOS o Linux

```bash
python3
```

1. En Python no hay que poner punto y coma al final de la setencia del código
2. Un comentario en python se realiza con `#`, un comentario multilínea es con """ """
3. Escribir las variables en minusculas y snakeCase
4. En Python se puede multiplicar una cadena

```python
    print("Mayer" * 4) # MayerMayerMayerMayer
```

5. En Python no se pueden hacer comparación de diferentes tipos
6. En Python también existen los conceptos de "truthy" y "falsy".
7. Python al igual que JavaScript el intérprete convierte implícitamente el valor de esa variable a un booleano para ser evaluada por un `if`
8. Evita la Modificación de Listas Mientras las Iteras: Modificar una lista mientras iteras sobre ella puede llevar a comportamientos inesperados.

- Las funciones deben evitar modificar variables globales u otras partes del programa para que sean más fáciles de entender y probar.

## Diccionarios

9. Las claves de un diccionario deben ser inmutables, es decir, pueden ser de tipos como enteros, cadenas o tuplas, pero no listas o diccionarios.
10. Es una buena práctica usar el método get al acceder a los valores de un diccionario para evitar errores si la clave no existe.
