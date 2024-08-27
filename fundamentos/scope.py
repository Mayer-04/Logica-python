"""
* Scope - (ámbito o alcance)

El scope en Python se refiere a `dónde` puedes usar una variable o una función en tu código.
- El scope define en qué partes de tu código una variable está disponible para ser usada. 
Si tratas de usar una variable fuera de su scope, Python no la va a reconocer, y te dará un error. 

El manejo de los scopes en Python sigue la regla conocida como LEGB (Local, Enclosing, Global, Built-in).

- Primero se busca en el scope Local.
- Si no se encuentra, se busca en el scope Enclosing.
- Si no se encuentra allí, se busca en el scope Global.
- Finalmente, si no se encuentra en ninguno de los anteriores, se busca en el scope Built-in.

- Global: Este scope se refiere a las variables definidas en el nivel más alto del script o módulo, 
fuera de cualquier función. Las variables globales son accesibles desde cualquier parte del módulo.

- Local: Es el scope más interno y se refiere a las variables definidas dentro de una función. 
Estas variables solo son accesibles dentro de esa función.

- Enclosing: Se refiere al scope de una función que encierra a otra función.
Si una función interna intenta acceder a una variable que no está en su propio scope local, 
Python buscará esa variable en el scope de la función externa.

- Built-in: Se refiere a las funciones y excepciones incorporadas (print, len, Exception, etc.).


- las estructuras de control no crean un nuevo scope en Python.
las variables definidas dentro de ellas simplemente `heredan` el scope 
del bloque de código en el que la estructura está contenida.

* Las estructuras de control como if, while, y for no crean un nuevo scope en Python. 
Las variables definidas dentro de estas estructuras heredan el scope del bloque en el que están contenidas.

- Si defines una variable dentro de un if, while, o for en el nivel global del script, 
esa variable tendrá un scope global.

- Si defines una variable dentro de un if, while, o for dentro de una función, 
esa variable tendrá un scope local a esa función.
"""
