# Consejos en Python

## Iniciar el Modo Interactivo

**En Windows:**

```bash
python
```

**En MacOS o Linux:**

```bash
python3
```

Para salir del modo interactivo de Python, utiliza el siguiente comando:

```shell
exit()
```

## Mutabilidad e Inmutabilidad

Los objetos en Python se pueden clasificar en dos categorías basadas en su capacidad para cambiar:

1. **Mutables:** Estos objetos pueden cambiar su valor después de haber sido creados. Cuando un objeto mutable se pasa como argumento a una función, se pasa por referencia, lo que significa que las modificaciones realizadas en la función afectarán al objeto original.

Algunos objetos mutables son:

- list (listas)
- dict (diccionario)
- set (conjuntos)
- bytearray

2. **Inmutables:** Estos objetos no pueden cambiar su valor una vez creados. Si se intenta modificar un objeto inmutable, se creará un nuevo objeto en su lugar. Cuando un objeto inmutable se pasa como argumento a una función, se pasa por valor, es decir, la función trabaja con una copia del valor original y no puede modificar el objeto original.

Algunos objetos inmutables son:

- int (entero)
- float (flotante)
- bool (booleano)
- str (cadena)
- tuple
- frozenset

## Lenguaje Interpretado o de Script

El código Python que escribimos no se convierte directamente en instrucciones que la computadora pueda entender **(lenguaje máquina)**. En lugar de eso, un programa especial llamado `intérprete` lee y ejecuta el código línea por línea.

En el caso de Python, cuando ejecutas un programa, el código se traduce primero a un formato intermedio llamado `bytecode`, que es una especie de lenguaje máquina simplificado.

- El intérprete de Python ejecuta este bytecode. Es decir, el intérprete lee el bytecode y lo traduce a instrucciones que la computadora puede entender y ejecutar.
- Los archivos _.pyc_ o _.pyo_ se generan automáticamente y se guardan en un directorio especial llamado **pycache**, que se encuentra en la misma carpeta donde está tu archivo _.py_ original.

## Características y Consejos

1. En Python, no es necesario terminar cada sentencia con un punto y coma (;).
2. **Indentación Obligatoria:** En lugar de usar llaves `{}` para agrupar bloques de código (como en otros lenguajes), Python utiliza la `indentación`. Por convención, se emplean 4 espacios por nivel de indentación. Una indentación incorrecta resultará en un error de sintaxis.
3. **Nombres de Variables Descriptivos:** Es recomendable utilizar nombres de variables en minúsculas, separando las palabras con guiones bajos `(snake_case).`
4. Puedes multiplicar una cadena por un número para repetirla varias veces con el operador aritmetico `*`:

```py
print("Mayer" * 4) # MayerMayerMayerMayer
```

5. **Evita Comparar Tipos Diferentes:** Comparar valores de diferentes tipos puede generar errores o comportamientos inesperados. Asegúrate de que los valores sean del mismo tipo antes de compararlos.
6. **Uso de Truthy y Falsy:** Al igual que en JavaScript, Python evalúa valores como `True` o `False` en condiciones. Ejemplos de valores `Falsy` incluyen `None`, `0`, `""`, `[]`, `{}`, mientras que cualquier otro valor se considera `Truthy`.
7. **Conversión Implícita en Condicionales:** El intérprete de Python convierte `implícitamente` una variable a un booleano cuando se evalúa en una condición if. Esto sucede también en lenguajes como JavaScript.
8. **Modificación de Listas Durante la Iteración:** Modificar una lista mientras la recorres puede causar comportamientos inesperados. Para evitarlo, trabaja con una copia de la lista:

```py
for item in my_list[:]:
    if some_condition(item):
        my_list.remove(item)
```

9. **Evita Efectos Colaterales en Funciones:** Las funciones deben evitar modificar variables globales u otras partes del programa para mantener la claridad y facilitar las pruebas.
10. **Secuencias:** Es un tipo de dato que puede almacenar una colección de elementos o contener varios elementos. Algunas secuencias en Python son las listas, tuplas, cadenas de caracteres y rangos (la función `range()`).

## Buenas practicas

1. **Uso de Funciones Incorporadas (Built-ins):** Python ofrece muchas funciones incorporadas que pueden simplificar tu código, como **len()**, **sum()**, **max()**, **min()**, entre otras. Siempre que sea posible, utiliza estas funciones en lugar de reinventar la rueda.
2. **Comprensión de Listas y Generadores:** Utiliza comprensión de listas y generadores para crear listas, diccionarios, o conjuntos de manera concisa y eficiente:

```py
cuadrados = [x**2 for x in range(10)]
```

```py
cuadrados_tup = (x**2 for x in range(10))
```

3. **Utiliza Entornos Virtuales:** Para evitar conflictos de dependencias entre proyectos, utiliza entornos virtuales. Esto te permite gestionar paquetes y versiones de manera aislada para cada proyecto.

## Diccionarios

1. Las claves de un diccionario deben ser inmutables, como enteros, cadenas o tuplas. No uses listas o diccionarios como claves.
2. **Acceso Seguro a Valores con get():** Utiliza el método get() para acceder a los valores de un diccionario sin riesgo de lanzar un error si la clave no existe:

```py
diccionario = {"cuidad": "medellin"}
print(diccionario.get("clave2", "Valor por defecto"))  # Salida: Valor por defecto
```

3. **Comprensión de Diccionarios:** Usa la comprensión de diccionarios para crear diccionarios de manera concisa y eficiente:

```py
cuadrados_dict = {x: x**2 for x in range(10)}
```

4. **Evita Modificar un Diccionario Durante la Iteración:** Similar a las listas, modificar un diccionario mientras lo iteras puede causar errores. Usa métodos como `copy()` si necesitas modificarlo dentro de un bucle.

## Características adicionales

1. **Desempaquetado:** Utiliza `*` y `**` para desempaquetar listas y diccionarios al pasar argumentos a funciones o al realizar asignaciones:

```py
my_list = [1, 2, 3]
print(*my_list)  # Salida: 1 2 3
```

```py
my_dict = {"a": 1, "b": 2, "c": 3}
new_dict = {**my_dict}
print(new_dict) # salida: {'a': 1, 'b': 2, 'c': 3}
```

```py
def generar_diccionario(a, b, c):
    print(a, b, c)

diccionario = {'a': 1, 'b': 2, 'c': 3}
generar_diccionario(**diccionario)  # Salida: 1 2 3
```

## Objetos

Recordemos que en **objeto** en Python es una _instancia_ de una clase. Cada objeto en Python tiene tres características fundamentales: `identidad`, `tipo` y `valor`.

- **Identidad:** La identidad de un objeto es un identificador único (número entero) que lo distingue de otros objetos. Esta identidad es inmutable durante la vida del objeto y se puede verificar usando el operador `is`, que determina si dos referencias apuntan al mismo objeto en memoria.
- **Tipo:** El tipo de un objeto define la naturaleza de los datos que contiene y las operaciones que se pueden realizar sobre él. Una vez que se crea un objeto, su tipo no cambia. El tipo de un objeto se puede consultar con la función `type()`.
- **Valor:** El valor de un objeto es el contenido que almacena. Dependiendo de si el objeto es `mutable` o `inmutable`, su valor puede o no cambiar durante la ejecución del programa.

Ejemplo de como se veria esto:

```py
# Creando un objeto (en este caso una lista)
mi_lista = [1, 2, 3]

# Identidad: el identificador único del objeto
# Se representa como un número entero
identidad = id(mi_lista)
print(f"Identidad: {identidad}") # Identidad: 2706717792512

# Tipo: el tipo del objeto
tipo = type(mi_lista)
print(f"Tipo: {tipo}") # Tipo: <class 'list'>

# Valor: el contenido del objeto
valor = mi_lista
print(f"Valor: {valor}") # Valor: [1, 2, 3]

# Comparación de identidad con otro objeto similar
# Las listas son mutables por lo que crea un nuevo objeto en memoria,
# incluso si el contenido de la lista es idéntico al de otra lista.
otra_lista = [1, 2, 3]
print(f"¿mi_lista es la misma que otra_lista? {mi_lista is otra_lista}") # False

# Modificación del objeto mutable
mi_lista.append(4)
print(f"Valor modificado: {mi_lista}") # Valor modificado: [1, 2, 3, 4]
```
