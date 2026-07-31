# iterables

# son fundamentales en Python
# son la base de operaciones de procesamiento 
#     de datos 
# son claves en la manipulacion de estructuras 

lista=[1,2,3,4,5,6]
i=0
while i < len(lista):
    print(lista[i])
    i += 1

# iterar en python significa repetir una accion
# o conjunto de acciones en un bucle
# hasta que se cumpla una condicion determinada

ista=[1,2,3,4,5,6]
for elemento in lista:
    print(elemento)

# no se necesita una variable de control (como i)
# el valor de cada elemento de la lista se asigna
# a la variable elemento

# el bucle for es mas facil de comprender
# el bucle for se utiliza para iterar sobre una 
# secuencia de valores
# en cada iteracion el ciclo for 
# asigna el siguiente valor de la secuencia 
# a una variable del control del bucle y 
# ejecuta el código con el valor correspondiente


# que es un iterable?
# en python es una clase que puede ser iterada como 
#     listas, strings, diccionarios o tuplas 

lista=[1,2,3,4]
# for elemento in clase_iterable
for e in lista: # e toma el valor de cada elemento
                # presente en la clase iterabla.
    print(e) # muestra el elemento correspondiente

# Se puede iterar una cadena
cadena = "Henry"
for c in cadena:
    print(c)

# Este fragmento crea una variable cadena que 
# contiene la cadena de texto "Henry". 
# Después usa un bucle for para recorrer la cadena 
# carácter por carácter.

# En cada iteración, 
# la variable c toma el siguiente carácter de cadena, 
# y el print(c) muestra ese carácter en una 
# línea separada. El resultado es que se 
# imprimen todas las letras de "Henry" 
# una por una: H, e, n, r, y.

# ------------------------------------




cadena = 'Henry'
for c in enumerate(cadena):
    print(c)

# (0,H), (1,e) ... (4,y)

# En este fragmento se crea la variable 
# cadena con el valor 'Henry'. 
# Luego se utiliza un for con enumerate(cadena).

# enumerate recorre la cadena y 
# en cada iteración devuelve una tupla 
# con el índice y el carácter correspondiente. 
# Por eso, en este caso c no es la letra directamente, 
# sino la pareja (indice, letra). 
# El print(c) mostrará cada tupla, 
# por ejemplo (0, 'H'), (1, 'e'), etc.


# --------------------------------------

cadena='Henry'
for i,c in enumerate(cadena):
    print(f"Indice {i} -> letra {c}")

# En este fragmento de código se define una cadena 
# de texto con el valor Henry. 
# Luego se recorre esa cadena con un for 
# usando enumerate, que devuelve en cada 
# iteración una tupla (indice, elemento).

# Aquí i recibe el índice de cada carácter 
# en la cadena (0, 1, 2, ...) 
# y c recibe el carácter correspondiente. 
# Dentro del bucle se imprime una línea 
# por cada letra, mostrando el índice y 
# la letra con formato Indice {i} -> letra {c}.

# El resultado es una salida ordenada donde se asocia cada posición de la cadena con su carácter, por ejemplo:

# Indice 0 -> letra H
# Indice 1 -> letra e
# Indice 2 -> letra n
# etc.

# enumerate()
# enumerate() es una función incorporada 
# en Python que toma un iterable 
# (como una lista o una cadena) y 
# devuelve un objeto enumerado, 
# que contiene pares de índices 
# y valores correspondientes a 
# cada elemento del iterable.
# Es decir, enumerate() 
# permite recorrer un iterable mientras 
# se tiene acceso tanto al valor como 
# al índice de cada elemento.



# -----------------------------
# range(inicio, fin, paso): 
# genera una secuencia de enteros. 
# Se usa mucho para iterar un número determinado 
# de veces o para acceder a índices.
print("*"*20)
for i in range(0,10,3):
    print(i)

# --------------------
# zip(*iterables): 
# combina varias secuencias elemento a elemento, 
# devolviendo tuplas. 
# Con for puedes recorrer varias listas 
# al mismo tiempo.

num = [1,2,3,4,5]
letr = ['a','b','c','d','e']
for n,l in zip(num,letr):
    print(f"{n} - {l}")


# ---------------------------
# reversed(iterable): 
# devuelve los elementos en orden inverso. 
# Si necesitas iterar al revés, 
# evita gestionar índices manualmente.
num = [5,3,8,15]
for c in reversed(num):
    print(c)
# salida 15,8,3,5

# -------------------
# sorted(iterable): 
# devuelve una lista ordenada del iterable. 
# Permite recorrer valores ya ordenados 
# sin modificar la colección original.
num = [5,3,8,15]
for c in sorted(num):
    print(c)

# devuelve 3,5,8,15

# ---------------------------
# Como saber si una clase es iterable o no?
# 1. consultar la documentacion en python 
# 2. ver si hereda la clase iterable

# se importa el modulo para utilizar 'Iterable'
from collections.abc import Iterable
objetos = [123, "Henry", [1, 2, 3], {"a": 1}]
for obj in objetos:
    print(obj, isinstance(obj, Iterable))
# Resultado: 
# 123 False   
# Henry True 
# [1, 2, 3] True 
# {'a': 1} True

# isinstance()
# El método isinstance() es una función 
# incorporada en Python que se utiliza para 
# comprobar si un objeto es una instancia 
# de una clase o de una subclase de dicha clase. 
# Recibe dos argumentos: 
# el objeto que se quiere comprobar 
# y la clase que se quiere verificar 
# si es su superclase o no. 
# Si el objeto es una instancia de la clase, 
# devuelve True, 
# de lo contrario devuelve False. 
# Es comúnmente utilizado para asegurarse 
# de que un objeto es del tipo de datos 
# correcto antes de procesarlo o manipularlo 
# en alguna forma.

# -----------------------------------


# importar Iterable de collections.abc
from collections.abc import Iterable
# declaro dos variables distintas
cadena = 'Henry'
numero = 9
# utilizar el método isinstance()
isinstance(cadena, Iterable) #resultado True (es iterable)
isinstance(numero, Iterable) #resultado False (no es iterable)


# list conviente a lista una clase iterable 
cadena='Henry'
cadena_lista = isinstance(cadena, Iterable)
print(cadena_lista)
cadena_lista = list(cadena)
print(cadena_lista) # ['H', 'e', 'n', 'r', 'y']

# -----------------------------
# map(func, iterable): 
# aplica una función a cada elemento 
# del iterable y devuelve un iterador 
# con los resultados. 
# Útil para procesar valores antes de iterar.

# filter(func, iterable): 
# devuelve solo los elementos que 
# cumplen una condición. 
# Ideal para iterar sobre un subconjunto filtrado.

# any(iterable) y all(iterable): 
# no iteran directamente para ejecutar 
# código en cada elemento, 
# pero suelen usarse junto con comprensiones 
# y for para evaluar condiciones en colecciones.

# sum(iterable), 
# min(iterable), 
# max(iterable): 
# son funciones de agregación que a menudo 
# se usan en combinación con iterables 
# antes o después de un for.
num = [1,2,3,4]
print(sum(num))  # resultado: 10
print(min(num))  # resultado: 10
print(max(num))  # resultado: 10

# --------------------------------
separado = 'SEPARADO'
print(' *-* '.join(separado))

# Se define la variable separado 
# con la cadena "SEPARADO". 
# Luego se llama al método join sobre 
# la cadena ' *-* ', 
# usando separado como iterable de entrada.

# join toma cada carácter de la 
# cadena separado 
# y los une con el separador ' *-* '. 
# El resultado impreso es la cadena 
# S *-* E *-* P *-* A *-* R *-* A *-* D *-* O, 
# donde entre cada letra aparece el texto *-*.

# ---------------------------------------------------
# iteracion con clase_iterable -> diccionario
mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(f'Imprimir la clave: {i}')
    print(f'Imprimir su valor {mi_dict[i]}')
    print("+"*15)

# salida
# Imprimir la clave: a
# Imprimir su valor 1
# +++++++++++++++
# Imprimir la clave: b
# Imprimir su valor 2
# +++++++++++++++
# Imprimir la clave: c
# Imprimir su valor 3
# +++++++++++++++

# Se define un diccionario mi_dict con tres 
# pares clave-valor: 'a': 1, 'b': 2 y 'c': 3. 
# El bucle for recorre el diccionario directamente, 
# lo que en Python itera sobre las claves por defecto.

# En cada iteración, la variable i toma una clave 
# del diccionario. Primero se imprime la clave 
# con el texto Imprimir la clave: .... 
# Después se accede al valor correspondiente 
# usando mi_dict[i] y se imprime con Imprimir 
# su valor ....

# Finalmente, se imprime una línea de + 
# repetida 15 veces para separar visualmente 
# cada par clave-valor en la salida.


# *******************************************
# *******************************************
# Iteradores

# En esta videoclase nos adentraremos 
# en el concepto de iterador en Python. 
# Como ya sabemos, los objetos iterables 
# pueden ser recorridos en un bucle for, 
# pero ¿cómo se lleva a cabo este 
# proceso de iteración en Python? 
# La respuesta es a través de los iteradores. 
# ¡Aprendamos sobre esto!

# # EJEMPLO:
# tengo un libro que representa una clase Iterable 
#     -> Libro = lista
# cada página es un elemento 
#     -> página = elemento
# cada señalador en el libro (marcapágina) es un iterador
#     -> marcapágina = iterador
#     -> iter()


# La función iter() es una función integrada en 
# Python que devuelve un objeto iterador a 
# partir de un objeto iterable. 

# OBJETO ITERABLE -> iter() -> OBJETO ITERADOR
# (list, tuple,
#  dict, string)

# Un objeto iterable es cualquier objeto 
# en Python que se puede iterar uno a uno. 
# Algunos ejemplos de objetos iterables son 
# listas, tuplas, cadenas y diccionarios.

# La función iter() 
# toma un objeto iterable como argumento 
# y devuelve un objeto iterador. 

# OBJETO_ITERADOR = iter(OBJETO_ITERABLE)

# El objeto iterador se utiliza para acceder 
# a los elementos del objeto iterable de uno en uno. 
# de manera eficiente sin tener que cargar todos 
# los elementos en memoria al mismo tiempo....

# ITERADORES

# iter()

libro_lista=['pagina1','pagina2','pagina3','pagina4']
libro_tuplas = (0,'pagina1')
print(libro_lista)
print(libro_tuplas)
marcapagina_lista=iter(libro_lista)
marcapagina_tupla=iter(libro_tuplas)
print(type(marcapagina_lista)) # list_iterator
print(type(marcapagina_tupla)) # tuple_iterator



# El método next() devuelve el siguiente elemento del 
# objeto iterable en cada llamada.

# CLASE ITERABLE (ej: list)
#   posicion principal antes de los marcadores (sin datos)
#   primer marcador (se accede con next())
#   segundo marcador (se accede con next())
#   ....
#   ultimo marcador (se accede con next())
#   posicion final (lanza error StopIteration)

print(next(marcapagina_lista))
print(next(marcapagina_lista))
print(next(marcapagina_lista))
print(next(marcapagina_lista))

# salida esperada:
# pagina1
# pagina2
# pagina3
# pagina4


# si me pase de la cantidad de marcapáginas
# print(next(marcapagina_lista))
# ---------------------------------------------------------------------------
# StopIteration   Traceback (most recent call last)
# Cell In[5], line 5
#       3 print(next(marcapagina_lista))
#       4 print(next(marcapagina_lista))
# ----> 5 print(next(marcapagina_lista))

# StopIteration:

# ***********************************
# ¿Qué son las excepciones?

# Una excepción es un evento 
# que ocurre durante la ejecución 
# de un programa que interrumpe 
# el flujo normal de instrucciones del programa. 
# Las excepciones se utilizan para manejar errores 
# y otros eventos excepcionales que pueden 
# ocurrir durante la ejecución del programa.

# Cuando una excepción es lanzada, 
# el programa detiene su ejecución normal 
# y se busca un bloque de código que pueda 
# manejar la excepción lanzada. 
# Si no se encuentra un bloque de código 
# que pueda manejar la excepción, 
# el programa termina su ejecución 
# y muestra un mensaje de error.

# utilizar for evita la exception stopIteration!!!
# utilizar try/except envuelto en next evita la interrupcion


# ejemplo
# lista=[0,1,2,3]
# marcador = iter(lista)
# while True:
#     next(marcador)
# tira error exepcion
# ---------------------------------------------------------------------------
# StopIteration          Traceback (most recent call last)
# .....
# ----> 4     next(marcador)

lista=[0,1,2,3]
marcador = iter(lista)
for c in lista:
    print(c)
    next(marcador)
# El fragmento crea una lista lista 
# y un iterador explícito marcador = iter(lista). 
# El bucle for recorre la lista e imprime cada elemento c. 
# Dentro del cuerpo del bucle se llama a 
# next(marcador), que avanza el iterador externo 
# pero descarta su valor.

# Importante: 
# el for crea y usa su propio iterador interno 
# sobre lista, independiente de marcador. 
# Por eso el código imprime todos los 
# elementos (0, 1, 2, 3) 
# mientras que marcador también avanza 
# en paralelo; las llamadas a 
# next(marcador) aquí son redundantes 
# y podrían provocar una excepción 
# StopIteration si se llamaran más veces 
# de las que hay elementos.

# Solucion 1: Simplemente
lista=[66,67,68]
for c in lista:
    print(c)

# Solucion 2:
lista=[100,101,102,103,104] 
marcador = iter(lista)
while True:
    try:
        print(next(marcador))
    except StopIteration:
        print("Ya se paso del ultimo elemento, no hay nada mas que iterar")
        break

    # sentencia zip toma dos o mas iterables
    # y combinarla en una estructura

    # La sentencia zip es una función integrada 
    # de Python que toma dos o más iterables 
    # y los combina en una sola estructura. 
    # Esta estructura se puede utilizar para 
    # iterar simultáneamente a través de 
    # los elementos de los iterables originales. 
    # Por ejemplo, si tienes dos listas, 
    # puedes utilizar la sentencia zip 
    # para combinarlas en una sola lista de tuplas.

    # En la sentencia zip, 
    # se pueden pasar dos o más iterables como argumentos 
    # y se creará un iterador que agrega 
    # los elementos correspondientes de cada iterable. 
    # El iterador se detiene cuando 
    # se agotan los elementos del iterable más corto.

# A tener en cuenta...
# 1 zip() es una función incorporada de Python 
# que toma dos o más secuencias y las combina 
# en una secuencia de tuplas de elementos correspondientes.

# 2 zip() devuelve un objeto de tipo zip, 
# que es una secuencia de tuplas de elementos 
# de los iterables proporcionados.

# 3 zip() es una herramienta útil 
# para combinar datos de múltiples fuentes, 
# como columnas de una tabla o 
# datos de diferentes archivos.

# 4 También es posible usar zip() 
# con más de dos iterables a la vez.

# 5 Es importante tener en cuenta que 
# la secuencia resultante va a contener 
# tantos elementos como la secuencia 
# más corta proporcionada.

lista1 = [1,2,3]
lista2 = ['a','b','c']
combinacion = zip(lista1, lista2)
type(combinacion) # zip
print(combinacion) # <zip object at 0x7f233dfde780>

# muestra el objeto zip en formato de tuplas
for elemento in combinacion:
    print(elemento)

# salida: 
# (1, 'a')
# (2, 'b')
# (3, 'c')

# **********************
lista1 = [1,2,3]
lista2 = ['a','b','c']
combinacion = zip(lista1, lista2)

for i, letr in enumerate(combinacion):
    print(f'El índice {i} corresponde al número {letr[0]} y a la letra {letr[1]}')

# salida: 
# El índice 0 corresponde al número 1 y a la letra a
# El índice 1 corresponde al número 2 y a la letra b
# El índice 2 corresponde al número 3 y a la letra c

# empareja objetos listas e imprime hasta donde pueda mostrar los 
# datos de todos por igual (el 5 de lista1 queda afuera)

lista1 = [1,2,3,4,5]
lista2 = ['a','b','c','d']
combinacion = zip(lista1, lista2)

for i, letr in enumerate(combinacion):
    print(f'El índice {i} corresponde al número {letr[0]} y a la letra {letr[1]}')

# salida:
# El índice 0 corresponde al número 1 y a la letra a
# El índice 1 corresponde al número 2 y a la letra b
# El índice 2 corresponde al número 3 y a la letra c
# El índice 3 corresponde al número 4 y a la letra d

# ******************************************
# añadiendo condicionales
