from Empleado import Empleado

class Desarrollador(Empleado):
    def __init__(self, nombre, rol, horas):
        super().__init__(nombre, rol , horas)
        self.valorHora = 20