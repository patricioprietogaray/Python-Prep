# personas.py
from datetime import date

class Persona:
    def __init__(self):
        self.__codigo = 0
        self.__nombre = ""
        self.__tipo_documento = ""
        self.__nro_documento = ""
        self.__fecha_nacimiento = ""
    
    def ingresar_datos(self):
        self.__ingresar_nombre()
        self.__ingresar_tipo_doc()
        self.__ingresar_nro_doc()
        print("***********************Los datos ingresados son ********************")
        print(self.__mostrar_datos_ingresados())
        
    
    def __ingresar_nombre(self):
        self.__nombre = input("Ingrese el nombre del alumno: ")
        
    def __ingresar_tipo_doc(self):
        tipo = int(input("Ingrese el tipo de documento (1.DNI 2.LC 3.LE 4.PASAPORTE ARGENTINO 0.SIN DOCUMENTO ARGENTINO): "))
        if tipo == 1:
            self.__tipo_documento = 'DNI'
        elif tipo == 2:
            self.__tipo_documento = 'LC'
        elif tipo == 3:
            self.__tipo_documento = 'LE'
        elif tipo == 4:
            self.__tipo_documento = 'PASAPORTE ARGENTINO'
        elif tipo == 0:
            print("Debe nacionalizarse!")
            self.__tipo_documento = 'Z'
        else:
            print("Opción incorrecta (0 - 4)")
            
    def __ingresar_nro_doc(self):
        self.__nro_documento = int(input("Ingrese el numero de documento: "))
    
    def __mostrar_datos_ingresados(self):
        print('Nombre: ', self.__nombre)
        print('Tipo de docuemnto: ', self.__tipo_documento, "- Nro: ", self.__nro_documento)
        
