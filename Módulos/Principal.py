import Operaciones

def bienvenida():
    print()
    print("+-*/ Super Calculadora Python +-*/")
    print("====================================")
    print()

def menu():    
    print("Seleccione su Operación")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    print("0: Salir")
    print()

def ejecutar_calculadora():
    while True:
        print()
        num_1 = float(input("Ingrese Número 1: "))
        num_2 = float(input("Ingrese Número 2: "))
        menu()
        opcion = input("Seleccione su opción (0-4): ")
        
        resultado = 0
        operacion = ""

        if opcion == "1":
            resultado = Operaciones.op_suma(num_1, num_2)
            operacion = "+"
        elif opcion == "2":
            resultado = Operaciones.op_resta(num_1, num_2)
            operacion = "-"
        elif opcion == "3":
            resultado = Operaciones.op_multiplicacion(num_1, num_2)
            operacion = "*"
        elif opcion == "4":
            resultado = Operaciones.op_division(num_1, num_2)
            operacion = "/"
        elif opcion == "0":
            print("Saliendo del sistema básico de la Calculadora en Python")
            break
        else:
            print("Opción Inválida... Vuelva a Ingresar...")
            return
        
        if resultado == None:
            print("Operación NO PERMITIDA, ¡NO SE PUEDE DIVIDIR POR 0!")
        else:
            print(f"{num_1} {operacion} {num_2} = {resultado}")

ejecutar_calculadora()