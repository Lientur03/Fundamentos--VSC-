# Escribir un programa que almacene la cadena de cararacteres 'CONTRASEÑA' en una variable.
# Luego le pida al usuario que ingrese la contraseña y el sistema debe indicar por pantalla
# si la contraseña ingresada es correcta

def validacion_contraseña(contraseña_usuario):
    CONTRASEÑA = "Universitario INACAPINO"
    if contraseña_usuario == CONTRASEÑA:
        print("CORRECTA")
    else:
        print("INCORRECTA")

CONTRASEÑA_INGRESADA = input("Ingrese su contraseña: ")
validacion_contraseña(CONTRASEÑA_INGRESADA)