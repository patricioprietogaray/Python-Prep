import sys

# cuando desde el terminal ejecuto el script
# este script puede tener lugar para argumentos



#   py   arg 0   arg1 arg2 arg3
#   py script.py   1    2   3


nombre_script = sys.argv[0]
argumento_01 = sys.argv[1]
argumento_02 = sys.argv[2]
argumento_03 = sys.argv[3]

print(f"""El script es: {nombre_script};
      El primer argumento es: {argumento_01} y es de tipo {type(argumento_01)};
      El primer argumento es: {argumento_02} y
      El primer argumento es: {argumento_03}""")

