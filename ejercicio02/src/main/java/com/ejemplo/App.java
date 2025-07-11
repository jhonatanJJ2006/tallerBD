package com.ejemplo;

import java.sql.*;
import java.util.Scanner;

// Clase principal
public class App {
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        // Ruta de la base de datos SQLite
        String url = "jdbc:sqlite:Vehiculos.db";
        vehiculo[] vehiculos = null;
        int op = 0, index;

        // Conexión a la base de datos
        try (Connection conn = DriverManager.getConnection(url)) {
            if (conn != null) {
                System.out.println("Conexión establecida a SQLite.");
                crearTabla(conn); // Crear tabla si no existe

                System.out.println("Bienvenido a la base de datos de Vehículos");

                // Menú de opciones
                do {
                    System.out.println("\nOpciones:");
                    op = menu();
                    switch (op) {
                        case 1:
                            // Agregar nuevos vehículos
                            System.out.println("Ingrese el número de vehículos a agregar:");
                            int numVehiculos = sc.nextInt();
                            vehiculos = new vehiculo[numVehiculos];
                            for (index = 0; index < numVehiculos; index++) {
                                agregarVehiculo(conn, vehiculos, index);
                            }
                            break;
                        case 2:
                            // Mostrar los vehículos almacenados en memoria
                            System.out.println("Mostrando vehículos:");
                            for (vehiculo vehiculo : vehiculos) {
                                vehiculo.informacion(); // Polimorfismo
                            }
                            break;
                        default:
                            System.out.println("Opción no válida. Intente de nuevo.");
                            break;
                    }

                } while (op != 0);

                System.out.println("Gracias por usar la base de datos de Vehículos. ¡Hasta luego!");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    // Menú de opciones
    public static int menu() {
        System.out.println("1. Agregar Vehículo");
        System.out.println("2. Mostrar Vehículos");
        System.out.println("0. Salir");
        return sc.nextInt();
    }

    // Crea la tabla "vehiculos" si no existe
    public static void crearTabla(Connection conn) {
        String sqlCrear = "CREATE TABLE IF NOT EXISTS vehiculos (" +
                          "Indice INTEGER PRIMARY KEY AUTOINCREMENT, " +
                          "Tipo TEXT, Marca TEXT, Modelo TEXT)";
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(sqlCrear);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    // Agrega un vehículo a la base de datos y al arreglo
    public static void agregarVehiculo(Connection conn, vehiculo[] vehiculos, int index) {
        System.out.println("Ingrese el tipo de vehículo (Coche/Moto): ");
        String tipo = sc.next();

        System.out.println("Ingrese la marca: ");
        String marca = sc.next();

        System.out.println("Ingrese el modelo: ");
        String modelo = sc.next();

        System.out.println("Ingrese el año: ");
        int year = sc.nextInt();

        // Crear objeto según el tipo usando herencia y polimorfismo
        if (tipo.equalsIgnoreCase("Coche")) {
            vehiculos[index] = new coche(marca, modelo, year);
        } else if (tipo.equalsIgnoreCase("Moto")) {
            vehiculos[index] = new moto(marca, modelo, year);
        } else {
            System.out.println("Tipo de vehículo no reconocido.");
            return;
        }

        // Insertar en la base de datos (sin el campo Indice, que es autoincremental)
        try {
            String sqlInsertar = "INSERT INTO vehiculos(Tipo, Marca, Modelo) VALUES(?, ?, ?)";
            PreparedStatement pstmt = conn.prepareStatement(sqlInsertar);
            pstmt.setString(1, tipo);
            pstmt.setString(2, vehiculos[index].marca);
            pstmt.setString(3, vehiculos[index].modelo);
            pstmt.executeUpdate();
            System.out.println("Vehículo agregado exitosamente.");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    // Muestra todos los vehículos desde la base de datos (no desde memoria)
    public static void mostrarVehiculos(Connection conn) {
        String sqlMostrar = "SELECT * FROM vehiculos";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sqlMostrar)) {
            while (rs.next()) {
                System.out.println("Tipo: " + rs.getString("Tipo") + 
                                   ", Marca: " + rs.getString("Marca") + 
                                   ", Modelo: " + rs.getString("Modelo"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}

// Clase base abstracta
abstract class vehiculo {
    public String marca, modelo;
    public int year;

    public vehiculo(String marca, String modelo, int year) {
        this.marca = marca;
        this.modelo = modelo;
        this.year = year;
    }

    // Método abstracto para mostrar información (polimorfismo)
    public abstract void informacion();
}

// Subclase que representa un coche
class coche extends vehiculo {
    public coche(String marca, String modelo, int year) {
        super(marca, modelo, year);
    }

    // Implementación del método abstracto
    public void informacion() {
        System.out.println("Coche: " + marca + ", Modelo: " + modelo + ", Año: " + year);
    }
}

// Subclase que representa una moto
class moto extends vehiculo {
    public moto(String marca, String modelo, int year) {
        super(marca, modelo, year);
    }

    // Implementación del método abstracto
    public void informacion() {
        System.out.println("Moto: " + marca + ", Modelo: " + modelo + ", Año: " + year);
    }
}
