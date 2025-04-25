# Tipo de dato: TEXTO
# Texto de una sola línea
texto_1 = 'Texto 1: texto de una línea'
texto_2 = "Texto 2: texto de una línea"

# Texto de múltiples líneas
texto_3 = '''Texto 3:
texto múltiple
línea'''

print(texto_1)
print(texto_2)
print(texto_3)

# Tipo de dato: NUMÉRICO
# Enteros, integers INT
número_entero = 21
número_prueba = '33'
print(número_entero)
print(type(número_entero))

# Decimales, float FLOAT DEC
número_decimal = 21.5
print(número_decimal)
print(type(número_decimal))

# Datos LÓGICOS, boolean BOOL
dato_booleano = True
print(dato_booleano)
print(type(dato_booleano))

nombre = "Andrés Hormazábal"
edad = 21
print("Hola estimado " + nombre)
print("Hola estimado", nombre)

print("Hola estimado "+ nombre + ", tienes unos maravillosos " + str(edad) + " años.")
print(f"Hola estimado {nombre}, tienes unos maravillosos {edad} años")

print(número_entero/número_decimal)
print(número_entero*número_decimal)
print(número_entero*número_prueba)
print(número_entero+int(número_prueba))