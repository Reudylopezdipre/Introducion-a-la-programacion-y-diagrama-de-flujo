import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # si tienes contraseña, ponla aquí
    )
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS ventas")
cursor.execute("USE ventas")

# Tabla clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
)
""")

# Tabla productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
)
""")

# Tabla facturas
cursor.execute("""
CREATE TABLE IF NOT EXISTS facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT DEFAULT 1,
    total DECIMAL(10,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
)
""")

print("Base de datos y tablas creadas correctamente.")
conexion.close()
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ventas"
)

cursor = conexion.cursor()

### Insertar clientes ###
sql_clientes = """
INSERT INTO clientes (nombre, telefono, correo)
VALUES (%s, %s, %s)
"""

datos_clientes = [
    ("Ana Pérez", "829-555-1234", "ana@gmail.com"),
    ("Carlos Méndez", "809-444-9988", "carlos@gmail.com"),
    ("María López", "849-777-6622", "maria@hotmail.com")
]

cursor.executemany(sql_clientes, datos_clientes)
conexion.commit()


### Insertar productos ###
sql_productos = """
INSERT INTO productos (nombre, precio)
VALUES (%s, %s)
"""

datos_productos = [
    ("Laptop Lenovo", 45000.00),
    ("Mouse Logitech", 1500.00),
    ("Monitor LG 24\"", 12000.00)
]

cursor.executemany(sql_productos, datos_productos)
conexion.commit()


### Insertar facturas ###
sql_facturas = """
INSERT INTO facturas (id_cliente, id_producto, cantidad, total)
VALUES (%s, %s, %s, %s)
"""

datos_facturas = [
    (1, 1, 1, 45000.00),
    (2, 2, 2, 3000.00),
    (3, 1, 1, 45000.00),
    (3, 3, 1, 12000.00)
]

cursor.executemany(sql_facturas, datos_facturas)
conexion.commit()

print("Datos insertados correctamente.")
conexion.close()
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ventas"
)

cursor = conexion.cursor()

query = """
SELECT 
    facturas.id_factura,
    clientes.nombre AS cliente,
    productos.nombre AS producto,
    facturas.cantidad,
    facturas.total,
    facturas.fecha
FROM facturas
INNER JOIN clientes ON facturas.id_cliente = clientes.id_cliente
INNER JOIN productos ON facturas.id_producto = productos.id_producto
"""

cursor.execute(query)
resultados = cursor.fetchall()

for factura in resultados:
    print(f"Factura ID: {factura[0]} | Cliente: {factura[1]} | Producto: {factura[2]} | Cantidad: {factura[3]} | Total: {factura[4]} | Fecha: {factura[5]}")

conexion.close()
