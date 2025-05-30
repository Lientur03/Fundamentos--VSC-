from negocio.negocio_asignaturas import 

def menu_principal():
    print()
    print("Sistema Gestión Notas")
    print("=====================")
    print("[1] Gestión de Asignaturas")
    print("[0] Salir")
    print()

def sub_menu_asignaturas():
    print()
    print("Gestión Asignaturas")
    print("===================")
    print("[1] Gestión de Asignaturas")
    print("[2] Agregar Asignatura")
    print("[3] Modificar Asignatura")
    print("[4] Eliminar Asignatura")
    print("[0] Volver al Menú Principal")
    print()    

def ejecucion_principal():
    while True:
        menu_principal()
        opcion_menu = input("Seleccione su Opción [0-1]: ")

        if opcion_menu == "1":
            sub_menu_asignaturas()
            opcion_sub_menu_asignaturas = input("Seleccione su Opción [0-4]: ")

            if opcion_sub_menu_asignaturas == "1":
                pass
            elif opcion_sub_menu_asignaturas == "2":
                pass
            elif opcion_sub_menu_asignaturas == "3":
                pass
            elif opcion_sub_menu_asignaturas == "4":
                pass
            elif opcion_sub_menu_asignaturas == "0":
                pass
            else:
                print("Opción Inválida, vuelva a ingresar...")
                return 
        elif opcion_menu == "0":
            break
        else:
            print("Opción Inválida, vuelva a ingresar...")

ejecucion_principal()