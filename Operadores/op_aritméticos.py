# Operadores aritméticos, permiten realizar operaciones entre variables.

numero_1 = 5
numero_2 = 7
numero_3 = 9
numero_4 = 3
numero_5 = 10

nombre = "Andrés"
apellido = "Hormazábal"

# Operador SUMA
suma = numero_1 + numero_2
print(suma)

# Operador Concatenación
concatenacion = nombre + " " + apellido
print(concatenacion)

# Operador RESTA
resta = numero_1 - numero_2
print(resta)

# Operador MULTIPLICACIÓN
multiplicacion = numero_1 * numero_2
print(multiplicacion)

multiplicar_texto = nombre * numero_1
print(multiplicar_texto)

exponente = numero_1 ** numero_2 # Potencias
print(exponente)

# Operador DIVISIÓN
division = numero_5 / numero_1
print(division)
print(type(division))

divison_baja = numero_3 // numero_4
print(divison_baja)
print(type(divison_baja))
print(numero_1 / numero_5)

# Mostrar con X la cantidad de decimales
print(f"{numero_1 / numero_5:.2f}")
print(f"{numero_1 / numero_5:.4f}")

# Operador RESTO
op_resto = numero_3 % numero_1
print(op_resto)