import sqlite3
from Empleado import Empleado
from Gerente import Gerente
from Desarrollador import Desarrollador

def menu():
    conn = sqlite3.connect("empresa.db")
    conn.row_factory = sqlite3.Row
    Empleado.crear_tabla(conn)

    while True:
        print("\n--- MENÚ DE EMPRESA ---")
        print("1. Registrar Gerente")
        print("2. Registrar Desarrollador")
        print("3. Ver empleados registrados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del gerente: ")
            horas = int(input("Horas trabajadas: "))
            gerente = Gerente(nombre, "Gerente", horas)
            salario = gerente.valorHora * gerente.horas
            gerente.createEmployee(conn, gerente.nombre, gerente.rol, salario, gerente.valorHora, gerente.horas)

        elif opcion == "2":
            nombre = input("Nombre del desarrollador: ")
            horas = int(input("Horas trabajadas: "))
            desarrollador = Desarrollador(nombre, "Desarrollador", horas)
            salario = desarrollador.valorHora * desarrollador.horas
            desarrollador.createEmployee(conn, desarrollador.nombre, desarrollador.rol, salario, desarrollador.valorHora, desarrollador.horas)

        elif opcion == "3":
            Empleado.listar_empleados(conn)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

    conn.close()

if __name__ == "__main__":
    menu()
