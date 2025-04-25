numero_1 = 5
numero_2 = 4

# Operador EQUIVALENTE
equivalente = numero_1 == 5
print(equivalente)

contraseña_guardada = "programacion_es_muy_dificil"
ingreso_contraseña = input("Ingrese su contraseña:")
acceso = ingreso_contraseña == contraseña_guardada

if acceso == True:
    print("Acceso Concedido")
else: 
    print("Acceso Denegado")

# Operador Distinto de
op_distinto = numero_1 != numero_2
print(f"Operador Distinto de: {op_distinto}")

# Operador MAYOR QUE
op_mayor_que = numero_1 > numero_2
print(f"Operador Mayor que: {op_mayor_que}")

# Operador MAYOR O IGUAL QUE
op_mayor_igual_que = numero_1 >= numero_2
print(f"Operador Mayor o Igual Que: {op_mayor_igual_que}")

# Operador MENOR QUE
op_menor_que = numero_1 < numero_2
print(f"Operador Menor Que: {op_menor_que}")

# Operador MENOR O IGUAL QUE
op_menor_igual_que = numero_1 <= numero_2
print(f"Operador Menor o Igual Que: {op_menor_igual_que}")