from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, rol, horas):
        super().__init__(nombre, rol, horas)
        self.valorHora = 10