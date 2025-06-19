while True:
    try:
        numerador = int(input('Ingrese el numerador: '))
        denominador = int(input('Ingrese el denominador: '))

        division = numerador/denominador
        print(f'{numerador} / {denominador} = {division} ')

        respuesta = input('Desea continuar ¿Sí o no?')
        if respuesta.lower() == 'no':
            break
    except:
        print("El número no corresponde a entero")