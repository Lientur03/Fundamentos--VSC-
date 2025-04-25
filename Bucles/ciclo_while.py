# El ciclo WHILE (Mientras) nos permite ejecutar una serie de acciones
# Mientras una condición lógica sea VERDADERA
# while condicion_logica :
#     ejecutar_tareas

contador_str = input("Ingrese un número entero menor a 50: ")
contador_int = int(contador_str)

while contador_int < 50:
    contador_int = contador_int + 1
    print(f"Su contador es: {contador_int}")

print(f"Ciclo terminado, Usted ingresó el número: {contador_str}")