from Inventario.Version.Versión import versionamiento

def programa_principal():
    Versión = versionamiento()
    while True:
        print(f"*** Manejo inventario {Versión} ***")
        break

programa_principal()