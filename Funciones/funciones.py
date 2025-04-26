# # Definición de funciones

# # Ejercicio 1
# def saludar(nombre):
#     print(f"Hola Universitario {nombre}")


# # Llamar a una función
# nombre = input("Ingrese su nombre: ")
# saludar(nombre)

# # Ejercicio 2
# def sumar(a,b):
#     resultado = a + b
#     print(resultado)

# print()
# sumar(12,8)


# # Ejercicio 3
# print()
# num_1 = int(input("Ingresa el primer número: "))
# num_2 = int(input("Ingresa el segundo número: "))

# sumar(num_1, num_2)


from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11