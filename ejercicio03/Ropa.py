from Producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)
    
    def listar_producto(self):
        print(f"[ROPA] {self.nombre.upper()} - Precio: ${self.precio:.2f}")