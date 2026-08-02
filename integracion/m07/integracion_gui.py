# 🚀 Proyecto: Sistema de Gestión de una Academia de Arte
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
# (ID_estudiante, nombre, edad).
#     • Listas: 
# Para llevar el registro de inscripciones. 
# Será una lista que contenga las tuplas de los estudiantes 
# inscritos en un curso específico.
#     • Conjuntos (Sets): 
# Para las áreas de especialización de la academia 
# (ej. "Pintura", "Escultura", "Digital"). 
# Servirán para evitar duplicados y hacer cruces de datos.

# 💻 Consigna del ejercicio
# Interfaz Gráfica (GUI) con tkinter - Misma funcionalidad que integracion_tui.py

# **************** importar modulos
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import tkinter.font as tkFont

# **************** variables globales
# catálogo de cursos con código de curso como clave y datos dentro de otro diccionario
catalogo_cursos = {
    'ART-01': {'nombre':'Pintura al óleo', 'precio':45000, 'cupo': 12},
    'ART-02': {'nombre':'Escultura en arcilla', 'precio':55000, 'cupo':15},
    'ART-03': {'nombre':'Historia del Arte', 'precio':45000, 'cupo':10},
    'ART-04': {'nombre':'Digitalización del Arte', 'precio':45000, 'cupo':19},
    'ART-05': {'nombre':'Preparación de arcillas', 'precio':65000, 'cupo':15}
}

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

# opciones del menú principal
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


def validar_cupos():
    '''Verifica si alguna inscripción supera el cupo máximo del curso.'''
    errores = []
    for codigo, datos in catalogo_cursos.items():
        inscritos = inscripciones.get(codigo, [])
        if len(inscritos) > datos['cupo']:
            errores.append(f"{codigo} excede cupo: {len(inscritos)} / {datos['cupo']}")
    return errores


class AcademiaApp(tk.Tk):
    """Aplicación principal de la Academia de Arte con interfaz gráfica."""
    
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión - Academia de Arte")
        self.geometry("900x700")
        self.configure(bg='#f0f0f0')
        
        # Fuentes personalizadas
        self.title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.subtitle_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.normal_font = tkFont.Font(family="Helvetica", size=10)
        
        # Mostrar menú principal
        self.show_main_menu()
    
    def clear_window(self):
        """Limpia la ventana principal."""
        for widget in self.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        """Muestra el menú principal."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="MENÚ PRINCIPAL",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para botones
        button_frame = tk.Frame(self, bg='#f0f0f0')
        button_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        for opcion in menu_principal:
            btn = tk.Button(
                button_frame,
                text=f"{opcion['id']}. {opcion['nombre']}",
                font=self.normal_font,
                width=35,
                height=2,
                bg='#3498db',
                fg='white',
                command=lambda op_id=opcion['id']: self.handle_main_menu_option(op_id),
                relief=tk.RAISED,
                cursor="hand2"
            )
            btn.pack(pady=8, fill=tk.X)
        
        # Footer
        footer_frame = tk.Frame(self, bg='#ecf0f1', height=40)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_label = tk.Label(
            footer_frame,
            text="Sistema de Gestión de Academia de Arte",
            font=self.normal_font,
            bg='#ecf0f1',
            fg='#7f8c8d',
            pady=10
        )
        footer_label.pack()
    
    def handle_main_menu_option(self, option_id):
        """Maneja las opciones del menú principal."""
        if option_id == 0:
            self.quit()
        elif option_id == 1:
            self.show_courses_menu()
        elif option_id == 2:
            self.show_students()
        elif option_id == 3:
            self.show_specializations()
        elif option_id == 4:
            self.show_enrollments()
        elif option_id == 5:
            self.show_report()
    
    def show_courses_menu(self):
        """Muestra el menú de cursos."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="MENÚ CURSOS",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para botones
        button_frame = tk.Frame(self, bg='#f0f0f0')
        button_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        for opcion in menu_cursos:
            btn = tk.Button(
                button_frame,
                text=f"{opcion['id']}. {opcion['nombre']}",
                font=self.normal_font,
                width=35,
                height=2,
                bg='#27ae60',
                fg='white',
                command=lambda op_id=opcion['id']: self.handle_courses_menu_option(op_id),
                relief=tk.RAISED,
                cursor="hand2"
            )
            btn.pack(pady=8, fill=tk.X)
    
    def handle_courses_menu_option(self, option_id):
        """Maneja las opciones del menú de cursos."""
        if option_id == 10:
            self.show_main_menu()
        elif option_id == 11:
            self.show_create_course()
        elif option_id == 12:
            self.show_courses_list()
        else:
            messagebox.showinfo("Información", "Funcionalidad en construcción")
            self.show_courses_menu()
    
    def show_create_course(self):
        """Muestra el formulario para crear un curso nuevo."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="CREAR CURSO NUEVO",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para formulario
        form_frame = tk.Frame(self, bg='#f0f0f0')
        form_frame.pack(expand=True, fill=tk.BOTH, padx=30, pady=20)
        
        # Código numérico
        tk.Label(form_frame, text="Código numérico (1-99):", font=self.normal_font, bg='#f0f0f0').pack(anchor=tk.W, pady=(10, 0))
        codigo_entry = tk.Entry(form_frame, font=self.normal_font, width=30)
        codigo_entry.pack(anchor=tk.W, pady=(0, 15))
        
        # Nombre
        tk.Label(form_frame, text="Nombre del curso:", font=self.normal_font, bg='#f0f0f0').pack(anchor=tk.W, pady=(10, 0))
        nombre_entry = tk.Entry(form_frame, font=self.normal_font, width=30)
        nombre_entry.pack(anchor=tk.W, pady=(0, 15))
        
        # Precio
        tk.Label(form_frame, text="Precio:", font=self.normal_font, bg='#f0f0f0').pack(anchor=tk.W, pady=(10, 0))
        precio_entry = tk.Entry(form_frame, font=self.normal_font, width=30)
        precio_entry.pack(anchor=tk.W, pady=(0, 15))
        
        # Cupo
        tk.Label(form_frame, text="Cupo máximo:", font=self.normal_font, bg='#f0f0f0').pack(anchor=tk.W, pady=(10, 0))
        cupo_entry = tk.Entry(form_frame, font=self.normal_font, width=30)
        cupo_entry.pack(anchor=tk.W, pady=(0, 20))
        
        def save_course():
            """Valida y guarda el curso."""
            try:
                codigo_num = int(codigo_entry.get())
                if codigo_num < 1 or codigo_num > 99:
                    messagebox.showerror("Error", "El código debe estar entre 1 y 99")
                    return
                
                codigo_formateado = f"ART-{codigo_num:02d}"
                
                if codigo_formateado in catalogo_cursos:
                    messagebox.showerror("Error", f"El curso {codigo_formateado} ya existe")
                    return
                
                nombre = nombre_entry.get().strip()
                if not nombre:
                    messagebox.showerror("Error", "El nombre no puede estar vacío")
                    return
                
                precio = float(precio_entry.get())
                if precio <= 0:
                    messagebox.showerror("Error", "El precio debe ser mayor a 0")
                    return
                
                cupo = int(cupo_entry.get())
                if cupo <= 0:
                    messagebox.showerror("Error", "El cupo debe ser mayor a 0")
                    return
                
                # Confirmación
                confirmacion = messagebox.askyesno(
                    "Confirmación",
                    f"¿Desea crear el curso:\n\nCódigo: {codigo_formateado}\nNombre: {nombre}\nPrecio: {precio}\nCupo: {cupo}"
                )
                
                if confirmacion:
                    catalogo_cursos[codigo_formateado] = {
                        'nombre': nombre,
                        'precio': precio,
                        'cupo': cupo
                    }
                    inscripciones[codigo_formateado] = []
                    messagebox.showinfo("Éxito", f"Curso {codigo_formateado} creado correctamente")
                    self.show_courses_menu()
                
            except ValueError as e:
                messagebox.showerror("Error", f"Entrada inválida: {str(e)}")
        
        # Botones
        button_frame = tk.Frame(form_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=20)
        
        btn_save = tk.Button(
            button_frame,
            text="Guardar Curso",
            font=self.normal_font,
            bg='#27ae60',
            fg='white',
            width=15,
            cursor="hand2",
            command=save_course
        )
        btn_save.pack(side=tk.LEFT, padx=5)
        
        btn_back = tk.Button(
            button_frame,
            text="Volver",
            font=self.normal_font,
            bg='#e74c3c',
            fg='white',
            width=15,
            cursor="hand2",
            command=self.show_courses_menu
        )
        btn_back.pack(side=tk.LEFT, padx=5)
    
    def show_courses_list(self):
        """Muestra la lista de cursos disponibles."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="CURSOS DISPONIBLES",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para lista con scrollbar
        list_frame = tk.Frame(self, bg='#f0f0f0')
        list_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.config(command=listbox.yview)
        
        # Agregar cursos a la lista
        for codigo, datos in catalogo_cursos.items():
            item = f"{codigo}: {datos['nombre']} - Precio: ${datos['precio']} - Cupo: {datos['cupo']}"
            listbox.insert(tk.END, item)
        
        # Botón para volver
        btn_back = tk.Button(
            self,
            text="Volver",
            font=self.normal_font,
            bg='#e74c3c',
            fg='white',
            width=15,
            cursor="hand2",
            command=self.show_courses_menu
        )
        btn_back.pack(pady=10)
    
    def show_students(self):
        """Muestra la lista de estudiantes."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="ESTUDIANTES REGISTRADOS",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para lista
        list_frame = tk.Frame(self, bg='#f0f0f0')
        list_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.config(command=listbox.yview)
        
        # Agregar estudiantes a la lista
        for estudiante in estudiantes:
            item = f"ID: {estudiante[0]} - Nombre: {estudiante[1]} - Edad: {estudiante[2]} años"
            listbox.insert(tk.END, item)
        
        # Botón para volver
        btn_back = tk.Button(
            self,
            text="Volver",
            font=self.normal_font,
            bg='#3498db',
            fg='white',
            width=15,
            cursor="hand2",
            command=self.show_main_menu
        )
        btn_back.pack(pady=10)
    
    def show_specializations(self):
        """Muestra las especializaciones disponibles."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="ESPECIALIZACIONES",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para información
        info_frame = tk.Frame(self, bg='#ecf0f1')
        info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        info_label = tk.Label(
            info_frame,
            text=f"Total especializaciones: {len(especializacion)}",
            font=self.subtitle_font,
            bg='#ecf0f1',
            fg='#2c3e50',
            pady=10
        )
        info_label.pack()
        
        # Frame para lista
        list_frame = tk.Frame(self, bg='#f0f0f0')
        list_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.config(command=listbox.yview)
        
        # Agregar especializaciones a la lista
        for especialidad in sorted(especializacion):
            listbox.insert(tk.END, f"- {especialidad}")
        
        # Botón para volver
        btn_back = tk.Button(
            self,
            text="Volver",
            font=self.normal_font,
            bg='#3498db',
            fg='white',
            width=15,
            cursor="hand2",
            command=self.show_main_menu
        )
        btn_back.pack(pady=10)
    
    def show_enrollments(self):
        """Muestra las inscripciones por curso y la validación de cupos."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="INSCRIPCIONES Y CUPOS",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para lista con scrollbar
        list_frame = tk.Frame(self, bg='#f0f0f0')
        list_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.config(command=listbox.yview)
        
        # Agregar inscripciones
        for codigo, curso in catalogo_cursos.items():
            inscritos = inscripciones.get(codigo, [])
            listbox.insert(tk.END, f"{codigo} - {curso['nombre']} (cupo: {curso['cupo']})")
            if inscritos:
                for alumno in inscritos:
                    listbox.insert(tk.END, f"  • {alumno[0]} - {alumno[1]} - {alumno[2]} años")
            else:
                listbox.insert(tk.END, "  • No hay alumnos inscritos.")
        
        # Validación de cupos
        listbox.insert(tk.END, "")
        errores = validar_cupos()
        if errores:
            listbox.insert(tk.END, "Validación de cupos: hay cursos con sobrecupo")
            for error in errores:
                listbox.insert(tk.END, f"  ⚠️  {error}")
        else:
            listbox.insert(tk.END, "✓ Validación de cupos: todos los cursos están dentro del cupo máximo.")
        
        # Botón para volver
        btn_back = tk.Button(
            self,
            text="Volver",
            font=self.normal_font,
            bg='#3498db',
            fg='white',
            width=15,
            cursor="hand2",
            command=self.show_main_menu
        )
        btn_back.pack(pady=10)
    
    def show_report(self):
        """Muestra el reporte completo."""
        self.clear_window()
        
        # Título
        title_frame = tk.Frame(self, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="REPORTE GENERAL",
            font=self.title_font,
            bg='#2c3e50',
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Frame para lista con scrollbar
        list_frame = tk.Frame(self, bg='#f0f0f0')
        list_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.config(command=listbox.yview)
        
        # Cursos disponibles
        listbox.insert(tk.END, "═════ CURSOS DISPONIBLES ═════")
        for codigo, datos in catalogo_cursos.items():
            item = f"{codigo}: {datos['nombre']} - Precio: ${datos['precio']} - Cupo: {datos['cupo']}"
            listbox.insert(tk.END, item)
        
        # Inscripciones por curso
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "═════ INSCRIPCIONES POR CURSO ═════")
        for codigo, inscritos in inscripciones.items():
            curso = catalogo_cursos.get(codigo, None)
            if curso is None:
                continue
            listbox.insert(tk.END, f"{codigo}: {curso['nombre']}")
            if inscritos:
                for alumno in inscritos:
                    listbox.insert(tk.END, f"  • {alumno[0]} - {alumno[1]} - {alumno[2]} años")
            else:
                listbox.insert(tk.END, "  • No hay alumnos inscritos.")
        
        # Especializaciones
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "═════ ESPECIALIZACIONES ═════")
        listbox.insert(tk.END, f"Total: {len(especializacion)}")
        for especialidad in sorted(especializacion):
            listbox.insert(tk.END, f"- {especialidad}")
        
        # Botón para volver
        btn_back = tk.Button(
            self,
            text="Volver",
            font=self.normal_font,
            bg='#3498db',
            fg='white',
            width=15,
            cursor="hand2",
            command=self.show_main_menu
        )
        btn_back.pack(pady=10)


def main():
    """Función principal que inicializa la aplicación."""
    app = AcademiaApp()
    app.mainloop()


if __name__ == "__main__":
    main()
