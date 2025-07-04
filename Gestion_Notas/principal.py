from negocio.negocio_asignaturas import obtener_listado_asignaturas,guardar_nueva_asignatura,actualizar_asignatura,eliminar_asignatura
from negocio.negocio_docentes import obtener_listado_docentes, guardar_nuevo_docente,actualizar_docente,eliminar_docente
from auxiliares.version import version_actual
from data.conexion import conectar_db
from prettytable import PrettyTable

def cargar_menu(tipo_menu):
    print()
    print(f"Sistema Gestión Notas v.{version_actual}")
    print("==============================")
    consulta = f'''
        SELECT numero_opcion,opcion_menu FROM opciones_menu
        WHERE tipo_menu = {tipo_menu}
    '''
    resultado = conectar_db(consulta)
    tabla_menu = PrettyTable()
    tabla_menu.field_names = ['N°', 'Opción']
    contador = 0
    if resultado != None:
        for asignatura in resultado:
            contador += 1
            tabla_menu.add_row(asignatura)
    print(tabla_menu)
    opcion_menu = input(f"Seleccione su Opción [0-{contador}]: ")
    return opcion_menu

def ejecucion_principal():
    while True:
        opcion_menu = cargar_menu()

        if opcion_menu == "1":
            sub_menu_asignaturas()
            opcion_submenu_asignaturas = input("Seleccione su Opción [0-4]: ")
            
            if opcion_submenu_asignaturas == "1":
                obtener_listado_asignaturas()
            elif opcion_submenu_asignaturas == "2":
                guardar_nueva_asignatura()
            elif opcion_submenu_asignaturas == "3":
                actualizar_asignatura()
            elif opcion_submenu_asignaturas == "4":
                eliminar_asignatura()
            elif opcion_submenu_asignaturas == "0":
                return
            else:
                print("Opción Inválida, vuelva a ingresar...")
                return
            
        elif opcion_menu == "2":
            sub_menu_docentes()
            opcion_submenu_docentes = input("Seleccione su Opción [0-4]: ")

            if opcion_submenu_docentes == "1":
                obtener_listado_docentes()
            elif opcion_submenu_docentes == "2":
                guardar_nuevo_docente()
            elif opcion_submenu_docentes == "3":
                actualizar_docente()
            elif opcion_submenu_docentes == "4":
                eliminar_docente()
            elif opcion_submenu_docentes == "0":
                return
            else:
                print("Opción Inválida, vuelva a ingresar...")
                return
            
        elif opcion_menu == "0":
            break
        else:
            print("Opción Inválida, vuelva a ingresar...")

ejecucion_principal()