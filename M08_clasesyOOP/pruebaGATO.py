from GATO import Gato

salida = False

while True:
    if salida == True: break
    print("La vida del Gato")
    nombre = input("ingrese el nombre del Gato: (S para Salir) ").capitalize()
    if nombre == 'S': break
    color = input("ingrese el color del Gato: ").capitalize()
    raza = input("ingrese la raza del Gato: ").capitalize()
    entrada = int(input("ingrese la edad del Gato: "))
    if isinstance(entrada, int):
        edad = int(entrada)
    else:
        print('Ingrese una edad válida (numero entero)!')
        continue
    sexo = input("ingrese el sexo del Gato (M/H): ").upper()
    energia = 100
    if sexo == 'M':
        sexo = 'Macho'
    else:
        sexo = 'Hembra'
    cat = Gato(nombre, color, raza, edad, sexo, energia)
    
    while cat.energia > 0:
        if cat.energia >= 101:
            print("El gato explotó por comer tanto!")
            salida = True            
            break
        cat.presentarse()
        opc = input('¿Desea que el gato juege, coma, maulle o se presente? (J/C/M/P) Salir (S): ').upper()
        if opc == 'J':
            cat.jugar()
        elif opc == 'C':
            cat.comer()
        elif opc == 'M':
            cat.maullar()
        elif opc == 'P':
            cat.presentarse()
        elif opc == 'S':
            break
            salida=True
        else:
            print('Elija una opción correcta (juegar, comer, maullar, presentarse o salir? (J/C/M/P/S)')
    print('El gato esta cansado, cambia de gato')