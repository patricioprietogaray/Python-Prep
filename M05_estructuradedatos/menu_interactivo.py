import curses

# Lista de registros (ID, Nombre, Apellido)
registros = [
    {"id": 101, "nombre": "Juan", "apellido": "Pérez"},
    {"id": 102, "nombre": "María", "apellido": "Gómez"},
    {"id": 103, "nombre": "Carlos", "apellido": "López"},
    {"id": 104, "nombre": "Ana", "apellido": "Martínez"},
    {"id": 105, "nombre": "Roberto", "apellido": "Sánchez"},
    {"id": 106, "nombre": "Elena", "apellido": "Fernández"},
]

def menu_clipper(stdscr):
    # Ocultar el cursor titilante
    curses.curs_set(0)
    
    # Índice de la opción actualmente seleccionada
    selected_idx = 0
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        # 1. Encabezado del menú estilo TUI
        titulo = "=== SISTEMA DE REGISTROS (ESTILO CLIPPER 5.2) ==="
        stdscr.addstr(1, max(0, (w - len(titulo)) // 2), titulo, curses.A_BOLD)
        
        instrucciones = "[▲/▼] Navegar  |  [ENTER] Seleccionar  |  [ESC] Salir"
        stdscr.addstr(2, max(0, (w - len(instrucciones)) // 2), instrucciones, curses.A_DIM)
        
        stdscr.addstr(4, 4, f"{'ID':<6} | {'NOMBRE':<15} | {'APELLIDO':<15}", curses.A_UNDERLINE)
        
        # 2. Renderizar la lista de ítems
        for idx, item in enumerate(registros):
            y_pos = 6 + idx
            linea = f"{item['id']:<6} | {item['nombre']:<15} | {item['apellido']:<15}"
            
            if idx == selected_idx:
                # Video invertido (resaltado) como el prompt de Clipper
                stdscr.addstr(y_pos, 4, linea, curses.A_REVERSE | curses.A_BOLD)
            else:
                stdscr.addstr(y_pos, 4, linea)
        
        stdscr.refresh()
        
        # 3. Lectura de teclas
        key = stdscr.getch()
        
        if key == curses.KEY_UP and selected_idx > 0:
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < len(registros) - 1:
            selected_idx += 1
        elif key in [curses.KEY_ENTER, 10, 13]:  # Tecla Enter
            return registros[selected_idx]
        elif key == 27:  # Tecla ESC
            return None

def main():
    # curses.wrapper gestiona la inicialización y restauración de la terminal
    seleccion = curses.wrapper(menu_clipper)
    
    # Resultado tras salir de la interfaz
    if seleccion:
        print("\n--- ÍTEM SELECCIONADO ---")
        print(f"ID       : {seleccion['id']}")
        print(f"Nombre   : {seleccion['nombre']}")
        print(f"Apellido : {seleccion['apellido']}\n")
    else:
        print("\nOperación cancelada por el usuario.\n")

if __name__ == "__main__":
    main()