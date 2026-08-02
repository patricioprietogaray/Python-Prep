# 🚀 Proyecto: Sistema de Gestión de una Academia # de Arte
# 📋 Descripción del problema
# Vas a construir el motor de datos para una academia. 
# El sistema debe gestionar cursos, estudiantes, 
# profesionales asignados y las etiquetas de especialidades de la academia.
# 🛠️ Requisitos técnicos (Estructuras de datos)
# Debes usar cada estructura de la siguiente manera:
#     • Diccionarios: 
# Para almacenar el catálogo de cursos. 
# La clave será el código del curso y el valor será otro diccionario con el nombre, 
# precio y cupo máximo.
#     • Tuplas: 
# Para representar a los estudiantes de forma inmutable. 
# Cada estudiante será una tupla con: 
# (ID_estudiante, nombre, edad). [1, 2]
#     • Listas: 
# Para llevar el registro de inscripciones. 
# Será una lista que contenga las tuplas de los estudiantes 
# inscritos en un curso específico. [1]
#     • Conjuntos (Sets): 
# Para las áreas de especialización de la academia 
# (ej. "Pintura", "Escultura", "Digital"). 
# Servirán para evitar duplicados y hacer cruces de datos. [1]

# 💻 Consigna del ejercicio
# Escribe un script en Python que realice los siguientes pasos numéricos:
#     1. Inicializar el catálogo: 
# Crea el diccionario de cursos con al menos 3 materias diferentes.
#     2. Crear el set de especialidades: 
# Define un conjunto con las áreas de arte disponibles.
#     3. Registrar alumnos: 
# Crea una lista de control de inscripciones vacía.
#     4. Simular inscripciones: 
# Agrega un par de tuplas de estudiantes a la lista de un curso.
#     5. Validar cupos: 
# Añade una estructura condicional que verifique si la longitud 
# de la lista de inscritos supera el cupo máximo definido 
# en el diccionario del curso.
#     6. Mostrar reporte: 
# Imprime en pantalla el menú de cursos, 
# los alumnos inscritos y las especialidades totales utilizando bucles for. [1, 2]

# 💡 Ejemplo de cómo estructurar los datos iniciales
# python
# # 1. Diccionario de cursos
# cursos = {
#     "ART-01": {"nombre": "Pintura Óleo", "precio": 150, "cupo": 2},
#     "ART-02": {"nombre": "Escultura Arcilla", "precio": 180, "cupo": 15}
# }

# # 2. Conjunto de especialidades
# especialidades = {"Tradicional", "Escultura", "Digital", "Historia"}

# # 3. Lista de inscritos para el curso ART-01 (utilizando tuplas)
# inscritos_oleo = [
#     (101, "Ana Gómez", 22),
#     (102, "Luis Pérez", 29)
# ]



# catalogo_cursos = {
#     'ART-01': {'nombre':'Pintura al óleo', 'precio':45000, 'cupo': 12},
#     'ART-02': {'nombre':'Escultura en arcilla', 'precio':55000, 'cupo':15},
#     'ART-03': {'nombre':'Historia del Arte', 'precio':45000, 'cupo':10},
#     'ART-04': {'nombre':'Digitalización del Arte', 'precio':45000, 'cupo':19},
#     'ART-05': {'nombre':'Preparación de arcillas', 'precio':65000, 'cupo':15}
# }
# estudiantes = [
#     (101, 'GOMEZ ANA', 22),
#     (102, 'GOMEZ JOSE', 24),
#     (101, 'PEREZ CARLA', 28)
# ]

# especializacion = {'Tradicional', 'Escultura', 'Digital', 'Historia'}

# inscripciones = {
#     'Art-01': [],
#     'Art-02': [],
#     'Art-03': [],
#     'Art-04': [],
#     'Art-05': []
# }

# modulo de color
from colorama import Fore, Back, init, Style
init(autoreset=True)

# crear las variables para control de bucle
cantidad_cursos = 5
cantidad_estudiantes = 5
cantidad_especializacion = 4

# crear variables complejas para almacenar datos: lista, tupla, diccionarios y conjuntos
catalogo_cursos = dict() # diccionario
estudiantes = list()
estudiante = tuple()
inscripciones = dict()
especializacion = set()
# pre_inscripcion = dict()


# cargar los cursos
for cc in range(1,cantidad_cursos + 1):
    # input datos de cursos
    curso_codigo = 'ART-0' + str(cc)
    if cc == 1: 
        nombre_curso = 'Pintura al óleo'
        precio_curso = 45000.00
        cupo_curso = 12
    elif cc == 2: 
        nombre_curso = 'Escultura en arcilla'
        precio_curso = 55000.00
        cupo_curso = 15
    elif cc == 3: 
        nombre_curso = 'Historia del Arte'
        precio_curso = 45000.00
        cupo_curso = 10
    elif cc == 4: 
        nombre_curso = 'Digitalización del Arte'
        precio_curso = 45000.00
        cupo_curso = 19
    elif cc == 5: 
        nombre_curso = 'Preparación de arcillas'
        precio_curso = 65000.00
        cupo_curso = 15
    else:
        # print("El curso no existe! (son cinco cursos habilitados para la inscripición)")
        continue

    # ingreso manual de datos
    # nombre_curso = input("Ingrese el nombre del curso: ")
    # precio_curso = float(input("Ingrese el precio del curso: "))
    # cupo_curso = int(input("Ingrese el cupo máximo que tendrá el curso: "))

    
    # input catalogo de cursos
    catalogo_cursos[curso_codigo]=dict()
    catalogo_cursos[curso_codigo]['nombre'] = nombre_curso
    catalogo_cursos[curso_codigo]['precio'] = precio_curso
    catalogo_cursos[curso_codigo]['cupo'] = cupo_curso
    # input para pre_inscripciones
    # pre_inscripcion[curso_codigo] = list()
    # input de inscripciones (vacio)
    inscripciones[curso_codigo] = list()

# cargar los estudiantes
for ee in range(101, cantidad_estudiantes + 101):
    # (101, 'GOMEZ ANA', 22)
    estudiante_codigo = ee
    if estudiante_codigo == 101:
        estudiante_nombre = 'GOMEZ ANA'
        estudiente_edad = 22
    elif estudiante_codigo == 102:
        estudiante_nombre = 'PEREZ ANDREA'
        estudiente_edad = 25
    elif estudiante_codigo == 103:
        estudiante_nombre = 'CONTRERA GABRIELA'
        estudiente_edad = 38
    elif estudiante_codigo == 104:
        estudiante_nombre = 'GONZALEZ DANIEL'
        estudiente_edad = 39
    elif estudiante_codigo == 105:
        estudiante_nombre = 'DE AGUSTINI NICOLAS'
        estudiente_edad = 52
    else:
        continue

    estudiante = (estudiante_codigo, estudiante_nombre, estudiente_edad)
    estudiantes.append(estudiante)

for es in range(0, cantidad_especializacion + 1):
    especializ = ""
    if es == 0:
        especializ = 'Tradicional'
    elif es == 1:
        especializ = 'Escultura'
    elif es == 2:
        especializ = 'Digital'
    elif es == 3:
        especializ = 'Historia'
    else:
        continue
    especializacion.add(especializ)

# inscribir los alumnos a pintura
curso_codigo = 'ART-01'
opc_insc_p_oleo = input("¿Desea inscribir alumnos a la Carrera Pintura al óleo? (S/N): ").upper()
if opc_insc_p_oleo == 'S':
    print("\nInscripción de alumnos a la Carrera de Pintura al óleo:\n")
    pintura = list()
    while True:
        print(f"En la carrera de Pintura al óleo tiene los siguientes alumnos:\n{pintura}")
        alum_codigo = int(input("Ingrese el código del alumno que desea inscribir (0 para Salir): "))
        if alum_codigo != 0:
            if not alum_codigo in pintura:
                print(Fore.GREEN + f"Se agrega el alumno {alum_codigo}")
                pintura.append(alum_codigo)
            else:
                print(Fore.RED + f"El alumno {alum_codigo} ya se encuentra inscripto")
        else:
            break
    print(f"Alumnos en PreInscripcion:\n{pintura}")
    insc = input("¿Desea inscribirlos? (S/N)").upper()
    if insc == 'S':
        inscripciones[curso_codigo]=pintura

print(f"Catálogo de cursos: \n{catalogo_cursos}\n")
# print(f"Pre_inscripciones: \n{pre_inscripcion}\n")
print(f"Inscripciones: \n{inscripciones}\n")
print(f"Estudiantes anotados: \n{estudiantes}\n")
print(f"Especializaciones de las carreras dictadas: \n{especializacion}\n")



# Falta el resto de las carreras
# falta el reporte
# Se irá haciendo a medida que el curso avance....






# #     if opc_insc == 'N' or opc_insc == None:
# #         if len(pintura)>0:
# #             pre_inscripcion['ART-01']=pintura
# #         break
# #     elif opc_insc == 'S':
# #         print(f"En la carrera de Pintura al óleo tiene los siguientes alumnos:\n{pintura}")
# #         alum_codigo = int(input("Ingrese el código del alumno que desea inscribir: "))
# #         if len(pintura) < 1:
# #             print('sin alumnos en la carrera de pintura al óleo')
# #             print(f"Se agrega el alumno {alum_codigo}")
# #             pintura.append(alum_codigo)
# #             continue
# #         # Verificamos si el código del alumno YA existe dentro de la lista
# #         if alum_codigo in pintura:
# #             print(f"El código de alumno {alum_codigo} ya se encuentra inscripto!")
# #         else:
# #             pintura.append(alum_codigo)
# #             continue


# #         else:
# #             print('hay alumnos en la carrera de pintura al óleo')
# #             if alum_codigo in pintura:
# #                 print("verdadero para pintura[alum_codigo]")
# #             else:
# #                 print("falso para pintura[alum_codigo]")
# #         pintura.append(alum_codigo)
# # print(pintura)


#         # if pintura.index(alum_codigo) >= 0:
#         #     indice_alumno_pintura = pintura.index(alum_codigo)
#         #     print(indice_alumno_pintura)
#         # else:
#         #     print(f'no existe el codigo {alum_codigo}!!!!')
            

#         # if len(pintura) > 0:
#         #     if pintura.index(alum_codigo) >= 0:
#         #         print(pintura.index(alum_codigo))
#         #     else:
#         #         print('No hay elementos que mostrar en la inscripción!!!!')
#         # else:
#         #     pintura.append(alum_codigo)

    
    
    
#     # pre_inscripcion['ART-01']=pintura



# # escultura = list()


# # pintura.append(101)
# # pintura.append(102)
# # pre_inscripcion['ART-01']=pintura
# # pre_inscripcion['ART-01']=102
# # pre_inscripcion['ART-02']=101
# # pre_inscripcion['ART-02']=103




# print(f"Catálogo de cursos: \n{catalogo_cursos}\n")
# # print(f"Pre_inscripciones: \n{pre_inscripcion}\n")
# print(f"Inscripciones: \n{inscripciones}\n")
# print(f"Estudiantes anotados: \n{estudiantes}\n")
# print(f"Especializaciones de las carreras dictadas: \n{especializacion}\n")


