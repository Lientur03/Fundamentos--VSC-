import os
asignaturas = ''

def obtener_data_asignaturas():
    archivo = "Gestion_Notas/data/asignaturas.txt"
    with open(archivo, 'r') as file:
        print(file.readlines())

# print()
# print(len(asignaturas))
# print(len('hola'))
# print(len(asignaturas) * len('hola'))
# print()
# print(asignaturas)

# if 'ol' in 'Hola':
#     print(True)
# else:
#     print(False)

def obtener_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    print('======================')
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f'[{contador}] {asignatura}')

def obtener_asignatura_individual():
    asignatura_encontrada = 'Asignatura NO encontrada'
    búsqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if búsqueda.lower() in asignatura.lower():
            asignatura_encontrada = asignatura
    return asignatura_encontrada

def guardar_nueva_asignatura():
    obtener_listado_asignaturas()
    nueva_asignatura = input('Ingrese nueva asignatura: ')
    # asignaturas.append(nueva_asignatura.title())
    obtener_listado_asignaturas()

obtener_data_asignaturas()