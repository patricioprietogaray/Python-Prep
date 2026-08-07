# # from colorama import Fore, Back, Style

# # # funciones propias
# # def menu():
# #     print(Fore.CYAN + "1. Opción 1" + Style.RESET_ALL)
# #     print(Fore.BLUE + "2. Opción 2" + Style.RESET_ALL)
# #     print(Fore.RED + "3. Salir" + Style.RESET_ALL)
# #     opcion = input("Seleccione una opción: ")
# #     return opcion

# # def opcion1():
# #     print(Fore.GREEN + "Has seleccionado la Opción 1" + Style.RESET_ALL)
# #     return "1"

# # def opcion2():
# #     print(Fore.GREEN + "Has seleccionado la Opción 2" + Style.RESET_ALL)
# #     return "2"

# # # main
# # while True:
# #     opcion = menu()
# #     if opcion == "1":
# #         opc=opcion1()
# #     elif opcion == "2":
# #         opc=opcion2()
# #     elif opcion == "3":
# #         print(Fore.RED + "Saliendo del programa..." + Style.RESET_ALL)
# #         break
# #     else:
# #         print(Fore.RED + "Opción no válida. Intente de nuevo." + Style.RESET_ALL)
# #     print("Opción seleccionada:", opc)






# def repeticion(lista):
#     '''Calcula cuales son los numeros que se repiten en una lista'''
#     lista_repetidos = []
#     for i in lista:
#         if lista.count(i) > 1 and i not in [x[0] for x in lista_repetidos]:
#             lista_repetidos.append((i,lista.count(i)))
#     # return lista_repetidos
#     # el que mas se repite
#     for n in lista_repetidos:
#         if n[1] == max([x[1] for x in lista_repetidos]):
#             return n

# lista = [1, 2, 3, 4, 5, 2, 1, 2, 3, 2]
# listado = repeticion(lista = lista)
# print(listado)

print("Funcion Factorial!")
while True:
    entrada = int(input("Ingrese un número positivo mayor que uno para factorizarlo: "))
    try:
        numero_positivo = int(entrada)
        if numero_positivo > 0:
            print("Es un numero entero positivo!")
            break 
        else:
            print("El número debe ser mayor a uno")
            continue 
    except ValueError:
        print("Debe ingresar un nḿero entero positivo sin letras y sin decimales.")
    
    