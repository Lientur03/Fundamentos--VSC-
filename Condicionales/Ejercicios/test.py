while True:
    try:
        numerador = float(input('Ingrese el numerador: '))
        denominador = float(input('Ingrese el denominador: '))

        division = numerador/denominador
        print(f'{numerador} / {denominador} = {division} ')

        respuesta = input('Desea continuar ¿Sí o no?: ')
        if respuesta.lower() == 'no' or respuesta.lower() == 'n':
            break
    except ValueError:
        print("El número no corresponde a entero")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except:
        print("No se puede realizar la operación")