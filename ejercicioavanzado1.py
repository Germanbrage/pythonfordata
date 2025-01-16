import pandas
import psycopg2

# Configuración de conexión
conexion = None
try:
    # Conectar a la base de datos
    conexion = psycopg2.connect(
        host="localhost",       # Dirección del servidor (localhost si es local)
        database="Northwind",   # Nombre de tu base de datos
        user="postgres",      # Tu nombre de usuario en PostgreSQL
        password="admin", # Tu contraseña
        port=5432               # Puerto por defecto de PostgreSQL
    )

    print("Conexión exitosa a la base de datos")

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta de prueba
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tablas = cursor.fetchall()
    print("Tablas en la base de datos:")
    for tabla in tablas:
        print(tabla[0])

    # Cerrar el cursor
    cursor.close()

except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

finally:
    if conexion is not None:
        conexion.close()
        print("Conexión cerrada")



