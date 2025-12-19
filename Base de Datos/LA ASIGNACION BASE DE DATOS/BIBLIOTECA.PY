import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexion.cursor()

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")
print("Base de datos creada correctamente.")

# Usar la BD
cursor.execute("USE biblioteca")

# Crear tabla autores
cursor.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(100)
)
""")

# Crear tabla libros
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    año INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
)
""")

print("Tablas creadas correctamente.")

conexion.close()
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = conexion.cursor()

# Insertar autores
sql_autor = "INSERT INTO autores (nombre, nacionalidad) VALUES (%s, %s)"
datos_autores = [
    ("Gabriel García Márquez", "Colombia"),
    ("Julio Cortázar", "Argentina"),
    ("Isabel Allende", "Chile")
]

cursor.executemany(sql_autor, datos_autores)
conexion.commit()

# Insertar libros
sql_libro = "INSERT INTO libros (titulo, año, id_autor) VALUES (%s, %s, %s)"
datos_libros = [
    ("Cien años de soledad", 1967, 1),
    ("Rayuela", 1963, 2),
    ("La casa de los espíritus", 1982, 3)
]

cursor.executemany(sql_libro, datos_libros)
conexion.commit()

print("Datos insertados correctamente.")

conexion.close()
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = conexion.cursor()

query = """
SELECT libros.titulo, libros.año, autores.nombre
FROM libros
INNER JOIN autores ON libros.id_autor = autores.id_autor
"""

cursor.execute(query)
resultados = cursor.fetchall()

for titulo, ano, autor in resultados:
    print(f"Título: {titulo} | Año: {ano} | Autor: {autor}")

conexion.close()
