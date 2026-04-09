lista=[]
class Vehiculo:
    def __init__(self,marca,velocidad_max):
        self.marca=marca
        self.velocidad_max=velocidad_max
    
    def describir():
        pass
    
class Auto(Vehiculo):
    def __init__(self,marca,velocidad_max,cantidad_puertas):
        super().__init__(marca,velocidad_max)
        self.cantidad_puertas=cantidad_puertas
    def describir(self):
        print("Marca:",self.marca,"Velocidad:",self.velocidad_max,"Cantidad de puertas:",self.cantidad_puertas)

class Moto(Vehiculo):
    def __init__(self,marca,velocidad_max,cc):
        super().__init__(marca,velocidad_max)
        self.cc=cc
    
    def describir(self):
        print("Marca:",self.marca,"Velocidad:",self.velocidad_max,"CC:",self.cc)
        
fiat=Auto("Fiat",120,5)
lista.append(fiat)

ns=Moto("Bajaj",140,400)
lista.append(ns)
for i in range(len(lista)):
    lista[i].describir()