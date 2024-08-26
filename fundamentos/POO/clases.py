"""
* POO (Programación Orientada a Objetos)

- La programación orientada a objetos es una teoria que describe el comportamiento de los objetos.
- Las clases son los moldes o plantillas que definen los atributos y métodos de un objeto.
- Las instancias son los objetos creados a partir de una clase.
- Los objetos son instancias de una clase.
- Las nombres de las clases por convención se escriben en `UpperCamelCase`.
- El parámetro `self` se refiere a la instancia de la clase, es decir, el objeto que se esta creando. (el objeto mismo)
"""


# Definiendo una clase en Python
class Persona:

    # Contructor: Método que se ejecuta cuando se crea una instancia de la clase
    # _init_ Define los valores iniciales de nuestra clase u objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        """
        Imprime un saludo de presentación.

        Ejemplo:
            persona = Persona("Mayer", 24)
            persona.presentar()  # Imprime "Hola, mi nombre es Mayer y tengo 24 años"
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")


# Creando una instancia de la clase Persona
mayer = Persona("Mayer", 24)
print(
    "persona:", mayer
)  # Imprime la referencia de la instancia: <__main__.Persona object at 0x0000016C44596510>

# Llamando al método `presentar()` de la instancia
mayer.presentar()
