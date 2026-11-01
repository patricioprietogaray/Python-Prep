import datetime
import sys
import os 

dir_actual = os.getcwd()
archivo = 'clase09-ejer02.csv'
titulos = 'Temperatura, Humedad, Llovio, Hora\n'
titulo_csv = False
bucle = True
bucle_validar = True

# preguntar si existe el archivo csv
if not os.path.isfile(archivo): 
    with open(archivo, 'w', encoding='utf-8') as archi: 
        archi.write(titulos)

# print(sys.argv)
if len(sys.argv) == 4:
    try:
        temp = float(sys.argv[1])
        hume = float(sys.argv[2])
        if sys.argv[3] == "False" or sys.argv[3] == 'false': 
            llovio = False
        else:
            llovio = True
    except TypeError as e: 
        print("""Error en el ingreso de los parámetros... 
              El parámetro debe ser Número entero o decimal. 
              
              Ejemplo de parámetro: 
                python3 clase09_ej2.py 15.0 82.0 True
                python3 clase09_ej2.py 15 82 False""")
        
        sys.exit()
    except ValueError: 
        print("""Error en el ingreso de los parámetros... 
               El parámetro debe ser Número entero o decimal. 
               
               Ejemplo de parámetro: 
                  python3 clase09_ej2.py 15.0 82.0 True
                  python3 clase09_ej2.py 15 82 False""")
        sys.exit()
else: 
    print("Debe ingresar tres parámetros: Temperatura, Humedad, ¿llovió? True/False")
    sys.exit()


with open(archivo, 'a') as arch: 
    arch.write(f"{temp},{hume},{llovio},{datetime.datetime.now()}\n")
    


