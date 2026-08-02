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

# **************** importar modulos
from colorama import Fore, Back, Style  # importa estilos de color para consola (no se usan en este menú)
import curses  # importa la librería curses para crear interfaces en modo texto



# **************** variables globales
# catálogo de cursos con código de curso como clave y datos dentro de otro diccionario
catalogo_cursos = {
    'ART-01': {'nombre':'Pintura al óleo', 'precio':45000, 'cupo': 12},
    'ART-02': {'nombre':'Escultura en arcilla', 'precio':55000, 'cupo':15},
    'ART-03': {'nombre':'Historia del Arte', 'precio':45000, 'cupo':10},
    'ART-04': {'nombre':'Digitalización del Arte', 'precio':45000, 'cupo':19},
    'ART-05': {'nombre':'Preparación de arcillas', 'precio':65000, 'cupo':15}
}
# opciones del menú principal como una lista de diccionarios
menu_principal = [
        {'id': 1, 'nombre': 'CRUD cursos'},
        {'id': 2, 'nombre': 'Mostrar estudiantes'},
        {'id': 3, 'nombre': 'Mostrar especializaciones'},
        {'id': 4, 'nombre': 'Mostrar inscripciones'},
        {'id': 5, 'nombre': 'Mostrar reporte'},
        {'id': 0, 'nombre': 'Salir'}
]
# opciones del submenú de cursos
menu_cursos = [
        {'id': 11, 'nombre': 'Crear un curso'},
        {'id': 12, 'nombre': 'Mostrar los cursos'},
        {'id': 13, 'nombre': 'Actualizar un curso'},
        {'id': 14, 'nombre': 'Borrar un curso'},
        {'id': 10, 'nombre': 'Volver al Menú Principal'}
]

# datos iniciales para completar la resolución del ejercicio
estudiantes = [
    (101, 'ANA GÓMEZ', 22),
    (102, 'LUIS PÉREZ', 29),
    (103, 'CARLA PÉREZ', 28)
]

especializacion = {'Tradicional', 'Escultura', 'Digital', 'Historia'}

inscripciones = {
    'ART-01': [estudiantes[0], estudiantes[1]],
    'ART-02': [estudiantes[2]],
    'ART-03': [],
    'ART-04': [],
    'ART-05': []
}


def dibujar_borde(stdscr, top, left, width, height, title=""):
    ''''''
    # dibuja la esquina superior izquierda y la línea superior horizontal
    stdscr.addstr(top, left, "╔" + "═" * (width - 2) + "╗")
    # dibuja las líneas laterales izquierda y derecha
    for y in range(top + 1, top + height - 1):
        stdscr.addstr(y, left, "║")
        stdscr.addstr(y, left + width - 1, "║")
    # dibuja la línea inferior y las esquinas inferiores
    stdscr.addstr(top + height - 1, left, "╚" + "═" * (width - 2) + "╝")
    # si se proporciona un título, lo escribe dentro del borde
    if title:
        label = f" {title} "
        if len(label) < width - 2:
            stdscr.addstr(top, left + 2, label)


def validar_cupos():
    '''Verifica si alguna inscripción supera el cupo máximo del curso.'''
    errores = []
    for codigo, datos in catalogo_cursos.items():
        inscritos = inscripciones.get(codigo, [])
        if len(inscritos) > datos['cupo']:
            errores.append(f"{codigo} excede cupo: {len(inscritos)} / {datos['cupo']}")
    return errores


def mostrar_texto_tui(stdscr, title, lines):
    '''Muestra una lista de líneas dentro de un cuadro TUI.'''
    curses.curs_set(0)
    stdscr.keypad(True)
    height, width = stdscr.getmaxyx()
    if height < 12 or width < 50:
        mensaje = "Aumenta el tamaño de la terminal y presiona una tecla."
        stdscr.clear()
        stdscr.addstr(0, 0, mensaje[:width - 1])
        stdscr.refresh()
        stdscr.getch()
        return

    box_width = min(80, width - 4)
    box_height = min(len(lines) + 6, height - 4)
    left = (width - box_width) // 2
    top = (height - box_height) // 2

    stdscr.clear()
    dibujar_borde(stdscr, top, left, box_width, box_height, title)
    for idx, line in enumerate(lines[: box_height - 4]):
        stdscr.addstr(top + 2 + idx, left + 2, line[:box_width - 4])

    stdscr.addstr(top + box_height - 2, left + 2, "Presiona cualquier tecla para volver...")
    stdscr.refresh()
    stdscr.getch()


def mostrar_estudiantes_tui(stdscr):
    '''Muestra la lista de estudiantes registrados.'''
    lines = [f"{estudiante[0]} - {estudiante[1]} - {estudiante[2]} años" for estudiante in estudiantes]
    if not lines:
        lines = ["No hay estudiantes registrados."]
    mostrar_texto_tui(stdscr, "ESTUDIANTES REGISTRADOS", lines)


def mostrar_especializaciones_tui(stdscr):
    '''Muestra el conjunto de especializaciones disponibles.'''
    lines = [f"- {especialidad}" for especialidad in sorted(especializacion)]
    lines.insert(0, f"Total especializaciones: {len(especializacion)}")
    mostrar_texto_tui(stdscr, "ESPECIALIZACIONES", lines)


def mostrar_cursos_scroll_tui(stdscr):
    '''Muestra los cursos con scroll cuando exceden 7 entradas.'''
    curses.curs_set(0)
    stdscr.keypad(True)
    height, width = stdscr.getmaxyx()

    if height < 14 or width < 50:
        mensaje = "Aumenta el tamaño de la terminal y presiona una tecla."
        stdscr.clear()
        stdscr.addstr(0, 0, mensaje[:width - 1])
        stdscr.refresh()
        stdscr.getch()
        return

    lines = [f"{codigo}: {datos['nombre']} - Precio: {datos['precio']} - Cupo: {datos['cupo']}"
             for codigo, datos in catalogo_cursos.items()]
    if not lines:
        lines = ["No hay cursos disponibles."]

    max_display = 7  # máximo 7 cursos por pantalla
    start = 0
    ayuda = "Usa ↑/↓ para desplazar, ESC para volver."

    while True:
        stdscr.clear()
        box_width = min(80, width - 4)
        box_height = min(max_display + 6, height - 4)
        left = (width - box_width) // 2
        top = (height - box_height) // 2

        dibujar_borde(stdscr, top, left, box_width, box_height, "CURSOS DISPONIBLES")
        stdscr.addstr(top + 1, left + 2, ayuda[:box_width - 4])

        visible_lines = lines[start:start + max_display]
        for idx, line in enumerate(visible_lines):
            stdscr.addstr(top + 3 + idx, left + 2, line[:box_width - 4])

        page_info = f"Mostrando {start + 1}-{start + len(visible_lines)} de {len(lines)}"
        stdscr.addstr(top + box_height - 2, left + 2, page_info[:box_width - 4])
        stdscr.refresh()

        tecla = stdscr.getch()
        if tecla in (curses.KEY_DOWN, ord('j')) and start + max_display < len(lines):
            start += 1
        elif tecla in (curses.KEY_UP, ord('k')) and start > 0:
            start -= 1
        elif tecla == 27:
            return


def mostrar_inscripciones_tui(stdscr):
    '''Muestra las inscripciones por curso y la validación de cupos.'''
    lines = []
    for codigo, curso in catalogo_cursos.items():
        inscritos = inscripciones.get(codigo, [])
        lines.append(f"{codigo} - {curso['nombre']} (cupo: {curso['cupo']})")
        if inscritos:
            for alumno in inscritos:
                lines.append(f"  • {alumno[0]} - {alumno[1]} - {alumno[2]} años")
        else:
            lines.append("  • No hay alumnos inscritos.")
    errores = validar_cupos()
    lines.append("")
    if errores:
        lines.append("Validación de cupos: hay cursos con sobrecupo")
        lines.extend(errores)
    else:
        lines.append("Validación de cupos: todos los cursos están dentro del cupo máximo.")
    mostrar_texto_tui(stdscr, "INSCRIPCIONES Y CUPOS", lines)


def mostrar_reporte_tui(stdscr):
    '''Muestra el reporte completo de cursos, alumnos inscritos y especializaciones.'''
    lines = ["Cursos disponibles:"]
    for codigo, datos in catalogo_cursos.items():
        lines.append(f"{codigo}: {datos['nombre']} - Precio: {datos['precio']} - Cupo: {datos['cupo']}")
    lines.append("")
    lines.append("Inscripciones por curso:")
    for codigo, inscritos in inscripciones.items():
        curso = catalogo_cursos.get(codigo, None)
        if curso is None:
            continue
        lines.append(f"{codigo}: {curso['nombre']}")
        if inscritos:
            for alumno in inscritos:
                lines.append(f"  • {alumno[0]} - {alumno[1]} - {alumno[2]} años")
        else:
            lines.append("  • No hay alumnos inscritos.")
    lines.append("")
    lines.append(f"Especializaciones totales: {len(especializacion)}")
    for especialidad in sorted(especializacion):
        lines.append(f"- {especialidad}")
    mostrar_texto_tui(stdscr, "REPORTE GENERAL", lines)


def mostrar_menu_principal(stdscr):
    '''Mostrar el menú principal (TUI) y manejar la navegación y selección de opciones.'''
    curses.curs_set(0)  # oculta el cursor del terminal
    stdscr.keypad(True)  # permite leer teclas especiales como flechas
    seleccion = 0        # índice de la opción seleccionada inicialmente
    opciones = menu_principal  # opciones que se mostrarán en el menú principal

    while True:
        stdscr.clear()  # borra la pantalla antes de volver a dibujar
        height, width = stdscr.getmaxyx()  # obtiene el tamaño actual de la ventana

        # si el terminal es muy pequeño, muestra un mensaje y espera una tecla
        if height < 10 or width < 28:
            mensaje = "Aumenta el tamaño de la terminal y presiona una tecla."
            stdscr.addstr(0, 0, mensaje[:width - 1])
            stdscr.refresh()
            stdscr.getch()
            continue

        # calcula el tamaño del cuadro del menú dentro de la ventana
        ayuda = "Usa ↑/↓ para navegar, Enter para seleccionar, ESC para salir."
        max_opcion_len = max(len(f" {opcion['id']}. {opcion['nombre']} ") for opcion in opciones)
        ancho_requerido = max(len(ayuda), max_opcion_len) + 4
        box_width = min(max(ancho_requerido, 60), width - 4)
        box_height = min(12, height - 4)
        left = (width - box_width) // 2
        top = (height - box_height) // 2

        # dibuja el borde del menú y el título
        dibujar_borde(stdscr, top, left, box_width, box_height, "MENÚ PRINCIPAL")
        # texto de ayuda dentro del menú
        stdscr.addstr(top + 1, left + 2, ayuda[:box_width - 4])

        # ancho máximo para cada línea de opción
        max_item_width = max(0, box_width - 6)
        for idx, opcion in enumerate(opciones):
            texto = f" {opcion['id']}. {opcion['nombre']} "
            y = top + 3 + idx
            estilo = curses.A_REVERSE if idx == seleccion else curses.A_NORMAL
            # escribe la opción, recortando/truncando si es necesario
            stdscr.addstr(y, left + 3, texto[:max_item_width].ljust(max_item_width), estilo)

        stdscr.refresh()  # actualiza la pantalla con todo lo dibujado
        tecla = stdscr.getch()  # lee la tecla presionada por el usuario

        if tecla in (curses.KEY_UP, ord('k')):
            seleccion = (seleccion - 1) % len(opciones)  # sube la selección
        elif tecla in (curses.KEY_DOWN, ord('j')):
            seleccion = (seleccion + 1) % len(opciones)  # baja la selección
        elif tecla in (curses.KEY_ENTER, 10, 13):
            opcion = opciones[seleccion]  # opción actual seleccionada
            if opcion['id'] == 0:
                return  # sale del programa
            elif opcion['id'] == 1:
                mostrar_menu_cursos(stdscr, catalogo_cursos)  # abre el submenú de cursos
            elif opcion['id'] == 2:
                mostrar_estudiantes_tui(stdscr)
            elif opcion['id'] == 3:
                mostrar_especializaciones_tui(stdscr)
            elif opcion['id'] == 4:
                mostrar_inscripciones_tui(stdscr)
            elif opcion['id'] == 5:
                mostrar_reporte_tui(stdscr)
            else:
                mensaje = "Funcionalidad en construcción. Presiona cualquier tecla para volver."
                stdscr.addstr(top + box_height - 2, left + 2, mensaje[:box_width - 4])
                stdscr.refresh()
                stdscr.getch()
        elif tecla == 27:
            return  # ESC vuelve o sale del menú

def mostrar_menu_cursos(stdscr, catalogo_cursos):
    '''Mostrar el submenú de cursos (TUI) y manejar la navegación y selección de opciones.'''
    curses.curs_set(0)  # oculta el cursor del terminal
    stdscr.keypad(True)  # permite leer teclas especiales como flechas
    seleccion = 0        # índice de la opción seleccionada
    opciones = menu_cursos  # opciones que se mostrarán en el submenú

    while True:
        stdscr.clear()  # borra la pantalla antes de volver a dibujar
        height, width = stdscr.getmaxyx()  # obtiene el tamaño actual de la ventana

        if height < 10 or width < 28:
            mensaje = "Aumenta el tamaño de la terminal y presiona una tecla."
            stdscr.addstr(0, 0, mensaje[:width - 1])
            stdscr.refresh()
            stdscr.getch()
            continue

        ayuda = "Usa ↑/↓ para navegar, Enter para seleccionar, ESC para volver."
        max_opcion_len = max(len(f" {opcion['id']}. {opcion['nombre']} ") for opcion in opciones)
        ancho_requerido = max(len(ayuda), max_opcion_len) + 4
        box_width = min(max(ancho_requerido, 60), width - 4)
        box_height = min(12, height - 4)
        left = (width - box_width) // 2
        top = (height - box_height) // 2

        dibujar_borde(stdscr, top, left, box_width, box_height, "MENÚ CURSOS")
        stdscr.addstr(top + 1, left + 2, ayuda[:box_width - 4])

        max_item_width = max(0, box_width - 6)
        for idx, opcion in enumerate(opciones):
            texto = f" {opcion['id']}. {opcion['nombre']} "
            y = top + 3 + idx
            estilo = curses.A_REVERSE if idx == seleccion else curses.A_NORMAL
            stdscr.addstr(y, left + 3, texto[:max_item_width].ljust(max_item_width), estilo)

        stdscr.refresh()  # actualiza la pantalla
        tecla = stdscr.getch()  # lee la tecla que presiona el usuario

        if tecla in (curses.KEY_UP, ord('k')):
            seleccion = (seleccion - 1) % len(opciones)
        elif tecla in (curses.KEY_DOWN, ord('j')):
            seleccion = (seleccion + 1) % len(opciones)
        elif tecla in (curses.KEY_ENTER, 10, 13):
            opcion = opciones[seleccion]
            if opcion['id'] == 10:
                return  # vuelve al menú principal
            elif opcion['id'] == 11:
                crear_curso_tui(stdscr, catalogo_cursos)
            elif opcion['id'] == 12:
                mostrar_cursos_scroll_tui(stdscr)
            else:
                mensaje = "Funcionalidad de cursos en construcción. Presiona cualquier tecla..."
                stdscr.addstr(top + box_height - 2, left + 2, mensaje[:box_width - 4])
                stdscr.refresh()
                stdscr.getch()
        elif tecla == 27:
            return  # ESC vuelve al menú principal

ESC_CANCEL = object()


def solicitar_input(stdscr, prompt, row, col, max_length=40, right_limit=None):
    '''Solicita texto al usuario dentro de la pantalla curses.

    Detecta ESC para cancelar la entrada y devuelve ESC_CANCEL.
    '''
    curses.curs_set(1)
    stdscr.keypad(True)
    if right_limit is None:
        _, width = stdscr.getmaxyx()
        right_limit = width - 2

    # Calcular espacio disponible para el prompt y el valor
    available = max(0, right_limit - col)
    prompt = prompt[:available]
    max_input = min(max_length, max(1, available - len(prompt) - 1))

    texto_actual = ''
    while True:
        stdscr.move(row, col)
        stdscr.addstr(row, col, ' ' * available)
        stdscr.addstr(row, col, prompt + texto_actual)
        stdscr.move(row, col + len(prompt) + len(texto_actual))
        stdscr.refresh()

        ch = stdscr.getch()
        if ch in (10, 13):
            break
        if ch == 27:
            curses.curs_set(0)
            return ESC_CANCEL
        if ch in (curses.KEY_BACKSPACE, 127, 8):
            texto_actual = texto_actual[:-1]
        elif 32 <= ch < 127 and len(texto_actual) < max_input:
            texto_actual += chr(ch)

    curses.curs_set(0)
    return texto_actual.strip()


def seleccionar_confirmacion(stdscr, top, left, width, opciones):
    '''Muestra un pequeño menú de confirmación y devuelve la opción seleccionada.'''
    seleccion = 0
    while True:
        for idx, opcion in enumerate(opciones):
            texto = f"{opcion}"
            estilo = curses.A_REVERSE if idx == seleccion else curses.A_NORMAL
            stdscr.addstr(top + idx, left, texto.ljust(width), estilo)
        stdscr.refresh()
        tecla = stdscr.getch()
        if tecla in (curses.KEY_UP, ord('k')):
            seleccion = (seleccion - 1) % len(opciones)
        elif tecla in (curses.KEY_DOWN, ord('j')):
            seleccion = (seleccion + 1) % len(opciones)
        elif tecla in (curses.KEY_ENTER, 10, 13):
            return opciones[seleccion]
        elif tecla == 27:
            return 'Cancelar'


def confirmar_cancelacion(stdscr, top, left, width):
    '''Pregunta al usuario si desea cancelar la operación actual.'''
    dialog_width = min(40, width - 4)
    dialog_height = 7
    dialog_left = left + (width - dialog_width) // 2
    dialog_top = top + (dialog_height if top + dialog_height + 2 < stdscr.getmaxyx()[0] else 0)

    stdscr.clear()
    dibujar_borde(stdscr, dialog_top, dialog_left, dialog_width, dialog_height, "CANCELAR")
    mensaje = "¿Desea cancelar la operación?"
    stdscr.addstr(dialog_top + 2, dialog_left + 2, mensaje[:dialog_width - 4])
    opcion = seleccionar_confirmacion(stdscr, dialog_top + 4, dialog_left + 2, 10, ["Sí", "No"])
    return opcion == "Sí"


def crear_curso_tui(stdscr, catalogo_cursos):
    '''Interfaz TUI para crear un curso nuevo.

    El usuario ingresa un código numérico que se formatea como 'ART-XX',
    luego el nombre, precio y cupo del curso. Antes de guardar el curso,
    se muestra una pantalla de confirmación con las opciones "Confirmar"
    y "Cancelar".
    '''
    curses.curs_set(0)
    stdscr.keypad(True)
    height, width = stdscr.getmaxyx()
    box_width = min(70, width - 4)
    box_height = min(18, height - 4)
    left = (width - box_width) // 2
    top = (height - box_height) // 2

    while True:
        stdscr.clear()
        dibujar_borde(stdscr, top, left, box_width, box_height, "CREAR CURSO NUEVO")
        instrucciones = "Ingrese los datos del curso. Presione Enter para confirmar cada campo."
        stdscr.addstr(top + 1, left + 2, instrucciones[:box_width - 4])

        # Leer y validar el código numérico del curso
        codigo_num = solicitar_input(
            stdscr,
            "Código numérico (1-99): ",
            top + 3,
            left + 2,
            3,
            left + box_width - 2
        )
        if codigo_num is ESC_CANCEL:
            if confirmar_cancelacion(stdscr, top, left, box_width):
                return
            continue
        if not codigo_num:
            stdscr.addstr(top + box_height - 3, left + 2, "El código no puede quedar vacío.")
            stdscr.addstr(top + box_height - 2, left + 2, "Presiona cualquier tecla para reintentar...")
            stdscr.refresh()
            stdscr.getch()
            continue
        try:
            codigo_int = int(codigo_num)
            if codigo_int < 1 or codigo_int > 99:
                raise ValueError
        except ValueError:
            stdscr.addstr(top + box_height - 3, left + 2, "Código inválido. Debe ser un número entre 1 y 99.")
            stdscr.addstr(top + box_height - 2, left + 2, "Presiona cualquier tecla para reintentar...")
            stdscr.refresh()
            stdscr.getch()
            continue

        # Formatear el código en el formato requerido y prevenir duplicados
        codigo_formateado = f"ART-{codigo_int:02d}"
        if codigo_formateado in catalogo_cursos:
            stdscr.addstr(top + box_height - 4, left + 2, f"El curso {codigo_formateado} ya existe.")
            stdscr.addstr(top + box_height - 3, left + 2, "Presiona cualquier tecla para reintentar...")
            stdscr.refresh()
            stdscr.getch()
            continue

        # Leer el nombre del curso y asegurar que no esté vacío
        nombre = solicitar_input(
            stdscr,
            "Nombre del curso: ",
            top + 5,
            left + 2,
            40,
            left + box_width - 2
        )
        if nombre is ESC_CANCEL:
            if confirmar_cancelacion(stdscr, top, left, box_width):
                return
            continue
        if not nombre:
            stdscr.addstr(top + box_height - 4, left + 2, "El nombre no puede quedar vacío.")
            stdscr.addstr(top + box_height - 3, left + 2, "Presiona cualquier tecla para reintentar...")
            stdscr.refresh()
            stdscr.getch()
            continue

        # Leer y validar el precio
        precio_str = solicitar_input(
            stdscr,
            "Precio: ",
            top + 7,
            left + 2,
            15,
            left + box_width - 2
        )
        if precio_str is ESC_CANCEL:
            if confirmar_cancelacion(stdscr, top, left, box_width):
                return
            continue
        try:
            precio = float(precio_str)
            if precio <= 0:
                raise ValueError
        except ValueError:
            stdscr.addstr(top + box_height - 4, left + 2, "Precio inválido. Debe ser un número mayor a 0.")
            stdscr.addstr(top + box_height - 3, left + 2, "Presiona cualquier tecla para reintentar...")
            stdscr.refresh()
            stdscr.getch()
            continue

        # Leer y validar el cupo máximo
        cupo_str = solicitar_input(
            stdscr,
            "Cupo máximo: ",
            top + 9,
            left + 2,
            5,
            left + box_width - 2
        )
        if cupo_str is ESC_CANCEL:
            if confirmar_cancelacion(stdscr, top, left, box_width):
                return
            continue
        try:
            cupo = int(cupo_str)
            if cupo <= 0:
                raise ValueError
        except ValueError:
            stdscr.addstr(top + box_height - 4, left + 2, "Cupo inválido. Debe ser un entero mayor a 0.")
            stdscr.addstr(top + box_height - 3, left + 2, "Presiona cualquier tecla para reintentar...")
            stdscr.refresh()
            stdscr.getch()
            continue

        # Confirmar antes de guardar el curso nuevo
        stdscr.clear()
        dibujar_borde(stdscr, top, left, box_width, box_height, "CONFIRMACIÓN")
        stdscr.addstr(top + 2, left + 2, f"Código: {codigo_formateado}")
        stdscr.addstr(top + 3, left + 2, f"Nombre: {nombre}")
        stdscr.addstr(top + 4, left + 2, f"Precio: {precio}")
        stdscr.addstr(top + 5, left + 2, f"Cupo: {cupo}")

        opcion = seleccionar_confirmacion(stdscr, top + 8, left + 2, 20, ["Confirmar", "Cancelar"])
        if opcion == "Confirmar":
            catalogo_cursos[codigo_formateado] = {
                'nombre': nombre,
                'precio': precio,
                'cupo': cupo
            }
            stdscr.addstr(top + box_height - 3, left + 2, f"Curso {codigo_formateado} creado correctamente.")
            stdscr.addstr(top + box_height - 2, left + 2, "Presiona cualquier tecla para volver al menú...")
            stdscr.refresh()
            stdscr.getch()
            return
        else:
            stdscr.addstr(top + box_height - 3, left + 2, "Creación cancelada. Presiona cualquier tecla para volver...")
            stdscr.refresh()
            stdscr.getch()
            return


def main():
    '''Función principal que inicializa la interfaz de usuario y ejecuta el menú principal.'''
    curses.wrapper(mostrar_menu_principal)  # inicializa curses y ejecuta el menú principal

if __name__ == "__main__":
    main()  # ejecuta el programa si el archivo se ejecuta directamente
