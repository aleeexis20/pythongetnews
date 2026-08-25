import mysql.connector

# Ingresamos credenciales de la base de datos MySQL
def conectar_bd():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="alexis123", 
        database="news_db"
    )
    return conexion

def guardar_datos(diccionario_fechas, diccionario_lugares):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Recorremos el diccionario llave por llave
    for dia in diccionario_fechas:
        numero = diccionario_fechas[dia]  # Extraemos el valor guardado
        sql_fecha = "INSERT INTO fechas (dia_semana, digito) VALUES (%s, %s)"
        cursor.execute(sql_fecha, (dia, numero))

    for tipo in diccionario_lugares:
        nombre = diccionario_lugares[tipo]  # Extraemos el valor guardado
        sql_lugar = "INSERT INTO vialidades (tipo_vialidad, nombre) VALUES (%s, %s)"
        cursor.execute(sql_lugar, (tipo, nombre))

    # Guardamos los cambios y cerramos la conexion
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Datos guardados exitosamente en MySQL.")

def consultar_vialidades():
    conexion = conectar_bd()
    # Solicitamos la tabla completa
    cursor = conexion.cursor() 
    
    cursor.execute("SELECT * FROM vialidades")
    resultados = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    return resultados