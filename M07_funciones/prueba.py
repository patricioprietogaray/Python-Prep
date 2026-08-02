from colorama import Fore, Back, Style

# funciones propias
def menu():
    print(Fore.CYAN + "1. Opción 1" + Style.RESET_ALL)
    print(Fore.BLUE + "2. Opción 2" + Style.RESET_ALL)
    print(Fore.RED + "3. Salir" + Style.RESET_ALL)
    opcion = input("Seleccione una opción: ")
    return opcion

def opcion1():
    print(Fore.GREEN + "Has seleccionado la Opción 1" + Style.RESET_ALL)
    return "1"

def opcion2():
    print(Fore.GREEN + "Has seleccionado la Opción 2" + Style.RESET_ALL)
    return "2"

# main
while True:
    opcion = menu()
    if opcion == "1":
        opc=opcion1()
    elif opcion == "2":
        opc=opcion2()
    elif opcion == "3":
        print(Fore.RED + "Saliendo del programa..." + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Opción no válida. Intente de nuevo." + Style.RESET_ALL)
    print("Opción seleccionada:", opc)



