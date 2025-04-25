diccionario = {
    "Nombre": "Andrés",
    "Apellido": "Hormazábal",
    "Edad": 21,
    "Estudiante": True
}

for elemento in diccionario:
    print(f"La clave es: {elemento}")

print()
for dato in diccionario.items():
    clave = dato[0]
    valor = dato[1]
    print(f"La clave es: {clave} y el valor es: {valor}")