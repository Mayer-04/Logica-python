"""
* POO (Programación Orientada a Objetos)

- La programación orientada a objetos es una teoria que describe el comportamiento de los objetos
- Las clases son los moldes o plantillas que definen los atributos y métodos de un objeto
- Las instancias son los objetos creados a partir de una clase
- Los objetos son instancias de una clase
"""


# Definiendo una clase en Python
class Persona:
    """
    Clase que representa a una persona.
    """

    # Contructor: Método que se ejecuta cuando se crea una instancia de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        """
        Imprime un saludo de presentación.
        """
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años")


# Creando una instancia de la clase Persona
persona = Persona("Mayer", 24)
print(
    "persona:", persona
)  # Imprime la referencia de la instancia: <__main__.Persona object at 0x0000016C44596510>

# Llamando al método `presentar()` de la instancia
persona.presentar()
