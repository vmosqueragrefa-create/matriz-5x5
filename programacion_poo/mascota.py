class Mascota:
    # Constructor
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Método para mostrar información
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad, "años")

    # Método para emitir un sonido según la especie
    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print("Guau Guau")
        elif self.especie.lower() == "gato":
            print("Miau Miau")
        else:
            print("Sonido desconocido")