# Podemos usar herramientas con nuestras variables

# f es para formatear
# del permite borrar variables
nombre_completo = input("Ingrese su nombre completo: ")
saludar = f"Buenos días don {nombre_completo}, ¿Cómo estás?"
# del saludar
print(saludar)

# IN permite buscar un texto dentro de otro
busqueda_texto = "Andrés" in nombre_completo
print(busqueda_texto)

busqueda_texto = "és" in nombre_completo
print(busqueda_texto)

busqueda_texto = "As" in nombre_completo
print(busqueda_texto)

texto = """¿Qué es Lorem Ipsum?
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor 
(N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. 
No sólo sobrevivió 500 años, 
sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. 
Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, 
y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.
"""

busqueda_in = input("Ingrese su texto de búsqueda con IN: ")
busqueda_texto = busqueda_in in texto
print(busqueda_texto)

# FIND permite buscar un texto dentro de otro
# Entrega la primera posición de la primera coincidencia de texto
# Entrega -1 si no lo encuentra
busqueda_find = input("Ingrese su texto de búsqueda con FIND: ")
busqueda_2 = texto.find(busqueda_find)
print(f"Buscando con FIND: {busqueda_2}")

# RFIND permite buscar un texto dentro de otro
# Entrega la primera posición de la primera coincidencia de texto
# Entrega -1 si no lo encuentra
nueva_busqueda_2 = texto.rfind(busqueda_find)
print(f"Buscando con RFIND: {nueva_busqueda_2}")

# COUNT permite buscar un texto dentro de otro
# Entrega la cantidad de ocurrencias del texto
# Entrega 0 si no lo encuentra
numero_ocurrencias = texto.count(busqueda_find)
print(f"Buscando con COUNT: {numero_ocurrencias}")

# INDEX permite buscar un texto dentro de otro
# Entrega el índice de la primera posición de la primera coincidencia de texto
# Entrega ERROR si no lo encuentra
busqueda_index = input("Ingrese su texto de búsqueda con INDEX: ")
busqueda_3 = texto.index(busqueda_index)
print(f"Buscando con INDEX: {busqueda_3}")