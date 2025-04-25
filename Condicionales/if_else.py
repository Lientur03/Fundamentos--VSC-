# Estructuras condicionales, se evaluará una condición lógica
# Existirá un set de instrucciones para una respuesta verdadera
# Luego tendremos otro set de instrucciones para una respuesta falsa.

# edad = 21

# if edad >= 18:
#    print(f"Con {edad} años, Usted es Mayor de Edad.")
# else:
#    print(f"Con {edad} años, Usted es Menor de Edad.")

# edad = 15

# if edad < 18:
#    print(f"Con {edad} años, Usted es Menor de Edad.")
# else:
#    print(f"Con {edad} años, Usted es Mayor de Edad.")

# print("Ingrese True o False")
# variable_booleana_str = input()
# variable_booleana = bool(variable_booleana_str) 

# if variable_booleana == True:
#     print("Verdadero")
# else:
#     print("Falso")

# Métodos para convertir tipos de datos
texto = '25'
decimal = 45
booleana = False
entero = 40.5

print(f"Variable de tipo {type(texto)}")
print(f"Variable de tipo {type(decimal)}")
print(f"Variable de tipo {type(booleana)}")
print(f"Variable de tipo {type(entero)}")
  
texto_entero = int(texto) # Convierte a INTEGER int
booleana_texto = str(booleana) # Convierte a STRING str
entero_decimal = float(decimal) # Convierte a DECIMAL float

print("")
print(f"Variable de tipo {type(texto_entero)}")
print(f"Variable de tipo {type(booleana_texto)}")
print(f"Variable de tipo {type(entero_decimal)}")