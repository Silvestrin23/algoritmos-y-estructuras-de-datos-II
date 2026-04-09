lista=[]
class Figura:
    def __init__(self,color):
        self.color=color
    def area(self):
        return 0   
class Rectangulo(Figura):
    def __init__(self,color,base,altura):
        super().__init__(color)
        self.base=base
        self.altura=altura
    def area(self):
        print(self.altura*self.base)
class Circulo(Figura):
    def __init__(self,color,radio):
        super().__init__(color)
        self.radio=radio
    
    def area(self):
        print((self.radio*self.radio)*3.14)
    
rectangulo=Rectangulo("rojo",2,3)
circulo=Circulo("Azul",3) 
lista.append(rectangulo)
lista.append(circulo)
for i in range(len(lista)):
    lista[i].area()