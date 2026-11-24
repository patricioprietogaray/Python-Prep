import numpy as np

# Semilla para reproducibilidad
rng = np.random.default_rng(seed=42)

# Matriz de 6 filas (horas 0 a 5) y 4 columnas (sensores S1 a S4) con temperaturas entre 15°C y 45°C
temperaturas = rng.integers(15, 46, size=(6, 4))
print("Matriz inicial:\n", temperaturas)

# Consignas a resolver:

# 1. Generación y tipos: 
#   Creá un arreglo 1D llamado horas que represente 
#   las 6 horas de medición (del 0 al 5) 
#   usando np.arange con tipo de dato np.int8. 

# funcion para convertir una matriz en un vector 1D
horas_totales = temperaturas.flatten()[:6]


# fin_horas_totales = np.arange(horas_totales,np.int8)
# fin_horas_totales = len(horas_totales) - 1
# horas_diaria = fin_horas_totales[0,fin_horas_totales,1]
# horas_diaria = np.arange(horas_totales[::4],np.int8)


print("Arreglo horas:\n", horas_totales)
#   Creá también un arreglo calibracion con 4 valores 
#   equidistantes entre -1.5 y 1.5 usando np.linspace.
#

# 2. Broadcasting y operaciones: 
#   Sumá el vector calibracion a toda la matriz 
#   temperaturas para obtener una nueva matriz 
#   temp_calibrada.

# 3. Slicing y copias: 
#   Extraé una copia independiente (usando .copy()) 
#   de las mediciones correspondientes a las últimas 
#   3 horas y los últimos 2 sensores. 
#   Modificá el primer elemento de esa copia 
#   a 99.9 y verificá que temp_calibrada no haya cambiado.

# 4. Filtrado booleano: 
#   Obtené un arreglo 1D con todas las temperaturas 
#   de temp_calibrada que sean menores a 20°C 
#   o mayores o iguales a 40°C.

# 5. Ordenamiento y forma: 
#   Aplaná temp_calibrada a 1D, ordenala de forma 
#   descendente y volvé a darle forma de matriz 
#   de 3 filas x 8 columnas.

