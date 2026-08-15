class Gato:
    def __init__(self, nombre, color, raza, edad, sexo, energia):
        # Defino los atributos
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.energia = energia
    
    # Método presentar
    def presentarse(self):
        # self.descarga_energia(5)
        print(f'Nombre: {self.nombre}, Color: {self.color}, Raza: {self.raza}, Edad: {self.edad}, Sexo: {self.sexo}, Energía {self.energia}.')
    
    def maullar(self):
        self.descarga_energia(5)
        print('Miau Miau Miauuuuuuu')

    def comer(self):
        if self.energia < 100:
            self.carga_energia(10)
            print('El gato está comiendo')
        else:
            print("El gato dejó de comer!")
            self.descarga_energia(5)
    
    def jugar(self):
        if self.energia > 0:
            print('El gato esta jugando...')
            self.descarga_energia(25)
        else:
            print('El gato esta muerto de hambre!')
    
    def carga_energia(self, energia):
        self.energia += energia
        
    def descarga_energia(self, energia):
        self.energia -= energia
            
        