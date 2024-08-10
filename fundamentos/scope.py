"""
* Scope - (ámbito o alcance)

El manejo de los scopes en Python sigue la regla conocida como LEGB (Local, Enclosing, Global, Built-in).

- Primero se busca en el scope Local.
- Si no se encuentra, se busca en el scope Enclosing.
- Si no se encuentra allí, se busca en el scope Global.
- Finalmente, si no se encuentra en ninguno de los anteriores, se busca en el scope Built-in.

- global: Se refiere al ámbito local de una función o método.
- local: Se refiere al ámbito global del módulo o script.
- enclosing: Se refiere al ámbito de funciones externas en las que está contenida una función interna. 
Las variables en el scope enclosing son accesibles en funciones internas
- built-in: Se refiere a los métodos incorporados de Python.


- las estructuras de control no crean un nuevo scope en Python.
las variables definidas dentro de ellas simplemente `heredan` el scope 
del bloque de código en el que la estructura está contenida.
"""

"""
* Las estructuras de control como `if`, `while` y `for` no crean un nuevo scope.
Las variables definidas dentro de estas estructuras pertenecen al mismo scope en el
que la estructura está contenida.

- Si defines una variable dentro de un `if`, `while` o `for` que está en el nivel global del script, 
la variable tendrá un scope global.

- Si defines una variable dentro de un `if`, `while` o `for` que está dentro de una función, 
la variable tendrá un scope local a esa función.
"""
