# Programa tradicional para registrar y mostrar información de una mascota

# Función para registrar los datos de la mascota
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad

# Función para mostrar los datos de la mascota
def mostrar_mascota(nombre, especie, edad):
    print("\n--- Información de la Mascota ---")
    print("Nombre:", nombre)
    print("Especie:", especie)
    print("Edad:", edad, "años")

# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)