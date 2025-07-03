import mysql.connector
from mysql.connector import errorcode
from auxiliares.data_conexion import servidor, puerto, usuario, base_datos, contraseña
try:
    conexion = mysql.connector.connect(
        host = servidor,
        port = puerto,
        user = usuario,
        database = base_datos,
        password = contraseña
    )

    if conexion and conexion.is_connected():
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM asignaturas')
        resultado = cursor.fetchall()
        print(resultado)
    else:
        print('No se ha podido establecer conexión con la base de datos')
except:
    print('No se ha podido establecer conexión con el servidor')