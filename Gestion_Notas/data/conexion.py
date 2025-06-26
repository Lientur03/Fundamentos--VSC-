import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    port=3308,
    user='root',
    database='gestion_notas'
)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM docentes')
resultado = cursor.fetchall()
print(resultado)