from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Cambia la URL si es necesario
db = client['sensores_db']  # Nombre de la base de datos
sensores_collection = db['sensores']  # Nombre de la colección

def ver_sensores():
    """Muestra todos los sensores en la base de datos."""
    sensores = list(sensores_collection.find({}))
    if not sensores:
        print("No hay sensores registrados en la base de datos.")
    else:
        print("\nSensores:")
        for sensor in sensores:
            print(f"Nombre: {sensor['nombre']}, Mínimo: {sensor['minimo']}, Máximo: {sensor['maximo']}")
    print()

def agregar_sensor():
    """Solicita los parámetros de un nuevo sensor y lo agrega a la base de datos."""
    nombre = input("Ingrese el nombre del sensor: ")
    minimo = int(input("Ingrese el valor mínimo: "))
    maximo = int(input("Ingrese el valor máximo: "))
    
    # Verificar si el sensor ya existe
    if sensores_collection.find_one({"nombre": nombre}):
        print("El sensor ya existe en la base de datos.")
    else:
        sensores_collection.insert_one({"nombre": nombre, "minimo": minimo, "maximo": maximo})
        print("Sensor agregado exitosamente.")

def eliminar_sensor():
    """Solicita el nombre del sensor y lo elimina de la base de datos."""
    nombre = input("Ingrese el nombre del sensor a eliminar: ")
    
    resultado = sensores_collection.delete_one({"nombre": nombre})
    
    if resultado.deleted_count > 0:
        print(f"Sensor '{nombre}' eliminado exitosamente.")
    else:
        print(f"No se encontró un sensor con el nombre '{nombre}'.")

def modificar_parametros():
    """Solicita el nombre del sensor y sus nuevos parámetros, y actualiza o agrega el sensor."""
    nombre = input("Ingrese el nombre del sensor: ")
    
    # Buscar el sensor en la base de datos
    sensor = sensores_collection.find_one({"nombre": nombre})
    
    if sensor:
        nuevo_minimo = int(input("Ingrese el nuevo valor mínimo: "))
        nuevo_maximo = int(input("Ingrese el nuevo valor máximo: "))
        
        # Actualizar los parámetros del sensor
        sensores_collection.update_one({"nombre": nombre}, {"$set": {"minimo": nuevo_minimo, "maximo": nuevo_maximo}})
        print(f"Parámetros del sensor '{nombre}' actualizados exitosamente.")
    else:
        agregar_sensor()  # Si no existe, agregarlo como nuevo

def menu():
    """Muestra el menú principal y maneja las opciones del usuario."""
    while True:
        print("Menú de Gestión de Sensores:")
        print("1. Ver Sensores")
        print("2. Agregar Sensor")
        print("3. Eliminar Sensor")
        print("4. Modificar Parámetros")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            ver_sensores()
        elif opcion == '2':
            agregar_sensor()
        elif opcion == '3':
            eliminar_sensor()
        elif opcion == '4':
            modificar_parametros()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
