DROP DATABASE IF EXISTS colegio;
CREATE DATABASE colegio;
USE colegio;
CREATE TABLE departamentos (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_departamento VARCHAR(100) NOT NULL
);

INSERT INTO departamentos (nombre_departamento) VALUES
('Informática'),
('Administración'),
('Contabilidad'),
('Diseño'),
('Electrónica');
CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_nacimiento DATE,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
);

INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, id_departamento) VALUES
('Ana', 'García', '2005-01-12', 1),
('Luis', 'Martínez', '2003-04-22', 2),
('María', 'García', '2004-07-09', 1),
('Carlos', 'Pérez', '2002-03-15', 3),
('Andrea', 'Lopez', '2003-06-30', 4),
('Amanda', 'Santos', '2005-02-10', 1),
('Bryan', 'Valdez', '2001-11-02', 5),
('Alberto', 'Ruiz', '2002-09-25', 2),
('Pedro', 'Jimenez', '2003-02-14', 3),
('Angel', 'Reyes', '2004-05-05', 1);
CREATE TABLE profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100)
);

INSERT INTO profesores (nombre, apellido) VALUES
('Juan', 'López'),
('María', 'Torres'),
('Pedro', 'Ramírez');
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES profesores(id_profesor)
);

INSERT INTO cursos (nombre, id_profesor) VALUES
('Matemáticas', 1),
('Historia', 2),
('Programación', 1),
('Electrónica Básica', 3),
('Contabilidad I', 2);
CREATE TABLE calificaciones (
    id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    calificacion DECIMAL(5,2),
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

INSERT INTO calificaciones (id_estudiante, id_curso, calificacion) VALUES
(1, 3, 95),
(2, 1, 88),
(3, 3, 91),
(4, 4, 83),
(5, 2, 72),
(6, 3, 98),
(7, 4, 64),
(8, 5, 87),
(9, 1, 78),
(10, 3, 92);
-- 1. Seleccionar todos los estudiantes
SELECT * FROM estudiantes;

-- 2. Nombres y apellidos
SELECT nombre, apellido FROM estudiantes;

-- 3. Filtrar por departamento
SELECT * FROM estudiantes WHERE id_departamento = 1;

-- 4. Ordenar por fecha de nacimiento (más viejos primero)
SELECT * FROM estudiantes ORDER BY fecha_nacimiento ASC;

-- 5. Contar estudiantes
SELECT COUNT(*) AS total_estudiantes FROM estudiantes;

-- 6. Apellido García
SELECT * FROM estudiantes WHERE apellido = 'García';

-- 7. Nombres que empiezan con A
SELECT * FROM estudiantes WHERE nombre LIKE 'A%';

-- 8. JOIN estudiante - departamento
SELECT e.nombre, e.apellido, d.nombre_departamento
FROM estudiantes e
INNER JOIN departamentos d ON e.id_departamento = d.id_departamento;

-- 9. Promedio por estudiante
SELECT e.nombre, e.apellido, AVG(c.calificacion) AS promedio
FROM calificaciones c
INNER JOIN estudiantes e ON c.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante;

-- 10. Cantidad de estudiantes por departamento
SELECT d.nombre_departamento, COUNT(e.id_estudiante) AS total_estudiantes
FROM departamentos d
LEFT JOIN estudiantes e ON d.id_departamento = e.id_departamento
GROUP BY d.id_departamento;

-- 11. Cursos por profesor
SELECT p.nombre AS profesor, p.apellido, c.nombre AS curso
FROM cursos c
INNER JOIN profesores p ON c.id_profesor = p.id_profesor;

-- 12. Estudiantes con promedio > 90
SELECT e.nombre, e.apellido, AVG(c.calificacion) AS promedio
FROM calificaciones c
INNER JOIN estudiantes e ON c.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante
HAVING promedio > 90;

-- 13. Top 5 mejores promedios
SELECT e.nombre, e.apellido, AVG(c.calificacion) AS promedio
FROM calificaciones c
INNER JOIN estudiantes e ON c.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante
ORDER BY promedio DESC
LIMIT 5;
