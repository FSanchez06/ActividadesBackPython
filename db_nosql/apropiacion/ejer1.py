import random
import time
from colorama import Fore, Style, init
from pymongo import MongoClient

# Inicializar colorama
init(autoreset=True)

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Cambia la URL si es necesario
db = client['sensores_db']  # Nombre de la base de datos
sensores_collection = db['sensores']  # Nombre de la colección

# Contador de mediciones fuera de rango
mediciones_fuera_de_rango = 0

def obtener_valor(sensor):
    """Genera un valor aleatorio para el sensor dentro de un rango amplio."""
    return random.randint(0, 50)  # Genera un valor entre 0 y 50

def monitorear_sensores():
    global mediciones_fuera_de_rango

    while mediciones_fuera_de_rango < 3:
        # Obtener todos los sensores desde la base de datos
        sensores = list(sensores_collection.find({}))  # Convertir a lista

        if not sensores:
            print("No se encontraron sensores en la base de datos.")
            break
        
        # Seleccionar un sensor aleatorio
        sensor = random.choice(sensores)
        valor = obtener_valor(sensor)

        # Comparar el valor con los límites
        if sensor["minimo"] <= valor <= sensor["maximo"]:
            print(f"{Fore.GREEN}{sensor['nombre']} - Valor: {valor} (Dentro del rango){Style.RESET_ALL}")
            mediciones_fuera_de_rango = 0  # Reiniciar contador si está dentro del rango
        else:
            print(f"{Fore.RED}{sensor['nombre']} - Valor: {valor} (Fuera del rango){Style.RESET_ALL}")
            mediciones_fuera_de_rango += 1

        time.sleep(1)  # Esperar un segundo antes de la siguiente medición

if __name__ == "__main__":
    print("Iniciando monitoreo de sensores...")
    monitorear_sensores()
    print("El monitoreo ha terminado debido a 3 mediciones fuera del rango.")
