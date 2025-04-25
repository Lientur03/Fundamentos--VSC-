# Datos compuestos son COLECCIONES de elementos o datos que pueden pertenecer a una variable

# LISTAS, Colección ORDENADA de elementos mutables
lista = ["Andrés Hormazábal", 21, True]
print(lista)
print(type(lista))
print(lista[0])
lista[0] = "Andrés Hormazábal Fuentes"
print(lista)
lista.append("Decodificación")
print(lista)

# DICCIONARIOS, Colecciones ORDENADAS de PARES DE ELEMENTOS mutables
diccionario = {
    "nombre": "Andrés Hormazábal", 
    "edad": 21,
    "Eres Universitario?": True
}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
diccionario["nombre"] = "Andrés Hormazábal Fuentes"
print(diccionario)
# print(diccionario.keys())
# diccionario.clear()
# print(f"Diccionario: {diccionario}")

# TUPLAS, colección ordenada INMUTABLE de elementos
tupla = ("Andrés Hormazábal", 21, True)
print(tupla)
print(type(tupla))

print(tupla[0])
# tupla[0] = "Andrés Hormazábal Fuentes"

# CONJUNTOS, colección DESORDENADA de elementos
conjunto = {"Andrés Hormazábal", 21, True}
print(conjunto)
print(type(conjunto))
conjunto.add(78)
print(conjunto)
conjunto.pop()
print(conjunto)