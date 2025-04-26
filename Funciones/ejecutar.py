from operaciones import op_suma, op_resta, op_multiplicacion, op_division

respuesta = "SI"
while True:
    if respuesta.upper() == "SI":
            numero_1 = float(input("Ingresa el primer número: "))
            numero_2 = float(input("Ingresa el segundo número: "))
            operacion = input("Ingrese la operación a realizar: ")

            if operacion == "+":
                resultado = op_suma(numero_1, numero_2)
            elif operacion == "-":
                 resultado = op_resta(numero_1, numero_2)
            elif operacion == "*":
                 resultado = op_multiplicacion(numero_1, numero_2)
            elif operacion == "/":
                 resultado = op_division(numero_1, numero_2)
            else:
                 print("Operación Inválida")
            print(resultado)