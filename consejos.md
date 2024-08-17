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

1. En Python, no es necesario colocar un punto y coma (;) al final de cada sentencia.
2. Usa minúsculas y separa las palabras con guiones bajos para nombrar variables. snake_case
3. Puedes multiplicar una cadena por un número para repetirla varias veces:

```py
    print("Mayer" * 4) # MayerMayerMayerMayer
```

4. **Evita Comparar Diferentes Tipos:** Comparar valores de diferentes tipos puede llevar a errores o resultados inesperados.
5. **Uso de Truthy y Falsy:** Al igual que en JavaScript, Python evalúa valores como `True` o `False` en condiciones. Ejemplos de valores `Falsy` incluyen `None`, `0`, `""`, `[]`, `{}`, mientras que cualquier otro valor se considera `Truthy`.
6. Python al igual que JavaScript el intérprete convierte implícitamente el valor de esa variable a un booleano para ser evaluada por un `if`
7. **Evita Modificar Listas Durante la Iteración:** Modificar una lista mientras la iteras puede causar comportamientos inesperados. Considera usar una copia de la lista o una comprensión de listas para evitar problemas.

```py
    for item in my_list[:]:
        if some_condition(item):
            my_list.remove(item)
```

8. **Evita Efectos Colaterales en Funciones:** Las funciones deben evitar modificar variables globales u otras partes del programa para mantener la claridad y facilitar las pruebas.
9. **Secuencias:** Es un tipo de dato que puede almacenar una colección de elementos o contener varios elementos. Algunas secuencias en Python son las listas, diccionarios, tuplas, cadenas de caracteres, conjuntos y la función `range()`.

## Diccionarios

1. Las claves de un diccionario deben ser inmutables, como enteros, cadenas o tuplas. No uses listas o diccionarios como claves.
2. **Uso de get para Acceder a Valores:** Usa el método `get()` para acceder a los valores de un diccionario de forma segura, evitando errores si la clave no existe:

```py
diccionario = {"cuidad": "medellin"}
print(diccionario.get("clave2", "Valor por defecto"))  # Salida: Valor por defectos
```

3. **Comprensión de Diccionarios:** Usa la comprensión de diccionarios para crear diccionarios de manera concisa:

```py
cuadrados = {x: x**2 for x in range(10)}
```
