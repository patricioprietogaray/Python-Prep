# calcular el perimetro y el area de un rectángulo
# utilizando argv.
# argv ingresa siempre como cadena de caracteres
#      luego se debe trasformar

import sys 


def calcular_perimetro(a, b):
    return ((a*2) + (b*2))

def calcular_area(a, b):
    return a * b


# verificar que hayan dos argumentos!
if len(sys.argv) < 3:
    print("Error: Faltan argumentos.")
    print("Uso correcto: python area_rectangulo.py <base> <altura>")
    sys.exit()

var1 = float(sys.argv[1])
var2 = float(sys.argv[2])

print(f"Calcular el perímetro: {calcular_perimetro(var1, var2)}")
print(f"Calcular el area: {calcular_area(var1, var2)}")