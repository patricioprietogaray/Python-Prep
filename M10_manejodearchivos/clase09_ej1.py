import sys
# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
# + argumento 0 que es el nombre del archivo
if len(sys.argv) == 4:
    print("El nombre del archivo py es: ", sys.argv[0])
    print("El primer parámetro es:",sys.argv[1])
    print("El segundo parámetro es:",sys.argv[2])
    print("El tercer parámetro es:",sys.argv[3])
else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py 1 2 3')