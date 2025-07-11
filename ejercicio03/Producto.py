from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    @staticmethod
    def ejecutar_sql(conn, sql, params=()):
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur

    @staticmethod
    def crear_tabla(conn):
        Producto.ejecutar_sql(conn, """
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                precio FLOAT NOT NULL
            )
        """)

    @staticmethod
    def createProduct(conn, nombre, tipo, precio):
        Producto.ejecutar_sql(conn,
            "INSERT INTO producto (nombre, tipo, precio) VALUES (?, ?, ?)", (nombre, tipo, precio))
        print(f"Producto '{nombre}' agregado.")

    @abstractmethod
    def listar_producto(self):
        pass