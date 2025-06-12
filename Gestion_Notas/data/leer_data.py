from data.asignaturas import asignaturas
from data.docentes import docentes

def listado_data(nombre_archivo):
    lista = []
    if nombre_archivo == 'asignaturas.py':
        lista = asignaturas
    elif nombre_archivo == 'docentes.py':
        lista = docentes
    return lista

def obtener_id_data(nombre_archivo, búsqueda):
    lista = []
    if nombre_archivo == 'asignaturas.py':
        lista = asignaturas
    elif nombre_archivo == 'docentes.py':
        lista = docentes
    
    indice = None
    for i in range(len(lista)):
        if búsqueda.lower() in lista[i].lower():
            indice = i
    return indice  