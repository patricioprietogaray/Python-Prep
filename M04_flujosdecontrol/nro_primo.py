# primo=False
# limite_evaluacion=30
# print(f" +++ Numero Primo: 1")
# print(f" +++ Numero Primo: 2")
# print(f" +++ Numero Primo: 3")

# for nro_a_evaluar in range(4,limite_evaluacion+1):
#     print(f" ** Numero a evaluar: {nro_a_evaluar}")
#     for rango_numeros in range(2,nro_a_evaluar):
#         print(f"Rango de numeros: {rango_numeros}")
#         if nro_a_evaluar % rango_numeros == 0:
#             # print(f"division perfecta {rango_numeros}")
#             primo=True
#             break
#     if nro_a_evaluar == rango_numeros + 1:
#         print(f"El numero {nro_a_evaluar} es primo")
#         print(f" +++ Numero Primo: {nro_a_evaluar}")



while True:
    primo=True
    verificar_numero = int(input("Ingrese un numero para verificar si es primo: "))
    if verificar_numero < 4:
        primo=True
    elif verificar_numero >= 4:
        for divisor in range(2, verificar_numero):
            print(f"Verificar el numero {verificar_numero} dividido por {divisor}")
            if verificar_numero > divisor > 1:
                # print("dentro del rango de búsqueda")
                resto = verificar_numero % divisor
                if resto == 0:
                    print("resto 0 y esta dentro del rango de busqueda, no es primo")
                    primo=False

    if primo == True:
        print(f"El numero {str(verificar_numero)} es primo")
    else:
        print(f"El numero {str(verificar_numero)} NO es primo")
        primo=True



            # if verificar_numero % divisor == 0 and (verificar_numero - 1) > divisor > 1:
            #     primo=False
            # else:
            #     primo=True
            # if verificar_numero <= divisor:
            #     primo=False
                # print(verificar_numero % divisor)
            #     continue
            # else:
            #     primo=True
            #     break


    #     print(f"El numero {str(verificar_numero)} es primo")

    #     continue
    # elif verificar_numero >= 4:
    #     for divisor in range(4, verificar_numero):
    #         if verificar_numero % divisor == 0:
    #             print(f"{verificar_numero} no es un número primo!")
    #             break  # Encontró un divisor, no es primo
    #         else:
    #             # Se ejecuta SOLO si el bucle terminó sin hacer ningún break
    #             print(f" +++ Numero Primo: {verificar_numero}")
    #             break
    # otro_numero = input("¿Desea continuar con la búsqueda de números primos?(s/n): ")
    # if otro_numero.lower() == 'n':
    #     break
    