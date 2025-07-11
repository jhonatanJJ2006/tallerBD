import sqlite3
from Producto import Producto
from Electronica import Electronica
from Ropa import Ropa

def menu():
    conn = sqlite3.connect("empresa.db")
    conn.row_factory = sqlite3.Row
    Producto.crear_tabla(conn)

    while True:
        print("\n--- MENÚ DE EMPRESA ---")
        print("1. Registrar electronico")
        print("2. Registrar ropa")
        print("3. Ver productos registrados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del electronico: ")
            precio = input("Precio del electronico: ")
            producto = Electronica(nombre, "Electronico", precio)
            producto.createProduct(conn, producto.nombre, producto.tipo, producto.precio)

        elif opcion == "2":
            nombre = input("Nombre de la Ropa: ")
            precio = input("Precio de la ropa: ")
            producto = Ropa(nombre, "Ropa", precio)
            producto.createProduct(conn, producto.nombre, producto.tipo, producto.precio)

        elif opcion == "3":
            cur = conn.cursor()
            cur.execute("SELECT * FROM producto")
            productos = cur.fetchall()

            for producto in productos:
                nombre = producto["nombre"]
                tipo = producto["tipo"]
                precio = producto["precio"]

                if tipo.lower() == 'electronico':
                    p = Electronica(nombre, tipo, precio)
                else :
                    p = Ropa(nombre, tipo, precio)

                p.listar_producto()


        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")
            conn.close()

if __name__ == "__main__":
    menu()
