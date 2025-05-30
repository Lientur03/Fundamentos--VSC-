import os 

def guardar_data(nombre_lista, lista_data, nombre_archivo):
    archivo_datos = 'asignaturas.py'
    ubicacion_archivo = os.path.join('Gestion_Notas/data', archivo_datos)
    ubicacion_archivo = os.path.join.abspath(ubicacion_archivo)
    ubicacion_archivo = os.path.realpath(ubicacion_archivo)
    archivo = open(f"{ubicacion_archivo}", "w+")
    archivo.write(f'{nombre_lista} = {lista_data}')
    archivo.close()