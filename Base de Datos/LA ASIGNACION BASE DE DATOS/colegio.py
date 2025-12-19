import mysql.connector

# Conexión inicial (sin seleccionar BD)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexion.cursor()

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS colegio;")
cursor.execute("USE colegio;")

# Crear tabla estudiantes
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INT NOT NULL
);
""")

# Crear tabla cursos
cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);
""")

# Crear tabla matriculas
cursor.execute("""
CREATE TABLE IF NOT EXISTS matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_curso INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);
""")

print("Base de datos y tablas creadas exitosamente.")

cursor.close()
conexion.close()
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="colegio"
)

cursor = conexion.cursor()

# Insertar estudiantes
cursor.execute("INSERT INTO estudiantes (nombre, apellido, edad) VALUES ('Ana', 'Pérez', 15);")
cursor.execute("INSERT INTO estudiantes (nombre, apellido, edad) VALUES ('Luis', 'Martínez', 16);")

# Insertar cursos
cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('Matemáticas', 'Curso básico de álgebra');")
cursor.execute("INSERT INTO cursos (nombre, descripcion) VALUES ('Historia', 'Historia universal');")

# Insertar matrículas
cursor.execute("INSERT INTO matriculas (id_estudiante, id_curso, fecha) VALUES (1, 1, '2025-02-01');")
cursor.execute("INSERT INTO matriculas (id_estudiante, id_curso, fecha) VALUES (2, 2, '2025-02-01');")

conexion.commit()

print("Datos insertados correctamente.")

cursor.close()
conexion.close()
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="colegio"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM estudiantes;")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="colegio"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM cursos;")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="colegio"
)

cursor = conexion.cursor()

cursor.execute("""
SELECT e.nombre, e.apellido, c.nombre, m.fecha
FROM matriculas m
INNER JOIN estudiantes e ON m.id_estudiante = e.id
INNER JOIN cursos c ON m.id_curso = c.id;
""")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()
