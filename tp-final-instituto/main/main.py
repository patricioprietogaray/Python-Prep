# main.py
# utilizar rutas dinamicas y no absolutas
import sys
import os
# 1. Obtener ruta raiz del proyecto - un nivel arriba de main
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(ruta_raiz)

# 2. Agregar la raíz al sistema para que Python encuentre la carpeta 'clases'
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)
    
# 3. Importar la clase usando la estructura de carpetas
from clases.personas.personas import Persona


# Test de funcionamiento
if (__name__ == '__main__'):
    inscripto = Persona()
    inscripto.ingresar_datos()

    print("hola");
