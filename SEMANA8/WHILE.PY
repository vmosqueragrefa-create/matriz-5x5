#inventario de bodega
producto = [
    {"id":1, "nombre":"perro","raza": "perro","edad": "1 año"},
    {"id":2, "nombre":"otro perro","raza": "perro","edad":"3 años"},
    {"id":3, "nombre": "gato","raza":"gato", "edad":"7 meses"},
    {"id":4, "nombre": "otro gato", "raza":"gato","edad":"7 años"},
   ]
while True:
    print("----------bienvenido a su veterinario favorito-------")
    print("----------Menu Principal---------")
    print("1. Listado de Animales")
    print("2. Ingrese el nuevo animal")
    print("3. Actualizar informacion del animal")
    print("4. Borrar animal")
    print("5. Salir")
    opcion = int(input("ingrese la opcion que nesecita (1,2,3,4,5,)")) 
    if opcion == 1:
        for animal in lista_animales:
            print(f"nombre:{animal["nombre"]}")
            print(f"raza:{animal["raza"]}")
            print(f"edad: {animal["edad"]}")
            print("--"*30)

