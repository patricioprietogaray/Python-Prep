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
import curses
init(autoreset=True)

# funciones propias

# def menu(stdscr, menu_principal):
#     '''Menú de opciones para el usuario'''
#     # Ocultar el cursor titilante
#     curses.curs_set(0)

#     # Índice de la opción actualmente seleccionada
#     id_menuitem_seleccionado = 0

#     while True: #hacer siempre
#         stdscr.clear() #limpiar pantalla
#         h, w = stdscr.getmaxyx() #obtener tamaño de pantalla
#         # 1. Encabezado del menú estilo TUI
#         titulo = "=== SISTEMA DE GESTIÓN DE ACADEMIA DE ARTE (ESTILO CLIPPER 5.2) ==="
#         stdscr.addstr(1, max(0, (w - len(titulo)) // 2), titulo, curses.A_BOLD)
#         instrucciones = "[▲/▼] Navegar  |  [ENTER] Seleccionar  |  [ESC] Salir"
#         stdscr.addstr(2, max(0, (w - len(instrucciones)) // 2), instrucciones, curses.A_DIM)

#         # 2. Renderizar la lista de ítems
#         for idx, item in enumerate(menu_principal):
#             y_pos = 4 + idx
#             linea = f"{item['id']}. {item['nombre']}"
#             if idx == id_menuitem_seleccionado:
#                 # Video invertido (resaltado) como el prompt de Clipper
#                 stdscr.addstr(y_pos, 4, linea, curses.A_REVERSE | curses.A_BOLD)
#             else:
#                 stdscr.addstr(y_pos, 4, linea)

#         # 3. Lectura de teclas
#         key = stdscr.getch()

#             # teclas de navegación
#         if key == curses.KEY_UP and id_menuitem_seleccionado > 0:
#             id_menuitem_seleccionado -= 1
#         elif key == curses.KEY_DOWN and id_menuitem_seleccionado < len(menu_principal) - 1:
#             id_menuitem_seleccionado += 1
#         elif key in [curses.KEY_ENTER, 10, 13]:  # Tecla Enter
#             return menu_principal[id_menuitem_seleccionado]
#         elif key == 27:  # Tecla ESC
#             return None 


def menu(stdscr, menu_principal):
    '''Menú de opciones interactivo con recuadro estilo Clipper 5.2'''
    curses.curs_set(0)
    id_menuitem_seleccionado = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # 1. Encabezado principal
        titulo = "=== SISTEMA DE GESTIÓN DE ACADEMIA DE ARTE ==="
        stdscr.addstr(1, max(0, (w - len(titulo)) // 2), titulo, curses.A_BOLD)
        
        instrucciones = "[▲/▼] Navegar  |  [ENTER] Seleccionar  |  [ESC] Salir"
        stdscr.addstr(2, max(0, (w - len(instrucciones)) // 2), instrucciones, curses.A_DIM)

        # 2. Calcular dimensiones para el recuadro del menú
        ancho_menu = max(len(f"{item['id']}. {item['nombre']}") for item in menu_principal) + 4
        alto_menu = len(menu_principal) + 2  # +2 para los bordes superior e inferior
        
        start_y = 5
        start_x = max(2, (w - ancho_menu) // 2)

        # 3. Dibujar el recuadro al estilo Clipper 5.2 (Borde con '=')
        borde_horizontal = "=" * (ancho_menu - 2)
        
        # Borde superior e inferior
        stdscr.addstr(start_y, start_x, f"+{borde_horizontal}+", curses.A_BOLD)
        stdscr.addstr(start_y + alto_menu - 1, start_x, f"+{borde_horizontal}+", curses.A_BOLD)

        # Bordes laterales
        for i in range(1, alto_menu - 1):
            stdscr.addstr(start_y + i, start_x, "|", curses.A_BOLD)
            stdscr.addstr(start_y + i, start_x + ancho_menu - 1, "|", curses.A_BOLD)

        # 4. Renderizar las opciones dentro del recuadro
        for idx, item in enumerate(menu_principal):
            y_pos = start_y + 1 + idx
            x_pos = start_x + 2  # Margen interno
            
            # Formatear la línea con espacios para rellenar el ancho de la caja
            texto_opcion = f"{item['id']}. {item['nombre']}"
            linea = f"{texto_opcion:<{ancho_menu - 4}}"

            if idx == id_menuitem_seleccionado:
                # Video invertido (resaltado)
                stdscr.addstr(y_pos, x_pos, linea, curses.A_REVERSE | curses.A_BOLD)
            else:
                stdscr.addstr(y_pos, x_pos, linea)

        stdscr.refresh()

        # 5. Captura de teclas
        key = stdscr.getch()

        if key == curses.KEY_UP and id_menuitem_seleccionado > 0:
            id_menuitem_seleccionado -= 1
        elif key == curses.KEY_DOWN and id_menuitem_seleccionado < len(menu_principal) - 1:
            id_menuitem_seleccionado += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            return menu_principal[id_menuitem_seleccionado]
        elif key == 27:  # Tecla ESC
            return None

def cargar_cursos(catalogo_cursos, inscripciones, cantidad_cursos):
    '''Cargar los cursos en el catálogo y crear la estructura de inscripciones'''
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
            continue
        # print(f"Curso {curso_codigo}: {nombre_curso}, Precio: {precio_curso}, Cupo: {cupo_curso}")
        # input catalogo de cursos
        
        # mas simple de hacer con dict() y no con dict literal
        catalogo_cursos[curso_codigo]={     # catalogo_cursos[curso_codigo]=dict()
            'nombre': nombre_curso,         # catalogo_cursos[curso_codigo]['nombre'] = nombre_curso
            'precio': precio_curso,         # catalogo_cursos[curso_codigo]['precio'] = precio_curso
            'cupo': cupo_curso              # catalogo_cursos[curso_codigo]['cupo'] = cupo_curso
        }        
        inscripciones[curso_codigo] = list()

    return catalogo_cursos, inscripciones

def cargar_estudiantes(estudiantes, cantidad_estudiantes):
    '''Cargar los estudiantes en la lista de control'''
    estudiante = tuple()
    for ee in range(101, cantidad_estudiantes + 101):
    # (101, 'GOMEZ ANA', 22)
        if ee == 101:
            estudiante_nombre = 'GOMEZ ANA'
            estudiente_edad = 22
        elif ee == 102:
            estudiante_nombre = 'PEREZ ANDREA'
            estudiente_edad = 25
        elif ee == 103:
            estudiante_nombre = 'CONTRERA GABRIELA'
            estudiente_edad = 38
        elif ee == 104:
            estudiante_nombre = 'GONZALEZ DANIEL'
            estudiente_edad = 39
        elif ee == 105:
            estudiante_nombre = 'DE AGUSTINI NICOLAS'
            estudiente_edad = 52
        else:
            continue

        estudiante = (ee, estudiante_nombre, estudiente_edad)
        estudiantes.append(estudiante)   
    return estudiantes

def cargar_especializacion(especializacion, cantidad_especializacion):
    '''Cargar las especializaciones en el conjunto'''
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
    return especializacion

# def cargar_inscripciones(catalogo_cursos, estudiantes):
#     '''Cargar las inscripciones en el diccionario de inscripciones'''
#     codigo_cursos = list(catalogo_cursos.keys())
#     estudiantes_inscritos = list(estudiantes)
        
def mostrar_cursos(catalogo_cursos):
    '''Mostrar el catálogo de cursos'''
    print(Fore.YELLOW + Style.BRIGHT + f"\nCatálogo de cursos:" + Style.RESET_ALL + Fore.RESET)
    for codigo, datos in catalogo_cursos.items():
        print(f"Curso {codigo}: {datos['nombre']}, Precio: {datos['precio']}, Cupo: {datos['cupo']}")

def mostrar_reporte(catalogo_cursos, inscripciones, estudiantes, especializacion):
    '''Mostrar el reporte de cursos, inscripciones, estudiantes y especializaciones'''
    print(Fore.YELLOW + Style.BRIGHT + f"\nCatálogo de cursos:" + Style.RESET_ALL + Fore.RESET + f" \n{catalogo_cursos}\n")
    print(Fore.YELLOW + Style.BRIGHT + f"Inscripciones:" + Style.RESET_ALL + Fore.RESET + f"\n{inscripciones}\n")
    print(Fore.YELLOW + Style.BRIGHT + f"Estudiantes anotados:" + Style.RESET_ALL + Fore.RESET + f"\n{estudiantes}\n")
    print(Fore.YELLOW + Style.BRIGHT + f"Especializaciones de las carreras dictadas:" + Style.RESET_ALL + Fore.RESET + f"\n{especializacion}\n")

def main():
    # crear las variables para control de bucle
    cantidad_cursos = 5
    cantidad_estudiantes = 5
    cantidad_especializacion = 4

    # crear variables complejas para almacenar datos: lista, tupla, diccionarios y conjuntos
    catalogo_cursos = dict() # diccionario
    estudiantes = list()
    inscripciones = dict()
    especializacion = set()
    menu_principal = [
        {'id': 1, 'nombre': 'Cargar cursos'},
        {'id': 2, 'nombre': 'Cargar estudiantes'},
        {'id': 3, 'nombre': 'Cargar especializaciones'},
        {'id': 4, 'nombre': 'Mostrar cursos'},
        {'id': 5, 'nombre': 'Mostrar estudiantes'},
        {'id': 6, 'nombre': 'Mostrar reporte'},
        {'id': 0, 'nombre': 'Salir'}
    ]   

    # gestionar el menú principal de opciones para el usuario
    seleccion = curses.wrapper(menu, menu_principal)

    # resultado tras salir de la interfaz
    if seleccion:
        print(f"\n--- OPCIÓN SELECCIONADA ---")
        print(f"ID       : {seleccion['id']}")
        print(f"Nombre   : {seleccion['nombre']}\n")
    else:
        print(f"\nOperación cancelada por el usuario.\n")


    # # crear las variables para control de bucle
    # cantidad_cursos = 5
    # cantidad_estudiantes = 5
    # cantidad_especializacion = 4

    # # crear variables complejas para almacenar datos: lista, tupla, diccionarios y conjuntos
    # catalogo_cursos = dict() # diccionario
    # estudiantes = list()
    # inscripciones = dict()
    # especializacion = set()
    # menu_principal = [
    #     {'id': 1, 'nombre': 'Cargar cursos'},
    #     {'id': 2, 'nombre': 'Cargar estudiantes'},
    #     {'id': 3, 'nombre': 'Cargar especializaciones'},
    #     {'id': 4, 'nombre': 'Mostrar cursos'},
    #     {'id': 5, 'nombre': 'Mostrar estudiantes'},
    #     {'id': 6, 'nombre': 'Mostrar reporte'},
    #     {'id': 0, 'nombre': 'Salir'}
    # ]


    # # menú principal de opciones para el usuario
    # menu(stdscr, menu_principal)

    # # cargar los cursos
    # print(f"{Fore.GREEN}Cargando cursos...")
    # catalogo_cursos, inscripciones = cargar_cursos(catalogo_cursos=catalogo_cursos, inscripciones=inscripciones, cantidad_cursos=cantidad_cursos)
    # # cargar los estudiantes
    # print(f"{Fore.GREEN}Cargando estudiantes...")
    # estudiantes = cargar_estudiantes(estudiantes=estudiantes, cantidad_estudiantes=cantidad_estudiantes)
    # # cargar las especializaciones
    # print(f"{Fore.GREEN}Cargando especializaciones...")
    # especializacion = cargar_especializacion(especializacion=especializacion, cantidad_especializacion=cantidad_especializacion)
    # # mostrar los cursos disponibles
    # mostrar_cursos(catalogo_cursos=catalogo_cursos)
    # # cargar_inscripciones(catalogo_cursos=catalogo_cursos, estudiantes=estudiantes)



    # # # print(f"Catálogo de cursos: \n{catalogo_cursos}\n")
    # # # # print(f"Pre_inscripciones: \n{pre_inscripcion}\n")
    # # # print(f"Inscripciones: \n{inscripciones}\n")
    # # # print(f"Estudiantes anotados: \n{estudiantes}\n")
    # # # print(f"Especializaciones de las carreras dictadas: \n{especializacion}\n")
    # mostrar_reporte(catalogo_cursos=catalogo_cursos, inscripciones=inscripciones, estudiantes=estudiantes, especializacion=especializacion)

if __name__ == "__main__":
    main()