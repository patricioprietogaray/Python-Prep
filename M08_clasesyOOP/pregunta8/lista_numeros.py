# clase ListaDeNumeros()
class ListaDeNumeros():
    def __init__(self, listado_numeros):
        self.lista = listado_numeros
        self.salida_lista = list()
        self.salida_numero = 0.0
        self.__es_primo = False
        
    def Menu(self):
        print("Menu Principal")
        print("1. De los numeros ingresados calcula cuales son primos")
        print("2. Estadística: Calcular la Moda de los numeros ingresados")
        print("3. Estadística: Calcular la Media de los numeros ingresados")
        print("4. Estadística: Calcular la Mediana de los numeros ingresados")
        print("5. Conversión de Grados: Celsius a Farenheit")
        print("6. Conversión de Grados: Celsius a Kelvin")
        print("7. Conversión de Grados: Farenheit a Celsius")
        print("8. Conversión de Grados: Farenheit a Kelvin")
        print("9. Conversión de Grados: Kelvin a Farenheit")
        print("10. Conversión de Grados: Kelvin a Celsius")
        print("11. Factorial: Calcular el factorial de cada numero")
        print("0. SALIR DEL PROGRAMA")
        opc = int(input("Ingrese su elección: "))
        if opc == 1:
            self.__calcular_primo()
            print(self.salida_lista)
        elif opc == 2:
            repite = self.__calcular_moda()
            print(repite)
        elif opc == 3:
            media = self.__calcular_media()
            print(media)
        elif opc == 4:
            mediana = self.__calcular_mediana()
            # mediana = self.__calcular_mediana()
            print(mediana)
        elif opc == 5:
            print(self.__conversion_grados("celsius","farenheit"))
        elif opc == 6:
            print(self.__conversion_grados("celsius","kelvin"))
        elif opc == 7:
            print(self.__conversion_grados("farenheit","celsius"))
        elif opc == 8:
            print(self.__conversion_grados("farenheit","kelvin"))
        elif opc == 9:
            print(self.__conversion_grados("kelvin","farenheit"))
        elif opc == 10:
            print(self.__conversion_grados("kelvin","celsius"))
        elif opc == 11:
            print(self.__carga_factorial_lista())
        else:
            print("Opción incorrecta (1 - 11)")
    
    def __carga_factorial_lista(self):
        for a in self.lista:
            self.salida_lista.append(self.__factorial_numero(a)) 
        return self.salida_lista
    
    def __factorial_numero(self, nro):
        self.nro = nro
        if self.nro > 1:
            self.nro = self.nro * self.__factorial_numero(self.nro - 1)
        return self.nro
            
    def __conversion_grados(self, origen, destino):
        # convertir la lista de grados a float
        lista_float = list()
        for f in self.lista:
            nro_float = float(f)
            lista_float.append(nro_float)
        
        if (origen == "celsius" and destino == "celsius") or (origen == "kelvin" and destino == "kelvin") or (origen == "farenheit" and destino == "farenheit"):
            return f"La lista en grados {origen} es: {lista_float}"
        elif origen == "celsius" and destino == "farenheit":
            # for grado in lista_float:
            #     conversion_farenheit = (grado * (9 / 5) + 32)
            #     self.salida_lista.append(conversion_farenheit)
            self.salida_lista = [f"{(grado * (9 / 5) + 32):.2f}" for grado in lista_float]
                
        elif origen == "celsius" and destino == "kelvin":
            # for grado in lista_float:
            #     conversion_kelvin = (grado + 273.15)
            #     self.salida_lista.append(conversion_kelvin)
            self.salida_lista = [f"{(grado + 273.15):.2f}" for grado in lista_float]
        elif origen == "farenheit" and destino == "kelvin":
            # for grado in lista_float:
            #     conversion_kelvin = ((grado - 32) * (5 / 9) + 273.15)
            #     self.salida_lista.append(conversion_kelvin)
            self.salida_lista = [f"{((grado - 32) * (5 / 9) + 273.15):.2f}" for grado in lista_float]
        elif origen == "farenheit" and destino == "celsius":
            # for grado in lista_float:
                # conversion_celsius = (grado - 32) * (5 / 9)
                # self.salida_lista.append(conversion_celsius)
            self.salida_lista = [f"{((grado - 32)*(5 / 9)):.2f}" for grado in lista_float]
        elif origen == "kelvin" and destino == "farenheit":
            for grado in lista_float:
                conversion_farenheit = ((grado - 273.15) * (9 / 5)) + 32
                self.salida_lista.append(f"{conversion_farenheit:.2f}")                
        elif origen == "kelvin" and destino == "celsius":
            for grado in lista_float:
                conversion_celsius = (grado - 273.15)
                self.salida_lista.append(f"{conversion_celsius:.2f}")
            
        else:
            print('Parámetros de Origen o Destino incorrectos')

        return f"La conversion en grados {origen} a grados {destino} es:\n{self.salida_lista}"
            
    def __calcular_mediana(self):
        
        # Si solo igualas las variables (lista_copia = self.lista), 
        # ambas apuntarán al mismo bloque de memoria y cualquier cambio afectará a las dos.
        # lista_desordenada = self.lista
        
        # desordenada es copia de lista
        lista_desordenada = self.lista.copy()
        
        # ordenada es copia de lista que la ordena
        lista_ordenada = sorted(self.lista)
        
        print(lista_desordenada)
        print(lista_ordenada)

        # si el numero de elementos es impar
        if len(lista_ordenada) % 2 == 1:
            # indice = len(lista_ordenada) // 2
            return f"El elemento de la mediana es: {lista_ordenada[len(lista_ordenada) // 2]}" 
        # si el numero de elementos es par
        else:
            indice = len(lista_ordenada) // 2
            elemento1 = lista_ordenada[indice - 1]
            elemento2 = lista_ordenada[indice]
            return f"El elemento de la mediana es: {(elemento1 + elemento2)/2}"
    
    def __calcular_media(self):
        self.salida_numero = sum(self.lista) / len(self.lista)
        return f"La media de los numeros de la lista es: {self.salida_numero:.2f}"
    
    def __calcular_moda(self):
        # el dato que mas se repite
        repite = 0                                                              # 0             2 2 4 
        repite_max = 0                                                          # 0             2 2 4
        evaluar_nro_max = 0                                                     # 0             2 2 4 
        for a in self.lista:                                                    # a = 2         3 4 5 6 2
            repite = len([r for i, r in enumerate(self.lista) if r == a ])      # repite = 2    2 4 2 1 
            if repite_max < repite:                                             #true           f t f f
                repite_max = repite                                             #r_max = 2      2 4 4 4
                evaluar_nro_max = a                                             #e_max = 2      2 4 4 4
        return f"El número {evaluar_nro_max} se repite {repite_max} veces como máximo."
    
    def __calcular_primo(self):
        # [2,3,4,5,6]
        for l in self.lista:        # 2
            if l == 2 and l not in self.salida_lista: 
                self.salida_lista.append(l)
            for i in range(2, l):   # 2,2
                if l % i == 0:
                    # print(f"NO SE TIENE EN CUENTA -> l:{l} - i:{i}")
                    self.__es_primo = False 
                    break 
                else:
                    # print(f"l:{l} - i:{i}")
                    self.__es_primo = True 
                    continue
            if self.__es_primo == True:
                # print(f"SE TIENE EN CUENTA -> l:{l}")
                self.__es_primo = False
                if l not in self.salida_lista:
                    self.salida_lista.append(l)
                
                #if l % i == 0:      # false
                    #break
            #    else:
                #self.salida_lista.append(l)
        