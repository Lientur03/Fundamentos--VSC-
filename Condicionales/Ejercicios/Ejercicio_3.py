# Pida al usuario que ingrese su sueldo y
# Defina el monto de impuesto de segunda categoría que debe pagar a SII
# https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2024.htm 

# [Diciembre 2024]
# $ 908.469,01	    $ 2.018.820,00	0,04	$ 36.338,76	    2,20%
# $ 2.018.820,01	$ 3.364.700,00	0,08	$ 117.091,56	4,52%
# $ 3.364.700,01	$ 4.710.580,00	0,135	$ 302.150,06	7,09%
# $ 4.710.580,01	$ 6.056.460,00	0,23	$ 749.655,16	10,62%
# $ 6.056.460,01	$ 8.075.280,00	0,304	$ 1.197.833,20	15,57%
# $ 8.075.280,01	$ 20.861.140,00	0,35    Y MÁS 27,48%

def definir_impuesto(sueldo):
    sueldo_int = int(sueldo)
    impuesto = 0

    if sueldo_int >= 8075280:
        impuesto = ((sueldo_int * 27.48)/100)
    elif sueldo_int >= 6056460 and sueldo_int < 8075280:
        impuesto = ((sueldo * 15.57)/100)
    elif sueldo_int >= 4710580 and sueldo_int < 6056460:
        impuesto = ((sueldo_int * 10.62)/100)
    elif sueldo_int >= 3364700 and sueldo_int < 4710580:
        impuesto = ((sueldo_int * 7.09)/100)
    elif sueldo_int >= 2018820 and sueldo_int < 3364700:
        impuesto = ((sueldo_int * 4.52)/100)
    elif sueldo_int >= 908469 and sueldo_int < 2018820:
        impuesto = ((sueldo_int * 2.2)/100)
    else:
        impuesto = 0
    print(f"El impuesto de segunda categoría a pagar con el sueldo de {sueldo_int} es: ${impuesto}")

sueldo_ingresado = input("Ingrese su sueldo: ")
definir_impuesto(sueldo_ingresado)