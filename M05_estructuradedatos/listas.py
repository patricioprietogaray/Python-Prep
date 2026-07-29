# estructuras de datos
# Es un conjunto o colecciones de elementos 
# Lista
# elementos separados por coma entre corchetes
# frutas = ['banana','manzana','pera']
# print(frutas)
# back = frutas.pop()
# print(frutas)
# print(back)

ciudades=[]
otras_ciudades=["Tandil", "San Juan", "Corrientes"]
while True:
    print("*"*80)
    print(f"Menu Principal de Ciudades - {len(ciudades)} elementos")
    print("*"*80)
    print("1. Agregar al final un elemento (append)")
    print("2. Agregar un elemento a un indice determinado (insert)")
    print("3. Buscar un elemento por su índice y mostrar su nombre (index)")
    print("4. Buscar un elemento por su nombre y mostrar su índice ([nombre])")
    print("5. Buscar un elemento por su índice con slice y mostrar sus nombres (index)")
    print("6. Mostrar el tipo de dato de la lista (type)")
    print("7. Mostrar el tipo de dato de un elemento (type)")
    print("8. Borrar un elemento por su indice (pop)")
    print("9. Borrar el último elemento de la lista (pop)")
    print("10. Mostrar toda la lista")
    print("11. Concatenar dos listas")
    print("0. Salir del programa")
    print("*"*80)
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 0: #salir
        break
    elif opcion == 1: #append
        nomb_ciud = input("Ingrese el nombre de la nueva ciudad: ")
        ciudades.append(nomb_ciud)
    elif opcion == 2: #insert
        nomb_ciud = input("Ingrese el nombre de la nueva ciudad: ")
        while True:
            ind = int(input(f"Ingrese el indice (max: {len(ciudades)-1}) para agregar una nueva ciudad: "))
            if ind > len(ciudades):
                print("El indice ingresado es mayor al numero de ciudades admitidas")
                continue
            else:
                break
        ciudades.insert(ind, nomb_ciud)
    elif opcion == 3: #buscar x id
        while True:
            ind = int(input(f"Ingrese el numero de índice a buscar (max: {len(ciudades)-1}): "))
            if ind > len(ciudades):
                continue
            else:
                print(ciudades[ind])
                break
    elif opcion == 4: #buscar por nombre
        nomb_ciud = input("Ingrese el nombre de la ciudad a buscar (respetar Mayúsculas y Minúsculas): ")
        ind = ciudades.index(nomb_ciud)
        print(f"La ciudad {nomb_ciud} es índice {ind}")
    elif opcion == 5: #buscar por slice (rebanadas)
        desde = input("Ingrese el índice del primer elemento a mostrar: ")
        hasta = input("Ingresa el índice del último elemento a mostrar: ")
        if desde != "": #esta "" -> vacio o len en cero
            desde = int(desde)
        else:
            desde = None
        if hasta != "": #esta "" -> vacio o len en cero
            hasta = int(hasta)
        else:
            hasta = None
        print("Lista de elementos")
        print(ciudades[desde:hasta])
    elif opcion == 6: #tipo lista
        print(f"El tipo de la lista ciudades es {type(ciudades)}")
    elif opcion == 7: #tipo dato
        elem_type = int(input("Ingrese el índice del elemento que desea saber su tipo: "))
        print(f"El tipo del un elemento cuyo contenido es {ciudades[elem_type]} de la lista ciudades, su tipo es {type(ciudades[elem_type])}")
    elif opcion == 8: #borrar x id
        elem_borrar = int(input("Ingrese el índice del elemento que desea borrar: "))
        opc = input(f"¿Desea borrar al elemento {ciudades[elem_borrar]}, cuyo índice es {elem_borrar}?: ")
        if opc.lower() == 's':
            elem_elim = ciudades.pop(elem_borrar)
            print(f"Se ha borrado el elemento {elem_elim} de la lista!")
    elif opcion == 9: #borrar ultimo
        print("Se borrará el ultimo elemento....")
        elim = ciudades.pop()
        print(f"Se ha borrado el elemento {elim} de la lista!")
    elif opcion == 10:  #Mostrar toda la lista
        print("Lista de Ciudades")
        print(ciudades)
        print("Fin de la lista de Ciudades")
    elif opcion == 11: #concatenar dos listas
        ciudades.extend(otras_ciudades)
        print("Se han concatenado las listas de 'ciudades' y 'otras_ciudades'")
    elif opcion == 12:
        ciudades.sort()
        print("Se han ordenado los elementos de la lista ciudades")
    else:
        print("Ingrese una opcion correcta 0 a 12")
        continue


    


