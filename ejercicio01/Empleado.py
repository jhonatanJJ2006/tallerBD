from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, rol, horas):
        self.nombre = nombre
        self.rol = rol
        self.salario = 0
        self.horas = horas

    @staticmethod
    def ejecutar_sql(conn, sql, params=()):
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur

    @staticmethod
    def crear_tabla(conn):
        Empleado.ejecutar_sql(conn, """
            CREATE TABLE IF NOT EXISTS empleado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                rol TEXT NOT NULL,
                salario FLOAT NOT NULL,
                valorhora FLOAT NOT NULL,
                horas INT NOT NULL
            )
        """)

    @staticmethod
    def updateEmployee(conn, id_, salario):
        Empleado.ejecutar_sql(conn, "UPDATE empleado SET salario = ? WHERE id = ?", (salario, id_))

    @staticmethod
    def createEmployee(conn, nombre, rol, salario, valorHora, horas):
        Empleado.ejecutar_sql(conn, 
            "INSERT INTO empleado (nombre, rol, salario, valorhora, horas) VALUES (?, ?, ?, ?, ?)", 
            (nombre, rol, salario, valorHora, horas))
        print(f"Empleado '{nombre}' agregado.")

    @staticmethod
    def calcularSalario(conn, nombre):
        cur = Empleado.ejecutar_sql(conn, "SELECT * FROM empleado WHERE nombre=?", (nombre,))
        fila = cur.fetchone()
        if fila is None:
            print(f"No se encontró ningún empleado con nombre {nombre}")
            return
        valorHora = fila["valorhora"]
        horas = fila["horas"]
        salario = valorHora * horas
        Empleado.ejecutar_sql(conn, "UPDATE empleado SET salario=? WHERE nombre=?", (salario, nombre))

    @staticmethod
    def listar_empleados(conn):
        cur = Empleado.ejecutar_sql(conn, "SELECT * FROM empleado")
        empleados = cur.fetchall()
        print("\n--- LISTA DE EMPLEADOS ---")
        if not empleados:
            print("No hay empleados registrados.")
            return
        for emp in empleados:
            print(f"ID: {emp['id']} | Nombre: {emp['nombre']} | Rol: {emp['rol']} | Salario: ${emp['salario']:.2f}")
