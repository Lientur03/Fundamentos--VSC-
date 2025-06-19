from data.leer_data import listado_data, obtener_indice_data
from data.crear_data import guardar_data
from data.docentes import docentes

# READ DATA
def obtener_listado_docentes():    
    print()
    print('Listado de Docentes')
    print('===================')
    lista = listado_data('docentes.py')
    if len(lista) > 0:
        contador = 0
        for data in sorted(lista):
            contador += 1
            print(f'[{contador} {data}]')
    else:
        print('No se han encontrado datos.')

# CREATE DATA
def guardar_nuevo_docente():
    obtener_listado_docentes()
    nuevo_docente = input('Ingrese nuevo docente: ')
    docentes.append(nuevo_docente.title())
    mensaje = guardar_data('docentes', docentes,'docentes.py')
    print(f'{mensaje} de docente {nuevo_docente}')

# UPDATE DATA
def actualizar_docente():
    obtener_listado_docentes()
    búsqueda = input("Ingrese docente a buscar: ")
    indice_docente = obtener_indice_data('docentes.py', búsqueda)

    if indice_docente is not None:
        docente_modificado = input("Ingrese un nuevo nombre de docente: ")
        docentes[indice_docente] = docente_modificado.title()
        mensaje = guardar_data('docentes', docentes, 'docentes.py')
        print(f'{mensaje} de docente {docente_modificado}')
    else:
        print("Docente NO Encontrado")

# DELETE DATA
def eliminar_docente():
    obtener_listado_docentes()
    búsqueda = input("Ingrese docente a buscar: ")
    indice_docente = obtener_indice_data('docentes.py', búsqueda)

    if indice_docente is not None:
        docente = docentes[indice_docente]
        docentes.pop(indice_docente)
        mensaje = guardar_data('docentes', docentes, 'docentes.py')
        print(f'{mensaje}, docente {docente} eliminado.')
    else:
        print("Docente NO Encontrado")