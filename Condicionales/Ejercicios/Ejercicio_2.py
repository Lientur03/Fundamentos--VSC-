# Escribir un programa que pida al usuario un número entero e indique si es par o impar.

def par_impar(número):
    modulo = número % 2
    if modulo % 2 == 0:
      print(f"Su número {número} es par.")
    else:
        print(f"Su número {número} es impar.")

número_ingresado = int(input("Ingrese un número entero: "))
par_impar(número_ingresado)