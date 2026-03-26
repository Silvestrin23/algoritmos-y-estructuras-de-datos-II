from abc import ABC, abstractmethod
#. Crear una clase abstracta Empleado:
# Atributos: nombre y salario_base más lo que ud. considere.
# Método abstracto: calcular_sueldo().
# Método normal: mostrar_datos() (que imprima sólo el nombre y el salario
#base).

#2. Crear clases que hereden de Empleado:
#○ EmpleadoContratado:
#■ Atributo adicional: valor_hora.
#■ Atributo adicional: horas_trabajadas.
#■ Implementar calcular_sueldo(): (valor_hora * horas_trabajadas).
#○ EmpleadoFijo:
#■ Atributo adicional: bono_antiguedad.
#■ Implementar calcular_sueldo(): (salario_base + bono_antiguedad).
class Empleado(ABC):
    def __init__(self,legajo,nombre,salario_base):
        self.legajo=legajo
        self.nombre=nombre
        self.salario_base=salario_base
        self.sueldo_bruto=0
    def mostrar_datos(self):
        print("El empleado:",self.nombre,"tiene de salario base:",self.salario_base) 

    @abstractmethod
    def calcular_sueldo(self):
        pass
    
class EmpleadoContratado(Empleado):
    def __init__(self,legajo,nombre,valor_hora,horas_trabajadas):
        super().__init__(legajo,nombre,0)
        self.valor_hora=valor_hora
        self.horas_trabajadas=horas_trabajadas
        
        
    def calcular_sueldo(self):
        self.sueldo_bruto=self.valor_hora*self.horas_trabajadas
        print("Sueldo bruto empleado contratado:",self.sueldo_bruto)

    def actualizar_datos(self,horas_trabajadas):
        self.horas_trabajadas=horas_trabajadas
    
    

class EmpleadoFijo(Empleado):
    def __init__(self,legajo,nombre,salario_base,bono_antiguedad):
        super().__init__(legajo,nombre,salario_base)
        self.bono_antiguedad=bono_antiguedad

    def calcular_sueldo(self):
        self.sueldo_bruto=self.salario_base+self.bono_antiguedad
        print("Sueldo bruto empleado fijo:",self.sueldo_bruto)
    
    def actualizar_datos(self,bono_antiguedad):
        self.bono_antiguedad=bono_antiguedad

empleado_contratado= EmpleadoContratado(301,"Mateo",9000,160)
empleado_fijo= EmpleadoFijo(108,"Lucas",450000,100000)
empleado_contratado.mostrar_datos()
empleado_contratado.calcular_sueldo()
print("")
empleado_fijo.mostrar_datos()
empleado_fijo.calcular_sueldo()


