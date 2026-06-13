# Importar la clase Mascota
from mascota import Mascota

# Crear objetos de la clase Mascota
mascota1 = Mascota("Luna", "Perro", 3)
mascota2 = Mascota("Michi", "Gato", 2)

# Mostrar información y sonido de la primera mascota
print("Mascota 1")
mascota1.mostrar_informacion()
mascota1.hacer_sonido()

print("\nMascota 2")
mascota2.mostrar_informacion()
mascota2.hacer_sonido()