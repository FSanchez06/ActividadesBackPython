import mysql.connector

# Datos de conexión
config = {
    'user': 'root',  
    'password': '',  
    'host': 'localhost',
    'database': 'unidad_productiva'
}

# Conectar a MySQL
db = mysql.connector.connect(**config)
cursor = db.cursor()

def ingresar_enfermedad():
    """Función para ingresar una enfermedad en la base de datos."""
    nombre = input("Ingrese el nombre de la enfermedad: ")
    caracteristicas = input("Ingrese las características (separadas por comas): ")
    tratamiento = input("Ingrese el tratamiento: ")
    
    sql = "INSERT INTO enfermedades (nombre, caracteristicas, tratamiento) VALUES (%s, %s, %s)"
    values = (nombre, caracteristicas, tratamiento)
    cursor.execute(sql, values)
    db.commit()
    print("Enfermedad ingresada correctamente.")

def pronosticar_enfermedad():
    """Función para pronosticar enfermedades según características ingresadas."""
    caracteristicas = input("Ingrese las características (separadas por comas): ")
    caracteristicas_lista = caracteristicas.split(',')
    
    sql = "SELECT nombre FROM enfermedades WHERE caracteristicas LIKE %s"
    
    enfermedades = []
    for caracteristica in caracteristicas_lista:
        cursor.execute(sql, ('%' + caracteristica.strip() + '%',))
        resultado = cursor.fetchall()
        enfermedades.extend([enfermedad[0] for enfermedad in resultado])
    
    if enfermedades:
        print("Posibles enfermedades:")
        for enfermedad in set(enfermedades):
            print("- " + enfermedad)
    else:
        print("No se encontraron enfermedades con esas características.")

def consultar_tratamiento():
    """Función para consultar el tratamiento de una enfermedad específica."""
    nombre_enfermedad = input("Ingrese el nombre de la enfermedad: ")
    
    sql = "SELECT tratamiento FROM enfermedades WHERE nombre = %s"
    cursor.execute(sql, (nombre_enfermedad,))
    resultado = cursor.fetchone()
    
    if resultado:
        print("Tratamiento para la enfermedad:", resultado[0])
    else:
        print("No se encontró la enfermedad.")

def main():
    """Función principal que presenta el menú y gestiona las opciones."""
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar BD de Conocimiento")
        print("2. Pronosticar enfermedad")
        print("3. Consultar tratamiento")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            ingresar_enfermedad()
        elif opcion == '2':
            pronosticar_enfermedad()
        elif opcion == '3':
            consultar_tratamiento()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

# Cerrar la conexión al final
cursor.close()
db.close()
