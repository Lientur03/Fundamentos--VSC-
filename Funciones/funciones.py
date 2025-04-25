# Definición de funciones

# Ejercicio 1
def saludar(nombre):
    print(f"Hola Universitario {nombre}")


# Llamar a una función
nombre = input("Ingrese su nombre: ")
saludar(nombre)

# Ejercicio 2
def sumar(a,b):
    resultado = a + b
    print(resultado)

print()
sumar(12,8)


# Ejercicio 3
print()
num_1 = int(input("Ingresa el primer número: "))
num_2 = int(input("Ingresa el segundo número: "))

sumar(num_1, num_2)

# Ejercicio 4
print()
def operar(a,b,op):
    resultado = 0
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b != 0:
            resultado = a / b
        else:
             print("El divisor de una división no puede ser 0.")
             return
    else:
        print("Operación incorrecta")
    print(f"{a}{op}{b} = {resultado}")


respuesta = "SI"
while True:
    if respuesta.upper() == "SI":
        while True:
            numero_1 = int(input("Ingresa el primer número: "))
            numero_2 = int(input("Ingresa el segundo número: "))
            operacion = input("Ingrese la operación a realizar: ")

            operar(numero_1, numero_2, operacion)
            respuesta = input("¿Desea realizar otra operación? Responda: SI o NO: ")
        
        else:
            break
